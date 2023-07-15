import pytest

from RePiCore.OuputLayer.base import Report


def test_init():
    with pytest.raises(NotImplementedError):
        Report()
