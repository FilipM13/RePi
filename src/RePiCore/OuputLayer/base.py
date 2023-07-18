from typing import List, Optional
from jinja2 import Environment, BaseLoader
import pandas as pd
from bs4 import BeautifulSoup as bs

from RePiCore.CheckingLayer.base import ReportElement, Table
from RePiCore.utils.decorators import MarkIO

from .addons import DEFAULT_CSS, DEFAULT_JS, HEAD_INCLUDE
from .templates import DEFAULT_HTML


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
        css: Optional[str] = DEFAULT_CSS,
        js: Optional[str] = DEFAULT_JS,
        head_include: Optional[str] = HEAD_INCLUDE,
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
        html_elements = [reel.render() for reel in self.report_elements]
        template = Environment(loader=BaseLoader()).from_string(self.render_template)
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
            table.data.dataframe.to_excel(writer, sheet_name=sheet_name)
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
        self.table.data.dataframe.to_csv(self.file_name)


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
        self.table.data.dataframe.to_json(self.file_name)
