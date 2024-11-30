try:
    import manimgl as mn
except ModuleNotFoundError:
    import manim as mn

import numpy as np


class Cross(mn.Polygram):
    DEFAULT_SIZE = 1.0

    def __init__(
        self, mobject: mn.Mobject | mn.Point = mn.ORIGIN, size=DEFAULT_SIZE, **kwargs
    ):
        color = kwargs.pop("color", mn.RED)
        try:
            size = size[:2]
        except TypeError:
            size = [size, size]
        if isinstance(mobject, mn.Mobject):
            mw = mobject.width * 0.5 * size[0]
            mh = mobject.height * 0.5 * size[1]
            center = mobject.get_center()
        elif isinstance(mobject, mn.Point) or isinstance(mobject, np.ndarray):
            mw = 0.5 * size[0]
            mh = 0.5 * size[1]
            center = mobject

        stroke1 = [
            center + [-mw, mh, 0],
            center + [mw, -mh, 0],
        ]
        stroke2 = [
            center + [mw, mh, 0],
            center + [-mw, -mh, 0],
        ]
        super().__init__(
            stroke1,
            stroke2,
            color=color,
            **kwargs,
        )
