from typing import Literal, Any, List, Optional
import re

from RePiCore.InputLayer.base import TableLike
from .addons import Pass, Fail, Neutral, Object


class ReportElement:
    def __init__(self) -> None:
        raise NotImplementedError(
            f"Method __init__ not implemented in class {self.__class__}."
        )


class WithCheck(ReportElement):
    def check(self) -> None:
        raise NotImplementedError(
            f"Method check not implemented in class {self.__class__}."
        )


class Plain(ReportElement):
    ALLOWED_TAGS = ["h3", "h2", "h1", "p"]

    def __init__(self, text: str, tag: Literal["h3", "h2", "h1", "p"]):
        assert isinstance(text, str)
        assert isinstance(tag, str)
        assert tag in self.ALLOWED_TAGS
        self.text = text
        self.tag = tag


class Equals(WithCheck):
    def __init__(
        self, name: str, checked_value: Any, expected_value: Any, description: str
    ):
        assert isinstance(name, str)
        assert isinstance(description, str)

        self.name = name
        self.checked_value = checked_value
        self.expected_value = expected_value
        self.description = description
        self.status = Neutral

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
        description: str,
        max_inclusive: bool = True,
        min_inclusive: bool = True,
    ):
        assert isinstance(name, str)
        assert isinstance(checked_value, (float, int))
        assert isinstance(max_value, (float, int))
        assert isinstance(min_value, (float, int))
        assert max_value > min_value
        assert isinstance(description, str)
        assert isinstance(max_inclusive, bool)
        assert isinstance(min_inclusive, bool)

        self.name = name
        self.checked_value = checked_value
        self.max_value = max_value
        self.min_value = min_value
        self.description = description
        self.max_inclusive = max_inclusive
        self.min_inclusive = min_inclusive
        self.status = Neutral

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
        assert isinstance(data, TableLike)
        assert isinstance(index, bool)
        self.data = data
        self.index = index

    def to_html(self) -> str:
        rv = self.data.dataframe.to_html(index=self.index)
        rv = re.sub(r"(style|border|class)=(.)+>", ">", rv)
        return rv


class Graphical(ReportElement):
    def __init__(self) -> None:
        self.id = id(self)
        self.report_object: Optional[Object] = None

    def create_object(self) -> None:
        raise NotImplementedError(
            f"Method create_object not implemented in class {self.__class__}."
        )


class Histogram(ReportElement):
    def __init__(
        self,
        data: TableLike,
        series: List[str],
        n_bins: int,
        colors: Optional[List[str]] = None,
    ):
        super().__init__()
        assert isinstance(data, TableLike)
        assert isinstance(series, list)
        assert all([isinstance(s, str) for s in series])
        assert all([s in data.dataframe.columns for s in series])
        assert isinstance(n_bins, int)
        assert n_bins > 0
        if colors is not NotInRange:
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
        self.n_bins = n_bins

    def create_object(self) -> None:
        pass


class ScatterPlot(ReportElement):
    def __init__(
        self, data: TableLike, series: List[str], colors: Optional[List[str]] = None
    ):
        super().__init__()
        assert isinstance(data, TableLike)
        assert isinstance(series, list)
        assert all([isinstance(s, tuple) for s in series])
        for ser in series:
            assert len(ser) == 2
            assert all([isinstance(s, str) for s in ser])
        assert all([s in data.dataframe.columns for s in series])
        if colors is not NotInRange:
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

    def create_object(self) -> None:
        pass
