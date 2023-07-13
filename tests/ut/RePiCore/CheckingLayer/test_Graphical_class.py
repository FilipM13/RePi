import pytest
from RePiCore.CheckingLayer.base import Graphical


def test_init():
    Graphical()


def test_create_element():
    o = Graphical()
    with pytest.raises(NotImplementedError):
        o.create_element()
