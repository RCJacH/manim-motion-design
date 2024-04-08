import math

import manim as mn


class ArcRing(mn.VGroup):
    def __init__(
        self,
        radius: float,
        sectors: int,
        color = mn.WHITE,
        start_angle: float = mn.PI*0.5,
        stroke_width: float = 1.0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        angle = -mn.TAU / sectors
        self.add(
            *(
                mn.Arc(
                    radius=radius,
                    start_angle=start_angle + i * angle,
                    angle=angle,
                    stroke_color=color,
                    stroke_width=stroke_width,
                    **kwargs,
                ) for i in range(sectors)
            )
        )


    @mn.override_animation(mn.Create)
    def _create_override(self, rate_func=mn.rate_functions.ease_in_out_quad, **kwargs):
        return mn.AnimationGroup(
            *(mn.Create(x) for x in self),
            rate_func=rate_func,
            **kwargs,
        )

    @mn.override_animation(mn.Uncreate)
    def _uncreate_override(self, flipped=False, rate_func=mn.rate_functions.ease_in_out_quad, **kwargs):
        if flipped is not False:
            for x in self:
                x.set_points(x.get_all_points()[::-1])
        return mn.AnimationGroup(
            *(mn.Uncreate(x) for x in self),
            rate_func=rate_func,
            **kwargs,
        )
