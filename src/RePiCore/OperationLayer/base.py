from typing import Dict, Callable, Any
import pandas as pd

from RePiCore.InputLayer.base import TableLike, SingleValues


class Operation:
    def __init__(self) -> None:
        raise NotImplementedError(
            f"Method __init__ not implemented in class {self.__class__}."
        )

    def execute(self) -> Any:
        raise NotImplementedError(
            f"Method execute not implemented in class {self.__class__}."
        )


class Filter(Operation):
    def __init__(
        self,
        data: TableLike,
        values: SingleValues,
        filters: Dict[str, Callable[[Any, SingleValues], bool]],
    ):
        assert isinstance(data, TableLike)
        assert isinstance(values, SingleValues)
        assert all([k in data.get_data().columns for k in filters.keys()])
        self.data = data
        self.values = values
        self.filters = filters

    def execute(self) -> TableLike:
        __filters__ = []
        source_df = self.data.get_data()
        for k, f in self.filters.items():
            vector = list(source_df[k].apply(lambda x: f(x, self.values)))
            __filters__.append(vector)
        _filters_ = pd.DataFrame({str(n): f for n, f in enumerate(__filters__)})
        filters = _filters_.apply(all, axis=1)
        return_df = source_df.loc[filters]
        return TableLike(return_df)


class ColumnCompareMatrix(Operation):
    def __init__(self, data: TableLike, column1: str, column2: str):
        assert isinstance(data, TableLike)
        assert isinstance(column1, str)
        assert column1 in data.dataframe.columns
        assert isinstance(column2, str)
        assert column2 in data.dataframe.columns
        self.data = data
        self.column1 = column1
        self.column2 = column2

    def execute(self) -> TableLike:
        unique1 = list(self.data.dataframe[self.column1].unique())
        unique2 = list(self.data.dataframe[self.column2].unique())
        unique = [*unique1, *unique2]
        rv_records: Dict[str, Dict[str, int]] = dict()
        for u1 in unique:
            rv_records[u1] = dict()
            for u2 in unique:
                count = self.data.dataframe.loc[
                    (self.data.dataframe[self.column1] == u1)
                    & (self.data.dataframe[self.column2] == u2)
                ].shape[0]
                rv_records[u1][u2] = count
        rv_df = pd.DataFrame(rv_records)
        rv = TableLike(rv_df)
        return rv


class Stack(Operation):
    pass


class Merge(Operation):
    pass


class CountOver(Operation):
    pass


class ColumnTransform(Operation):
    pass


class Size(Operation):
    pass
