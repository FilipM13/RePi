from typing import Dict, Any
import re


class Object:
    def __init__(self, **kwargs: Dict[str, Any]):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class Status:
    def __init__(self, name: str, code: int, rgba_color: str, description: str):
        assert isinstance(name, str)
        assert isinstance(code, int)
        assert isinstance(rgba_color, str)
        rgba_color = re.sub(r"\s", "", rgba_color)
        assert re.fullmatch(
            r"\(\d{1,3},\d{1,3},\d{1,3},\d(?:\.\d*)?\)", rgba_color
        ), f"The rgba_color must match pattern (ddd,ddd,ddd,d.d) where d is digit, instead got {rgba_color}."
        assert isinstance(description, str)

        self.name = name
        self.code = code
        self.rgba_color = rgba_color
        self.description = description


Fail = Status("FAIL", -1, "(255, 0, 0, 1)", "Check failed.")
Neutral = Status("NEUTRAL", 0, "(0, 0, 255, 1)", "Check with status neutral.")
Pass = Status("PASS", -1, "(0, 255, 0, 1)", "Check passed.")
