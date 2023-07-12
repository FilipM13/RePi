from typing import Dict, Callable, Any, Literal, List
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
        rv_records: Dict[str, Dict[str, int]] = dict()
        for u1 in unique1:
            rv_records[u1] = dict()
            for u2 in unique2:
                count = self.data.dataframe.loc[
                    (self.data.dataframe[self.column1] == u1)
                    & (self.data.dataframe[self.column2] == u2)
                ].shape[0]
                rv_records[u1][u2] = count
        rv_df = pd.DataFrame(rv_records)
        rv = TableLike(rv_df)
        return rv


class Stack(Operation):

    def __init__(self, data: List[TableLike]):
        assert all([isinstance(d, TableLike) for d in data])
        self.data = data

    def execute(self) -> TableLike:
        rv_df = pd.concat([*[d.dataframe for d in self.data]], ignore_index=True, axis=0)
        rv = TableLike(rv_df)
        return rv


class Merge(Operation):

    def __init__(self, data1: TableLike, data2: TableLike, on: str, how: Literal["inner", "outer", "left", "right", "cross"]):
        assert isinstance(data1, TableLike)
        assert isinstance(data2, TableLike)
        assert isinstance(on, str)
        assert how in ['inner', 'outer', 'left', 'right', 'cross']
        if how == 'cross':
            on = None
        self.data1 = data1
        self.data2 = data2
        self.on = on
        self.how = how

    def execute(self) -> TableLike:
        rv_df = self.data1.dataframe.merge(self.data2.dataframe, how=self.how, on=self.on)
        rv = TableLike(rv_df)
        return rv


class CountOver(Operation):
    pass


class ColumnTransform(Operation):
    pass


class Size(Operation):
    pass
