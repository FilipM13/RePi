import re
from jinja2 import Environment, BaseLoader

from .templates import DEFAULT_CSS


class Style:
    def __init__(
        self,
        border_color: str = "#132238",
        hover_color: str = "#cefdfd",
        header_color: str = "#cefdfd",
        container_color: str = "#c6e9f0",
        background_color: str = "#ebf0f6",
    ) -> None:
        assert re.fullmatch(r"#[a-zA-Z0-9]{6}", border_color)
        assert re.fullmatch(r"#[a-zA-Z0-9]{6}", hover_color)
        assert re.fullmatch(r"#[a-zA-Z0-9]{6}", header_color)
        assert re.fullmatch(r"#[a-zA-Z0-9]{6}", container_color)
        assert re.fullmatch(r"#[a-zA-Z0-9]{6}", background_color)

        self.render_template = DEFAULT_CSS
        self.border_color = border_color
        self.hover_color = hover_color
        self.header_color = header_color
        self.container_color = container_color
        self.background_color = background_color

    def render(self) -> str:
        template = Environment(loader=BaseLoader()).from_string(self.render_template)
        style = template.render(
            border_color=self.border_color,
            hover_color=self.hover_color,
            header_color=self.header_color,
            container_color=self.container_color,
            background_color=self.background_color,
        )
        return style
