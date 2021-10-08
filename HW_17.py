def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    # если элемент меньше заданного и следующий больше или равен заданному
    if array[middle] < element and array[middle+1]>=element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array


list_non_sort = list(input("Введите последовательность чисел через пробел: ").split())
num = input("Введите любое число: ")
list_sort = sort(list_non_sort)
print("Отсортированный список: ",list_sort)
ind = binary_search(list_sort,num,0,len(list_sort))
if ind==False:
    print("В списке нет числа, отвечающего заданным условиям.")
else:
    print("Индекс числа, отвечающего заданным условиям: ",ind)