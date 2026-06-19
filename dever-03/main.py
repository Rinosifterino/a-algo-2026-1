def palindromo(array):
    for i in range(len(array)):
        if array[i] != array[-i-1]:
            return print("não é palindromo")
    return print("é palindromo")

array1 = [0, 1, 2, 3, 2, 3, 6]
array2 = ["m","a","r","r","a","m"]

palindromo(array1)
palindromo(array2)