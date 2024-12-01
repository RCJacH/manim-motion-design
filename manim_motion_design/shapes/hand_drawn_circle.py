try:
    import manimgl as mn
except ModuleNotFoundError:
    import manim as mn

import numpy as np


class HandDrawnCircle(mn.VGroup):
    def __init__(
        self,
        mobject=mn.ORIGIN,
        buff=0.5,
        radius=1,
        number_of_points=4,
        radius_variation=0.1,
        rotation_variation=(0, 0.4),
        start_angle_variation=0.1,
        color=mn.RED,
        rnd=np.random,
        **kwargs,
    ):
        super().__init__()
        last_point = mn.ORIGIN
        cur_radius = radius
        radius_rnd = self._get_rnd_array(radius_variation)
        rotation_rnd = self._get_rnd_array(rotation_variation)
        start_angle = self._get_rnd_array(start_angle_variation)
        start_angle = rnd.uniform(*start_angle) * mn.TAU
        each_angle = mn.TAU / number_of_points
        angle = each_angle

        for _ in range(number_of_points):
            cur_radius += rnd.uniform(*radius_rnd) * cur_radius
            angle = each_angle * (1 + rnd.uniform(*rotation_rnd))
            quarter = self._get_quarter(
                cur_radius, start_angle, angle, last_point, color=color, **kwargs
            )
            self.add(quarter)
            last_point = quarter.get_last_point()
            start_angle = start_angle + angle

        try:
            buff = buff[:2]
        except TypeError:
            buff = float(buff)
            buff = (buff, buff)

        if isinstance(mobject, mn.Mobject):
            self.stretch_to_fit_width(mobject.width + buff[0])
            self.stretch_to_fit_height(mobject.height + buff[1])

        self.move_to(mobject)

    @staticmethod
    def _get_rnd_array(v):
        try:
            v = v[:2]
        except TypeError:
            v = float(v)
            v = (-v, v)
        finally:
            rnd_array = np.array(v)
        return rnd_array

    def _get_quarter(
        self, radius=1, start_angle=0, angle=mn.TAU / 4, last_point=None, **kwargs
    ):
        if last_point is None:
            arc_center = mn.ORIGIN
        else:
            cx = radius * np.cos(start_angle)
            cy = radius * np.sin(start_angle)
            new_start_point = [cx, cy, 0]
            arc_center = last_point - new_start_point
        return mn.Arc(radius, 0, angle, arc_center=arc_center, **kwargs).rotate(
            start_angle, about_point=arc_center
        )

    @mn.override_animation(mn.Create)
    def _overide_create(self, run_time=1, **kwargs):
        each_time = run_time / len(self)
        return mn.Succession(
            *(
                mn.Create(
                    x,
                    rate_func=mn.rate_functions.linear,
                    run_time=each_time,
                )
                for x in self
            ),
            **kwargs,
        )

    @mn.override_animation(mn.Uncreate)
    def _overide_uncreate(self, run_time=1, **kwargs):
        each_time = run_time / len(self)
        return mn.Succession(
            *(
                mn.Uncreate(
                    x,
                    rate_func=mn.rate_functions.linear,
                    run_time=each_time,
                )
                for x in self[::-1]
            ),
            **kwargs,
        )
