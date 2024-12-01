try:
    import manimgl as mn
except ModuleNotFoundError:
    import manim as mn

import numpy as np


class Check(mn.Polygram):
    DEFAULT_SIZE = 1.0

    def __init__(
        self, mobject: mn.Mobject | mn.Point = mn.ORIGIN, size=DEFAULT_SIZE, **kwargs
    ):
        color = kwargs.pop("color", mn.GREEN)
        points = [[mn.LEFT, mn.ORIGIN], [mn.ORIGIN, mn.UP * 2]]
        super().__init__(
            *points,
            color=color,
            **kwargs,
        )
        self.rotate(mn.PI * -0.25, about_point=mn.ORIGIN).shift(mn.DOWN * 0.5)
        self.replace(mobject)

        try:
            size = size[:2]
        except TypeError:
            if size != 1.0:
                self.scale(size)
        else:
            for ii in range(2):
                self.stretch(size[ii], ii)
