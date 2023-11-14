from typing import List, Optional
from jinja2 import Environment, FileSystemLoader
import pandas as pd
from bs4 import BeautifulSoup as bs

from RePiCore.CheckingLayer.base import ReportElement, Table
from RePiCore.utils.decorators import MarkIO
import RePiCore.templates as RePiTemplates

from .addons import Style
from .templates import DEFAULT_JS, HEAD_INCLUDE


class Report:
    def __init__(self) -> None:
        raise NotImplementedError("__init__ not implemented.")

    def generate(self) -> None:
        raise NotImplementedError("generate not implemented.")


MarkIO(
    inputs=[str, List[ReportElement], Optional[str], Optional[str], Optional[str]],
    outputs=[],
)


class HtmlFile(Report):
    def __init__(
        self,
        file_name: str,
        report_elements: List[ReportElement],
        css: Optional[Style] = Style(),
        js: Optional[str] = DEFAULT_JS,
        head_include: Optional[str] = HEAD_INCLUDE,
    ) -> None:
        assert isinstance(file_name, str)
        assert file_name.endswith(".html")
        assert isinstance(css, Style)
        assert isinstance(js, str)
        assert isinstance(head_include, str)
        assert isinstance(report_elements, list)
        assert all([isinstance(r, ReportElement) for r in report_elements])

        self.file_name = file_name
        self.render_template = "html.jinja2"
        self.css = css
        self.js = js
        self.head_include = head_include
        self.report_elements = report_elements

    def generate(self) -> None:
        # html_elements = [reel.render() for reel in self.report_elements]
        for reel in self.report_elements:
            reel.render()
        html_elements = self.report_elements
        print(html_elements)
        print(self.css)
        # template = Environment(loader=BaseLoader()).from_string(self.render_template)
        template = Environment(
            loader=FileSystemLoader(RePiTemplates.__file__.removesuffix("__init__.py"))
        ).get_template("html.jinja2")
        report_content = template.render(
            TITLE=self.file_name.removesuffix(".html"),
            CSS=self.css,
            JS=self.js,
            HEAD_INCLUDE=self.head_include,
            REPORT_ELEMENTS=html_elements,
        )
        report_content = bs(report_content, "html.parser").prettify()
        with open(self.file_name, "w") as f:
            f.write(report_content)


MarkIO(
    inputs=[str, List[Table], Optional[List[str]]],
    outputs=[],
)


class ExcelFile(Report):
    def __init__(
        self,
        file_name: str,
        tables: List[Table],
        sheet_names: Optional[List[str]] = None,
    ) -> None:
        assert isinstance(file_name, str)
        assert file_name.endswith(".xlsx")
        assert isinstance(tables, list)
        assert all([isinstance(tab, Table) for tab in tables])
        if sheet_names is not None:
            assert isinstance(sheet_names, list)
            assert all([isinstance(name, str) for name in sheet_names])
            assert len(tables) == len(sheet_names)

        self.file_name = file_name
        self.tables = tables
        self.sheet_names = sheet_names

    def generate(self) -> None:
        writer = pd.ExcelWriter(self.file_name, engine="xlsxwriter")
        for i, table in enumerate(self.tables):
            sheet_name = (
                self.sheet_names[i] if self.sheet_names is not None else f"sheet{i}"
            )
            table.data.to_excel(writer, sheet_name=sheet_name)
        writer.close()


MarkIO(
    inputs=[str, Table],
    outputs=[],
)


class CsvFile(Report):
    def __init__(
        self,
        file_name: str,
        table: Table,
    ) -> None:
        assert isinstance(file_name, str)
        assert file_name.endswith(".csv")
        assert isinstance(table, Table)

        self.file_name = file_name
        self.table = table

    def generate(self) -> None:
        self.table.data.to_csv(self.file_name)


MarkIO(
    inputs=[str, Table],
    outputs=[],
)


class JsonFile(Report):
    def __init__(
        self,
        file_name: str,
        table: Table,
    ) -> None:
        assert isinstance(file_name, str)
        assert file_name.endswith(".json")
        assert isinstance(table, Table)

        self.file_name = file_name
        self.table = table

    def generate(self) -> None:
        self.table.data.to_json(self.file_name)
