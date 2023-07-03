from typing import Union, List, Dict, Literal

BaseClasses = Union[str, float, int, bool]


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

    def __init__(
        self, **dictionary: Dict[str, Union[BaseClasses, List[BaseClasses]]]
    ) -> None:
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

    def get_attributes(self) -> Dict[str, Union[BaseClasses, List[BaseClasses]]]:
        attributes = self.__dict__
        return attributes


class TableLike(Source):
    pass


class FromDataBase(TableLike):
    def __init__(
        self,
        db_engine: Literal["postgre", "mysql"],
        host: str,
        login: str,
        password: str,
        query: str,
    ):
        pass

    def read(self) -> None:
        pass


class FromFile(TableLike):
    def __init__(self, path: str):
        pass

    def read(self) -> None:
        super().read()


class FromJson(FromFile):
    def __init__(self, path: str, per_line_regex: str, headers: List[str]):
        super().__init__(path)

    def read(self) -> None:
        pass


class FromCsv(FromFile):
    def __init__(self, path: str, delimiter: str):
        super().__init__(path)

    def read(self) -> None:
        pass


class FromExcel(FromFile):
    def __init__(self, path: str, sheets: List[str]):
        super().__init__(path)

    def read(self) -> None:
        pass
