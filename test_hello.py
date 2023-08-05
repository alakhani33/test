from hello import more_hello


def test_more_hello():
    assert "hi" == more_hello()


# just to create an error
# def test_more_hello2():
#    assert "no_hi" == more_hello()
