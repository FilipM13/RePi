import pytest
from RePiCore.InputLayer.base import Source


def test_init():
    with pytest.raises(NotImplementedError):
        Source()
