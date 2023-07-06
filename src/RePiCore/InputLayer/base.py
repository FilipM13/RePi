from typing import Union, List, Dict, Literal, Optional, Any
import re
import pandas as pd

BaseClasses = Union[str, float, int, bool]


def unpack_nested(nested_list: Union[list, tuple, set]) -> List[BaseClasses]:
    _l2_ = []
    for li in nested_list:
        if isinstance(li, (list, tuple, set)):
            _l2_.extend(unpack_nested(li))
        else:
            _l2_.append(li)
    return _l2_


class Source:
    def __init__(self) -> None:
        """
        Do not use. Only overwrite.
        """
        raise NotImplementedError(
            f"Method __init__ not implemented in {self.__class__.__name__}"
        )

    def read(self) -> None:
        """
        Do not use. Only overwrite.
        """
        raise NotImplementedError(
            f"Method read not implemented in {self.__class__.__name__}"
        )


class SingleValues(Source):
    __base_classes__ = (str, float, int, bool)

    def __init__(self, **dictionary: Union[BaseClasses, List[BaseClasses]]) -> None:
        # validate attribute
        assert isinstance(dictionary, dict)
        for k, v in dictionary.items():
            assert isinstance(k, str)
            assert k != ""
            if isinstance(v, list):
                assert all([isinstance(i, self.__base_classes__) for i in v])
            else:
                assert isinstance(v, self.__base_classes__)

        # assign attribute
        self.dictionary = dictionary

    def read(self) -> None:
        for k, v in self.dictionary.items():
            self.__setattr__(k, v)
        self.__delattr__("dictionary")

    def get_values(self) -> Dict[str, Union[BaseClasses, List[BaseClasses]]]:
        attributes = self.__dict__
        return attributes


class TableLike(Source):
    def __init__(self, dataframe: pd.DataFrame = pd.DataFrame()):
        self.dataframe = dataframe

    def get_data(self) -> pd.DataFrame:
        return self.dataframe


class FromDataBase(TableLike):
    def __init__(
        self,
        db_engine: Literal["postgre", "mysql"],
        host: str,
        login: str,
        password: str,
        query: str,
    ):
        super().__init__()
        pass

    def read(self) -> None:
        pass


class FromFile(TableLike):
    def __init__(self, path: str):
        super().__init__()
        assert isinstance(path, str)
        assert path != ""
        self.path = path

    def read(self) -> None:
        super().read()


class FromCsv(FromFile):
    def __init__(
        self, path: str, delimiter: str, options: Optional[Dict[str, Any]] = None
    ):
        super().__init__(path)
        assert isinstance(delimiter, str)
        assert len(delimiter) == 1
        assert isinstance(options, dict) or (options is None)
        if isinstance(options, dict):
            assert all([isinstance(k, str) for k in options.keys()])
        self.delimiter = delimiter
        self.options = options

    def read(self) -> None:
        if self.options is not None:
            self.dataframe = pd.read_csv(  # type: ignore [assignment]
                filepath_or_buffer=self.path, sep=self.delimiter, **self.options
            )
        else:
            self.dataframe = pd.read_csv(
                filepath_or_buffer=self.path, sep=self.delimiter
            )


class FromExcel(FromFile):
    def __init__(self, path: str, sheet: Optional[str] = None):
        super().__init__(path)
        assert isinstance(sheet, str) or (sheet is None)
        self.sheet = sheet

    def read(self) -> None:
        if self.sheet is None:
            self.dataframe = pd.read_excel(self.path)
        else:
            self.dataframe = pd.read_excel(self.path, sheet_name=self.sheet)


class FromJson(FromFile):
    def __init__(self, path: str, per_line_regex: str, headers: List[str]):
        super().__init__(path)
        assert isinstance(per_line_regex, str)
        assert isinstance(headers, list)
        assert all([isinstance(h, str) for h in headers])
        self.per_line_regex = per_line_regex
        self.headers = headers

    def read(self) -> None:
        with open(self.path, "r") as file:
            lines = file.readlines()

        groups = [re.findall(self.per_line_regex, line) for line in lines]
        groups = [unpack_nested(g) for g in groups]
        assert all([len(g) <= len(self.headers) for g in groups])
        groups = [g + [None for _ in range(len(self.headers) - len(g))] for g in groups]
        self.dataframe = pd.DataFrame(data=groups, columns=self.headers)
