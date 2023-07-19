from typing import List, Any, Union

from .base import Operation


class Line:
    def __init__(self, operations: List[Union[Operation, "Line"]]) -> None:
        assert isinstance(operations, list)
        assert all([isinstance(op, (Operation, Line)) for op in operations])
        self.__inputs__ = operations[0].__inputs__  # type: ignore [union-attr,has-type]
        self.__outputs__ = operations[-1].__outputs__  # type: ignore [union-attr,has-type]
        for i in range(len(operations) - 1):
            assert operations[i].__inputs__ == operations[i + 1].__inputs__  # type: ignore [union-attr]
            assert operations[i].__outputs__ == operations[i + 1].__outputs__  # type: ignore [union-attr]
        self.operations = operations

    def execute(self, *inputs: Any) -> Any:
        for i, v in zip(inputs, self.__inputs__):
            assert isinstance(i, v)

        _tmp_ = inputs
        for op in self.operations:
            _tmp_ = op.execute(*_tmp_)

        for t, v in zip(_tmp_, self.__outputs__):
            assert isinstance(t, v)

        return _tmp_
