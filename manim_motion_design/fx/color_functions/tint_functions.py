import manim as mn

from manim_motion_design.fx.color_functions import map_color


def tint_from_lightness(source_lightness: float, **kwargs) -> mn.ManimColor:
    return map_color(
        mn.ManimColor.from_rgb([source_lightness,] * 3),
        **kwargs,
    )
