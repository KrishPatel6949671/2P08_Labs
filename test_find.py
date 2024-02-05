import my_array as ma
def test_find():
    matrix = [[4, 5, 6], [2, 1, 0]]
    
    print(matrix[0][1])

    array = ["1", "2", "2"]
    item = "2"
    result= ma.findIndex(array, item)
    print(result)
    assert result == array.index(item)

def test_find2():
    array = ["1", "2", "2"]
    item = "0"
    result= ma.findIndex(array, item)
    print(result)
    assert result == -1

test_find()
test_find2()