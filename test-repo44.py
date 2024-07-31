# Write a program to find the largest number in a given list.

def largest_number(numbers):

    biggest_num = numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num

    return biggest_num


print(largest_number([1, 4, 6, 7, 9876, 78999, 3, 4, 678, 234]))
print(largest_number([1, 5, 15, 20, 150, 30]))
