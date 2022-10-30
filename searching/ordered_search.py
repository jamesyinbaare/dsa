import math
from operator import index


def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return -1
    return -1


def jump_search(order_list, term):
    print("Entering jump search")
    list_size = len(order_list)
    block_size = int(math.sqrt(list_size))

    i = 0

    while i != len(order_list) -1 and order_list[i] <= term:
        print(f"block under consideration - {order_list[i:i+block_size]}")
        if i+block_size > len(order_list):
            block_size = len(order_list) - i
            block_list = order_list[i: i+block_list]
            j = search_ordered(block_list, term)

            if j == -1:
                print("Element not found")
                return
            return i + j
        if order_list[i + block_size - 1] == term:
            return i+ block_size -1
        elif order_list[i + block_size - 1] > term:
            block_array = order_list[i: i+block_size - 1]
            j = search_ordered(block_array, term)
            if j == -1:
                print("Element not found")
                return
            return i + j
        i +=block_size



print(jump_search([1,2,3,4,5,6,7,8,9, 10, 11], 8))

def binary_search_iterative(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1             
        if index_of_first_element > index_of_last_element:
            return None

list1 = [10, 30, 100, 120, 500]
search_term = 10
index_position1 = binary_search_iterative(list1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term,index_position1))

list2 = ['book','data','packt', 'structure']
search_term2 = 'structure'
index_position2 = binary_search_iterative(list2, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))