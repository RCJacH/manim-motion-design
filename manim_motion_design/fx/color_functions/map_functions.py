import manim as mn


def map_color(
    source_color: mn.ManimColor,
    map_black_to: mn.ManimColor = mn.BLACK,
    map_white_to: mn.ManimColor = mn.WHITE,
    amount: float = 1.0,
) -> mn.ManimColor:
    source_rgb = source_color.to_rgb()
    black_rgb = map_black_to.to_rgb()
    white_rgb = map_white_to.to_rgb()
    return mn.ManimColor.from_rgb([
        mn.interpolate(
            source_rgb[i],
            mn.interpolate(black_rgb[i], white_rgb[i], source_rgb[i]),
            amount
        )
        for i in range(3)
    ])
