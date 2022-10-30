
def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        min_value = unsorted_list[index]
        min_index = index
        for j in range(index, len(unsorted_list)):
            if unsorted_list[j] < min_value:
                min_value = unsorted_list[j]
                min_index = j
        temp = unsorted_list[index]
        unsorted_list[index] = min_value
        unsorted_list[min_index] = temp


a_list = [3, 2, 35, 4, 32, 94, 5, 7]
print("List before sorting", a_list)
selection_sort(a_list)
print("List after sorting", a_list)