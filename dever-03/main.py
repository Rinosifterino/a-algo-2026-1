def palindromo(array):
    for i in range(len(array)):
        if array[i] != array[-i-1]:
            return print("não é palindromo")
    return print("é palindromo")

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"] 

palindromo(array1)
palindromo(array2)
palindromo(array3)
palindromo(array4)