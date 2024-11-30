import manim as mn
from manim import Scene

from manim_motion_design.shapes import Cross


class TestStrippedCircle(Scene):
    def construct(self):
        cross = Cross()
        self.play(mn.Create(cross))
        self.play(mn.Uncreate(cross))
