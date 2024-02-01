import my_array as ma

def test_insert():
    array = ["1", "2", "2"]
    item = "5"
    index = 0
    result = ma.addItem(array, index, item)
    print(result)
    array.insert(index, item)
    assert result == array

def test_insert2():
    array = ["1", "2", "2"]
    item = "5"
    index = 3
    result = ma.addItem(array, index, item)
    print(result)
    array.insert(index, item)
    assert result == array

test_insert()
test_insert2()