from typing import List, Any, Union

from .base import Operation


class Line:
    def __init__(self, operations: List[Union[Operation, "Line"]]) -> None:
        pass

    def execute(self) -> Any:
        pass
