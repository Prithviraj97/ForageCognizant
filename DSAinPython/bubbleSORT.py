my_list = [12,3,1,11,5]
# def bubble_sort(num_list):

#     list_len = len(num_list)
#     for i in range(list_len-1):
#         for j in range(list_len-1-i):
#             if (num_list[j] > num_list[j+1]) :
#                 num_list[j] = num_list[j+1]
#                 num_list[j+1] = num_list[j]
#     return num_list

def bubble_sort(my_list):
  list_length = len(my_list)
  # Correct the mistake
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    #Loop through all elements until the last one --becasue at this point the list is already sorted.
    for i in range(list_length-1):
      # Correct the mistake
      if my_list[i] > my_list[i+1]:
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    # Correct the mistake
    list_length -= 1
  return my_list

print(bubble_sort([4,3,7,1,5]))
print(bubble_sort(my_list))