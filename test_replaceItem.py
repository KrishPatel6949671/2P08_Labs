import my_array as ma
def test_count():
    array1 = ["1", "2", "2"]
    array2 = ["0", "2", "2"]
    result = ma.replaceItem(array1, 0, "0")
    print(result)
    assert result == array2

def test_count2():
    array1 = ["1", "2", "2"]
    array2 = ["1", "2", "0"]
    result = ma.replaceItem(array1, 2, "0")
    print(result)
    assert result == array2

def test_count3():
    array1 = ["1", "2", "2"]
    array2 = ["1", "2", "0"]
    result = ma.replaceItem(array1, 4, "0")
    print(result)
    assert result == -1

test_count()
test_count2()
test_count3()
