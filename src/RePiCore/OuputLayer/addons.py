import re


class Style:
    def __init__(
        self,
        border_color: str = "#132238",
        hover_color: str = "#cefdfd",
        header_color: str = "#cefdfd",
        container_color: str = "#c6e9f0",
        background_color: str = "#ebf0f6",
    ) -> None:
        assert re.fullmatch(r"#[a-fA-F0-9]{6}", border_color)
        assert re.fullmatch(r"#[a-fA-F0-9]{6}", hover_color)
        assert re.fullmatch(r"#[a-fA-F0-9]{6}", header_color)
        assert re.fullmatch(r"#[a-fA-F0-9]{6}", container_color)
        assert re.fullmatch(r"#[a-fA-F0-9]{6}", background_color)

        self.render_template = "style.jinja2"
        self.border_color = border_color
        self.hover_color = hover_color
        self.header_color = header_color
        self.container_color = container_color
        self.background_color = background_color
