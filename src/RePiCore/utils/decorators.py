from typing import List


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

    def __init__(self, inputs: List[type], outputs: List[type]) -> None:
        self.__inputs__ = inputs
        self.__outputs__ = outputs

    def __call__(self, cls: type) -> type:
        cls.__setattr__("__inputs__", self.__inputs__)
        cls.__setattr__("__outputs__", self.__outputs__)
        return cls
