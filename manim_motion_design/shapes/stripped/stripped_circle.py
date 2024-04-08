import manim as mn

from manim_motion_design.shapes import ArcRing


class StrippedCircle(mn.VGroup):
    def __init__(
        self, rings, colors, sectors=1, scale=1, **kwargs,
    ):
        super().__init__()
        radius_per_ring = scale / rings
        common_stroke_width = 100 * radius_per_ring
        self.add(
            *(
                ArcRing(
                    radius=radius_per_ring * (ring_count + 0.5),
                    sectors=sectors,
                    color=colors[ring_count % len(colors)],
                    stroke_width=common_stroke_width,
                    **kwargs,
                ) for ring_count in range(rings)
            )
        )

    @mn.override_animation(mn.Create)
    def _create_override(self, **kwargs):
        return mn.LaggedStart(
            *(mn.Create(x) for x in self),
            **kwargs,
        )

    @mn.override_animation(mn.Uncreate)
    def _uncreate_override(self, flipped=False, reversed=True, **kwargs):
        return mn.LaggedStart(
            *(mn.Uncreate(x, flipped=flipped) for x in (self[::-1] if reversed else self)),
            remover=True,
            **kwargs,
        )
