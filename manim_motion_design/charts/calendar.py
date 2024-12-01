import datetime
import calendar

try:
    import manimgl as mn
except ModuleNotFoundError:
    import manim as mn


class MonthlyCalendar(mn.Group):
    FONT = "Arial"
    FONT_SIZE = 30
    HEADER_HEIGHT_RATIO = 0.3
    INITIAL_HUE = 1.0
    MONTH_BG_COLORS = [
        mn.ManimColor(x)
        for x in [
            "#79bac4",
            "#8badd9",
            "#a39fe0",
            "#be94d9",
            "#d28dc4",
            "#db8ea8",
            "#d6958c",
            "#c5a277",
            "#acb06f",
            "#92bc77",
            "#7ec28c",
            "#75c2a8",
        ]
    ]
    WEEK_BG_COLORS = [
        mn.ManimColor(x)
        for x in [
            "#60a6b1",
            "#7298c7",
            "#8d89cf",
            "#aa7cc7",
            "#c075b1",
            "#ca7692",
            "#c47e73",
            "#b28c5d",
            "#979b54",
            "#7aa85d",
            "#64af73",
            "#5aae92",
        ]
    ]
    DAY_BG_COLORS = [
        mn.ManimColor(x)
        for x in [
            "#e1f3f5",
            "#e5effb",
            "#ecebfd",
            "#f3e8fb",
            "#f9e6f5",
            "#fce6ed",
            "#fae8e6",
            "#f6ece0",
            "#eff0de",
            "#e7f3e0",
            "#e2f5e6",
            "#dff5ed",
        ]
    ]

    def __new__(cls, *args, **kwargs):
        group = mn.Group.__new__(cls)
        group.MONTH_TEXTS = [
            mn.MarkupText(
                x.upper(),
                color=mn.WHITE,
                font=cls.FONT,
                font_size=cls.FONT_SIZE * 1.2,
                justify=True,
                weight=mn.BOLD,
            )
            for x in calendar.month_name
        ]
        group.WEEK_TEXTS = [
            mn.MarkupText(
                x[:2],
                color=mn.WHITE,
                font=cls.FONT,
                font_size=cls.FONT_SIZE * 0.8,
                justify=True,
                weight=mn.MEDIUM,
            )
            for x in calendar.day_abbr
        ]
        group.DAY_TEXTS = [
            mn.MarkupText(
                str(x),
                color=mn.DARKER_GRAY,
                font=cls.FONT,
                font_size=cls.FONT_SIZE,
                justify=True,
                weight=mn.MEDIUM,
            )
            for x in range(1, 32)
        ]
        return group

    def __init__(
        self, date: datetime.date = datetime.date.today(), height=6, width=8, **kwargs
    ):
        super().__init__()
        self.date = date
        calendar.setfirstweekday(6)
        self.calendar = calendar.monthcalendar(self.date.year, self.date.month)
        mw = width * 0.5
        mh = height * 0.5
        self.start = mn.ORIGIN + [-mw, mh, 0]
        self.header_height = height * self.HEADER_HEIGHT_RATIO
        self.content_height = height - self.header_height
        self.content_start = self.start + [0, -self.header_height, 0]
        self.header_row_h = self.header_height * 0.5
        self.rows = len(self.calendar)
        self.col_w = width / 7
        self.row_h = self.content_height / self.rows
        self._add_outline(width, height)
        self._add_grid(width, self.content_height)
        self._add_month_header()
        self._add_week_header()
        self._add_days()

    def _add_outline(self, width, height):
        self.outline = mn.Rectangle(mn.LIGHT_GRAY, height=height, width=width).set_fill(
            self.DAY_BG_COLORS[self.date.month - 1], 1
        )
        self.add(self.outline)

    def _add_grid(self, width, height):
        cols = [
            [
                self.content_start + [self.col_w * ii, 0, 0],
                self.content_start + [self.col_w * ii, -height, 0],
            ]
            for ii in range(1, 7)
        ]
        rows = [
            [
                self.content_start + [0, -self.row_h * ii, 0],
                self.content_start + [width, -self.row_h * ii, 0],
            ]
            for ii in range(0, self.rows)
        ]
        self.grid = mn.Polygram(*cols, *rows, color=mn.LIGHT_GRAY).set_z_index(1)
        self.add(self.grid)

    def _add_month_header(self):
        self.month_bg = (
            mn.Rectangle(None, self.header_row_h, self.width)
            .set_fill(self.MONTH_BG_COLORS[self.date.month - 1], 1)
            .set_stroke(None, 0, 0)
            .set_z_index(1)
            .move_to(self.start, mn.LEFT + mn.UP)
        )
        self.month_text = (
            self.MONTH_TEXTS[self.date.month]
            .copy()
            .set_z_index(2)
            .move_to(self.start * [0, 1, 0] + [0, -self.header_height * 0.25, 0])
        )
        self.month_header = mn.Group(self.month_bg, self.month_text)
        self.add(self.month_header)

    def _add_week_header(self):
        self.week_bg = (
            mn.Rectangle(None, self.header_row_h, self.width)
            .set_fill(self.WEEK_BG_COLORS[self.date.month - 1], 1)
            .set_stroke(None, 0, 0)
            .set_z_index(1)
            .move_to(self.start + [0, -self.header_row_h, 0], mn.LEFT + mn.UP)
        )
        self.week_text = mn.Group(
            *(
                self.WEEK_TEXTS[(ii + calendar.firstweekday()) % 7]
                .copy()
                .set_z_index(2)
                .move_to(self.start + [self.col_w * (ii + 0.5), 0, 0])
                for ii in range(7)
            )
        ).move_to(self.start * [0, 1, 0] + [0, -self.header_height * 0.75, 0])
        self.week_header = mn.Group(self.week_bg, self.week_text)
        self.add(self.week_header)

    def _add_days(self):
        self.days = mn.Group(
            *(
                self.DAY_TEXTS[day - 1]
                .copy()
                .set_z_index(2)
                .move_to(
                    self.content_start
                    + [self.col_w * (ii + 0.5), -self.row_h * (jj + 0.5), 0]
                )
                for jj, week in enumerate(self.calendar[:7])
                for ii, day in enumerate(week)
                if day > 0
            )
        )
        self.add(self.days)

    @mn.override_animation(mn.Create)
    def _override_create(self, run_time=2, **kwargs):
        return mn.LaggedStart(
            mn.DrawBorderThenFill(
                self.outline, rate_func=mn.rate_functions.ease_in_quad
            ),
            mn.LaggedStart(
                mn.DrawBorderThenFill(self.month_bg, run_time=0.5),
                mn.AnimationGroup(
                    mn.Write(self.month_text),
                    mn.DrawBorderThenFill(self.week_bg),
                    lag_ratio=0.2,
                    run_time=0.8,
                ),
                mn.AnimationGroup(
                    mn.LaggedStart(
                        *(mn.Create(x) for x in self.week_text),
                        lag_ratio=0.382,
                        run_time=0.7 * run_time,
                    ),
                    mn.Create(self.grid),
                    lag_ratio=0.2,
                ),
                lag_ratio=0.55,
            ),
            mn.LaggedStart(*(mn.FadeIn(x) for x in self.days)),
            lag_ratio=0.4,
            introducer=True,
            run_time=run_time,
            **kwargs,
        )

    @mn.override_animation(mn.Uncreate)
    def _override_uncreate(self, run_time=2, **kwargs):
        return mn.LaggedStart(
            mn.LaggedStart(*(mn.FadeOut(x) for x in self.days[::-1])),
            mn.LaggedStart(
                mn.AnimationGroup(
                    mn.LaggedStart(
                        *(mn.Uncreate(x) for x in self.week_text[::-1]),
                        lag_ratio=0.382,
                        run_time=0.7 * run_time,
                    ),
                    mn.Uncreate(self.grid),
                    lag_ratio=0.2,
                ),
                mn.AnimationGroup(
                    mn.Unwrite(self.month_text),
                    mn.FadeOut(self.week_bg),
                    lag_ratio=0.2,
                    run_time=0.8,
                ),
                mn.FadeOut(self.month_bg, run_time=0.5),
                lag_ratio=0.55,
            ),
            mn.Unwrite(self.outline, rate_func=mn.rate_functions.ease_in_quad),
            lag_ratio=0.4,
            introducer=False,
            remover=True,
            run_time=run_time,
            **kwargs,
        )
