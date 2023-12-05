def partition(my_list, first_index, last_index):
  pivot = my_list[first_index]
  left_pointer = first_index + 1
  right_pointer = last_index
 
  while True:
    # Iterate until the value pointed by left_pointer is greater than pivot or left_pointer is greater than last_index
    while my_list[left_pointer] < pivot and left_pointer < last_index:
      left_pointer += 1
    
    while my_list[right_pointer] > pivot and right_pointer >= first_index:
      right_pointer -= 1 
    if left_pointer >= right_pointer:
        break
    # Swap the values for the elements located at the left_pointer and right_pointer
    my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
   
  my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
  return right_pointer

def quicksort(my_list, first_index, last_index):
  if first_index < last_index:
    # Call the partition() function with the appropriate parameters
    partition_index = partition(my_list, first_index, last_index)
    # Call quicksort() on the elements to the left of the partition
    quicksort(my_list, first_index, partition_index)
    quicksort(my_list, partition_index + 1, last_index)
    
my_list = [6, 2, 9, 7] 
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)