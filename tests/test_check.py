import manim as mn
from manim import Scene

from manim_motion_design.shapes import Check


class TestCheck(Scene):
    def construct(self):
        sq = mn.Square(1)
        check = Check(sq, [1.2, 0.8])
        self.add(sq)
        self.play(mn.Create(check))
        self.play(mn.Uncreate(check))
