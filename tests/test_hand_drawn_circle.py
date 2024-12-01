import manim as mn
from manim import Scene

from manim_motion_design.shapes import HandDrawnCircle


class TestHandDrawnCircle(Scene):
    def construct(self):
        hand_drawn_circle = HandDrawnCircle()
        self.play(mn.Create(hand_drawn_circle))
        self.play(mn.Uncreate(hand_drawn_circle))

        sq = mn.Square(3)
        self.add(sq)
        hand_drawn_circle = HandDrawnCircle(sq)
        self.play(mn.Create(hand_drawn_circle))
        self.play(mn.Uncreate(hand_drawn_circle))
