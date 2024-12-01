import manim as mn
from manim import Scene

from manim_motion_design.charts import MonthlyCalendar, create_calendars


class TestCalendar(Scene):
    def construct(self):
        calendar = MonthlyCalendar()
        self.play(mn.Create(calendar))
        self.play(mn.Uncreate(calendar))

        calendars = create_calendars(2222, (1, 4))
        calendars.arrange_in_grid(2, 2)
        self.play(*(mn.Create(x) for x in calendars))
        self.play(*(mn.Uncreate(x) for x in calendars))
