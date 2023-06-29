from typing import Union, List, Dict

BaseClasses = Union[str, float, int, bool]

class Source:

    def __init__(self) -> None:
        """
        Do not use. Only overwrite.
        """
        raise NotImplementedError(f'Method __init__ not implemented in {self.__class__.__name__}')

    def read(self) -> None:
        """
        Do not use. Only overwrite.
        """
        raise NotImplementedError(f'Method read not implemented in {self.__class__.__name__}')


class SingleValues(Source):
    __base_classes__ = (str, float, int, bool)

    def __init__(
        self,
        **dictionary
    ) -> None:
        # validate attribute
        assert isinstance(dictionary, dict)
        for k, v in dictionary.items():
            assert isinstance(k, str)
            assert k != ''
            if isinstance(v, list):
                assert all([isinstance(i, self.__base_classes__) for i in v])
            else:
                assert isinstance(v, self.__base_classes__)

        # assign attribute
        self.dictionary = dictionary

    def read(self):
        for k, v in self.dictionary.items():
            self.__setattr__(k, v)
        self.__delattr__('dictionary')

    def get_attributes(self) -> Dict[str, Union[BaseClasses, List[BaseClasses]]]:
        attributes = self.__dict__
        return attributes


class TableLike(Source):
    pass
