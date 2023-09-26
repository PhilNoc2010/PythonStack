def countdown(count_start):
    for i in range(count_start, -1, -1):
        print(i)

countdown(5)
countdown(8)

def print_and_return(print_val, return_val):
    print(print_val)
    return return_val

print(print_and_return(4, 8))
print(print_and_return(8, 4))

def first_plus_length (list):
    total = list[0]
    total = total + len(list)
    return total

print(first_plus_length([1,2,3,4,5]))
print(first_plus_length([2,4,6,8,10]))

def values_greater_than_second(list):
    if (len(list) < 3):
        return False
    new_list = []
    for i in range(2,len(list)):
        if (list[i] > list[1]):
            new_list.append(list[i])
    return new_list

print(values_greater_than_second([2,4]))
print(values_greater_than_second([1,3,5,1,8]))

def length_and_value(length, value):
    output = []
    for i in range(0, length):
        output.append(value)
        # output[i] = value  >>> Is this possible in Python?
    return output

print(length_and_value(4, 7))
print(length_and_value(6, 2))

