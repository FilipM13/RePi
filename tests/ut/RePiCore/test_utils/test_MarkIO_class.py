from RePiCore.utils.decorators import MarkIO

def test_work():

    @MarkIO(
        inputs=[str, str, int],
        outputs=[str, str, float]
    )
    class Test:
        pass

    assert '__inputs__' in Test.__dict__.keys()
    assert '__outputs__' in Test.__dict__.keys()

    t = Test()

    assert t.__inputs__ == [str, str, int]
    assert t.__outputs__ == [str, str, float]
