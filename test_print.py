import my_array as ma
def test_print(capfd):
    print("hello")
    array = ["1", "2", "2"]
    ma.printArray(array)
    out, err = capfd.readouterr()
    assert out == "1\n2\n2\n"

test_print()

