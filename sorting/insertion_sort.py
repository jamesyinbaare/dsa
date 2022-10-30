def insertion_sort(unordered_list):
    for index in range(1, len(unordered_list)):
        search_index = index
        insert_value = unordered_list[index]
        while search_index > 0 and unordered_list[search_index-1] > insert_value:
            unordered_list[search_index] = unordered_list[search_index -1]
            search_index -=1
        unordered_list[search_index] = insert_value

my_list = [5, 1, 100, 2, 10]
print("Original list", my_list)
insertion_sort(my_list)
print("Sorted list", my_list)