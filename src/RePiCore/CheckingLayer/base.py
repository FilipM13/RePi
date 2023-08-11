from typing import Literal, Any, List, Optional
import re

from RePiCore.InputLayer.base import TableLike

from .addons import Pass, Fail, Neutral, Object

PLAIN = "plain.jinja2"
WITHCHECK = "withcheck.jinja2"
TABLE = "table.jinja2"
SCATTERPLOT = "scatterplot.jinja2"
HISTOGRAM = "histogram.jinja2"


class ReportElement:
    def __init__(self, render_template: Optional[str] = None) -> None:
        self.render_object: Optional[Object] = None
        self.render_template = render_template

    def render(self) -> None:
        assert self.render_object is not None
        assert self.render_template is not None


class Plain(ReportElement):
    ALLOWED_TAGS = ["h3", "h2", "h1", "p"]

    def __init__(self, text: str, tag: Literal["h3", "h2", "h1", "p"]):
        super().__init__(PLAIN)
        assert isinstance(text, str)
        assert isinstance(tag, str)
        assert tag in self.ALLOWED_TAGS
        self.text = text
        self.tag = tag
        self.render_object = Object(tag=self.tag, text=self.text)


class WithCheck(ReportElement):
    def __init__(self, name: str, description: Optional[str], checked_value: Any):
        super().__init__(WITHCHECK)
        assert isinstance(name, str)
        assert name != ""
        assert isinstance(description, str) or (description is None)

        self.checked_value = checked_value
        self.name = name
        self.description = description
        self.status = Neutral

    def check(self) -> None:
        raise NotImplementedError(
            f"Method check not implemented in class {self.__class__}."
        )

    def render(self) -> None:
        self.check()
        self.render_object = Object(
            status=self.status,
            name=self.name,
            checked_value=self.checked_value,
            description=self.description,
        )
        super().render()


class Equals(WithCheck):
    def __init__(
        self, name: str, checked_value: Any, expected_value: Any, description: str
    ):
        super().__init__(
            name=name, description=description, checked_value=checked_value
        )

        self.expected_value = expected_value

    def check(self) -> None:
        if self.checked_value == self.expected_value:
            self.status = Pass
        else:
            self.status = Fail


class InRange(WithCheck):
    def __init__(
        self,
        name: str,
        checked_value: float,
        max_value: float,
        min_value: float,
        description: Optional[str] = None,
        max_inclusive: bool = True,
        min_inclusive: bool = True,
    ):
        assert isinstance(checked_value, (float, int))
        super().__init__(
            name=name, description=description, checked_value=checked_value
        )
        assert isinstance(max_value, (float, int))
        assert isinstance(min_value, (float, int))
        assert max_value > min_value
        assert isinstance(max_inclusive, bool)
        assert isinstance(min_inclusive, bool)

        self.max_value = max_value
        self.min_value = min_value
        self.max_inclusive = max_inclusive
        self.min_inclusive = min_inclusive

        if self.description is None:
            lower = "<" if self.min_inclusive else "("
            upper = ">" if self.max_inclusive else ")"
            self.description = (
                f"Check if in range {lower}{self.min_value}, {self.max_value}{upper}."
            )

    def check(self) -> None:
        mx = None
        mn = None

        if self.max_inclusive:
            mx = self.checked_value <= self.max_value
        else:
            mx = self.checked_value < self.max_value

        if self.min_inclusive:
            mn = self.checked_value >= self.min_value
        else:
            mn = self.checked_value > self.min_value

        if mx and mn:
            self.status = Pass
        else:
            self.status = Fail


class NotInRange(InRange):
    def __init__(
        self,
        name: str,
        checked_value: float,
        max_value: float,
        min_value: float,
        description: str,
        max_inclusive: bool = True,
        min_inclusive: bool = True,
    ):
        super().__init__(
            name,
            checked_value,
            max_value,
            min_value,
            description,
            max_inclusive,
            min_inclusive,
        )

    def check(self) -> None:
        super().check()
        if self.status is Fail:
            self.status = Pass
        if self.status is Pass:
            self.status = Fail


class Table(ReportElement):
    def __init__(self, data: TableLike, index: bool = True):
        super().__init__(render_template=TABLE)
        assert isinstance(data, TableLike)
        assert isinstance(index, bool)
        self.data = data
        self.index = index

    def to_html(self) -> None:
        rv = self.data.dataframe.to_html(index=self.index)
        self.render_object = Object(html=re.sub(r"(style|border|class)=(.)+>", ">", rv))

    def render(self) -> None:
        self.to_html()
        super().render()


class Series(ReportElement):
    pass


class Bar(Series):
    render_template = "bar.jinja2"

    def __init__(self, x: List[Any], y: List[Any], name: str, color: Optional[str]):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.type = "bar"

    def render(self) -> None:
        self.render_object = Object(
            x=self.x, y=self.y, name=self.name, color=self.color, type=self.type
        )


class Histogram(Series):
    render_template = "histogram.jinja2"

    def __init__(self, x: List[Any], name: str, color: Optional[str]):
        self.x = x
        self.name = name
        self.color = color
        self.type = "histogram"

    def render(self) -> None:
        self.render_object = Object(
            x=self.x, name=self.name, color=self.color, type=self.type
        )


class Scatter(Series):
    render_template = "scatter.jinja2"

    def __init__(
        self,
        x: List[Any],
        y: List[Any],
        name: str,
        mode: Literal["markers", "lines", "markers+lines"],
        color: Optional[str],
    ):
        self.x = x
        self.y = y
        self.name = name
        self.mode = mode
        self.color = color
        self.type = "markers"

    def render(self) -> None:
        self.render_object = Object(
            x=self.x,
            y=self.y,
            name=self.name,
            mode=self.mode,
            color=self.color,
            type=self.type,
        )


class Layout(ReportElement):
    render_template = "layout.jinja2"
    pass


class Graph(ReportElement):
    render_template = "graph.jinja2"

    def __init__(self, name: str, series: List[Series], layout: Layout = Layout()):
        self.series = series
        self.layout = layout
        self.name = name
        self.id = id(self)

    def render(self) -> None:
        for ser in self.series:
            ser.render()
        self.render_object = Object(
            series=self.series, layout=self.layout, name=self.name, id=self.id
        )
