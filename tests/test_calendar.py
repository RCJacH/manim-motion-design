import manim as mn
from manim import Scene

from manim_motion_design.charts import MonthlyCalendar


class TestCalendar(Scene):
    def construct(self):
        calendar = MonthlyCalendar()
        self.play(mn.Create(calendar))
        self.play(mn.Uncreate(calendar))
