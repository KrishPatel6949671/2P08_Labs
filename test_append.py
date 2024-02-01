import my_array as ma
def test_append():
    array = ["1", "2", "2"]
    item = "0"
    result= ma.addItemAtEnd(array, item)
    print(result)
    array.append(item)
    assert result == array

test_append()