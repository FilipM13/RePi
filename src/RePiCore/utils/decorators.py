from typing import List, Type


class MarkIO(object):
    """
    Usage:
    >>>@MarkIO(inputs=[str], outputs=[int])
    >>>class Test:
    >>>    pass

    Results:
    >>>print(Test.__inputs__)
    [str]
    >>>print(Test.__outputs__)
    [int]
    >>>print(Test.__dict__)
    {... '__inputs__': [<class 'str'>], '__outputs__': [<class 'int'>]}
    """

    def __init__(self, inputs: List[object], outputs: List[object]) -> None:
        self.__inputs__ = inputs
        self.__outputs__ = outputs

    def __call__(self, cls: Type) -> Type:
        cls.__inputs__ = self.__inputs__
        cls.__outputs__ = self.__outputs__
        return cls
