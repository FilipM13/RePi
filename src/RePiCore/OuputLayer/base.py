from typing import List
from jinja2 import Environment, BaseLoader

from RePiCore.CheckingLayer.base import ReportElement

from .addons import DEFAULT_CSS, DEFAULT_JS, HEAD_INCLUDE
from .templates import DEFAULT_HTML


class Report:
    def __init__(self) -> None:
        raise NotImplementedError("__init__ not implemented.")

    def generate(self) -> None:
        raise NotImplementedError("generate not implemented.")


class HtmlFile(Report):
    def __init__(
        self,
        file_name: str,
        report_elements: List[ReportElement],
        css: str = DEFAULT_CSS,
        js: str = DEFAULT_JS,
        head_include: str = HEAD_INCLUDE,
    ) -> None:
        assert isinstance(file_name, str)
        assert file_name.endswith(".html")
        assert isinstance(css, str)
        assert isinstance(js, str)
        assert isinstance(head_include, str)
        assert isinstance(report_elements, list)
        assert all([isinstance(r, ReportElement) for r in report_elements])

        self.file_name = file_name
        self.render_template = DEFAULT_HTML
        self.css = css
        self.js = js
        self.head_include = head_include
        self.report_elements = report_elements

    def generate(self) -> None:
        html_elements = [re.render() for re in self.report_elements]
        template = Environment(loader=BaseLoader()).from_string(self.render_template)
        report_content = template.render(
            TITLE=self.file_name.removesuffix(".html"),
            CSS=self.css,
            JS=self.js,
            HEAD_INCLUDE=self.head_include,
            REPORT_ELEMENTS=html_elements,
        )
        with open(self.file_name, "w") as f:
            f.write(report_content)


class ExcelFile(Report):
    pass


class CsvFile(Report):
    pass


class JsonFile(Report):
    pass
