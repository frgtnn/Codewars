arr1 = [1, 2,3]
arr2 = [4, 5,6]

def array_plus_array(arr1,arr2):
    length = len(arr1)
    suma = 0
    for i in range(length):
        suma += arr1[i] + arr2[i]
    return suma
wynik = array_plus_array(arr1, arr2)
print(wynik)