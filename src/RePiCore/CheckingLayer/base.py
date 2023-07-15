from typing import Literal, Any, List, Optional, Tuple
import re
from jinja2 import Environment, BaseLoader

from RePiCore.InputLayer.base import TableLike

from .addons import Pass, Fail, Neutral, Object
from .templates import PLAIN, WITHCHECK, TABLE, SCATTERPLOT, HISTOGRAM


class ReportElement:
    def __init__(self, render_template: Optional[str] = None) -> None:
        self.render_object: Optional[Object] = None
        self.render_template = render_template

    def render(self) -> str:
        assert self.render_object is not None
        assert self.render_template is not None
        template = Environment(loader=BaseLoader()).from_string(self.render_template)
        rv = template.render(object=self.render_object)
        return rv


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

    def render(self) -> str:
        self.check()
        self.render_object = Object(
            status=self.status,
            name=self.name,
            checked_value=self.checked_value,
            description=self.description,
        )
        rv = super().render()
        return rv


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

    def render(self) -> str:
        self.to_html()
        rv = super().render()
        return rv


class Graphical(ReportElement):
    def __init__(self, render_template: Optional[str] = None) -> None:
        super().__init__(render_template=render_template)
        self.id = id(self)

    def create_element(self) -> None:
        raise NotImplementedError(
            f"Method create_object not implemented in class {self.__class__}."
        )

    def render(self) -> str:
        self.create_element()
        rv = super().render()
        return rv


class Histogram(Graphical):
    def __init__(
        self,
        data: TableLike,
        series: List[str],
        colors: Optional[List[str]] = None,
    ):
        super().__init__(render_template=HISTOGRAM)
        assert isinstance(data, TableLike)
        assert isinstance(series, list)
        assert all([isinstance(s, str) for s in series])
        assert all([s in data.dataframe.columns for s in series])
        if colors is not None:
            assert isinstance(colors, list)
            assert len(colors) == len(series)
            assert all([isinstance(c, str) for c in colors])
            assert all(
                [
                    re.fullmatch(r"\(\d{1,3},\d{1,3},\d{1,3},\d(?:\.\d*)?\)", c)
                    for c in colors
                ]
            )
        self.data = data
        self.series = series
        self.colors = colors

    def create_element(self) -> None:
        self.render_object = Object(id=self.id, series=[])
        for i, ser in enumerate(self.series):
            _s_ = {"name": ser, "x": str(list(self.data.dataframe[ser]))}
            if self.colors is not None:
                _s_["color"] = self.colors[i]
            self.render_object.series.append(_s_)  # type: ignore [attr-defined]


class ScatterPlot(Graphical):
    def __init__(
        self,
        data: TableLike,
        series: List[Tuple[str, str]],
        colors: Optional[List[str]] = None,
    ):
        super().__init__(render_template=SCATTERPLOT)
        assert isinstance(data, TableLike)
        assert isinstance(series, list)
        assert all([isinstance(s, tuple) for s in series])
        for ser in series:
            assert len(ser) == 2
            assert all([isinstance(s, str) for s in ser])
        if colors is not None:
            assert isinstance(colors, list)
            assert all([isinstance(c, str) for c in colors])
            assert len(colors) == len(series)
            assert all(
                [
                    re.fullmatch(r"\(\d{1,3},\d{1,3},\d{1,3},\d(?:\.\d*)?\)", c)
                    for c in colors
                ]
            )
        self.data = data
        self.series = series
        self.colors = colors

    def create_element(self) -> None:
        self.render_object = Object(id=self.id, series=[])
        for i, ser in enumerate(self.series):
            _s_ = {
                "name": ser[1],
                "x": str(list(self.data.dataframe[ser[0]])),
                "y": str(list(self.data.dataframe[ser[1]])),
            }
            if self.colors is not None:
                _s_["color"] = self.colors[i]
            self.render_object.series.append(_s_)  # type: ignore [attr-defined]
