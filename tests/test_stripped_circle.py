import manim as mn

from manim_motion_design.shapes import StrippedCircle
from manim_motion_design.fx.color_functions import tint_from_lightness


class TestStrippedCircle(mn.Scene):
    def construct(self):
        ref_circle = mn.Circle(radius=9, color=mn.GREEN, fill_opacity=1)
        self.add(ref_circle)
        self.wait(0.5)
        lights = [225, 80, 168, 255, 53, 36, 139, 239]
        colors = [tint_from_lightness(l / 255, map_black_to=mn.ManimColor.from_hex("#007984")) for l in lights]
        ele = StrippedCircle(
            8,
            colors,
            scale=9,
            sectors=2,
            start_angle=0,
        )
        self.play(mn.Create(ele, lag_ratio=0.15))
        ref_circle.set_color(mn.RED)
        self.play(mn.Uncreate(ele, flipped=True, lag_ratio=0.15))
