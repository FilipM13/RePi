import pytest
from RePiCore.CheckingLayer.base import ReportElement


def test_init():
    with pytest.raises(NotImplementedError):
        ReportElement()
