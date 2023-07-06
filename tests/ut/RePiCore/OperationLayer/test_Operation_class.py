import pytest
from RePiCore.OperationLayer.base import Operation


def test_init():
    with pytest.raises(NotImplementedError):
        Operation()
