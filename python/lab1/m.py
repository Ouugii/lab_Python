#a
for number in range(1, 100, 2):
    if number % 5 != 0:
        print(number)



lekhongchiahetcho5 = (number for number in range(1, 100, 2) if number % 5 != 0)
for number in lekhongchiahetcho5:
    print(number)

#b
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence

n = int(input("Nhập số phần tử Fibonacci cần xuất: "))
fib_sequence = fibonacci_sequence(n)
for number in fib_sequence:
    print(number, end=" ")



def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Nhập số phần tử Fibonacci cần xuất: "))
fib_gen = fibonacci_generator()
for _ in range(n):
    print(next(fib_gen), end=" ")

#c
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_largest_prime(limit):
    largest_prime = None
    for num in range(limit, 1, -1):
        if is_prime(num):
            largest_prime = num
            break
    return largest_prime

limit = int(input("Nhập giới hạn: "))
largest_prime = find_largest_prime(limit)

if largest_prime is not None:
    print("Số nguyên tố lớn nhất nhỏ hơn hoặc bằng", limit, "là:", largest_prime)
else:
    print("Không có số nguyên tố nào nhỏ hơn hoặc bằng", limit)

# d
def fibonacci_smallest():
    a, b = 0, 1
    while a < 1:
        a, b = b, a + b
    return a

print("Số Fibonacci bé nhất là:", fibonacci_smallest())



# e
def TinhTBSoLe(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    if not odd_numbers:
        return 0
    
    odd_sum = sum(odd_numbers)
    odd_count = len(odd_numbers)
    odd_TB = odd_sum / odd_count
    
    return odd_TB

# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# Tính trung bình các số lẻ
TB = TinhTBSoLe(numbers)

print("Trung bình các số lẻ là:", TB)

# //////

def calculate_odd_average(numbers):
    odd_sum = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
            odd_count += 1
    
    if odd_count == 0:
        return 0
    
    odd_average = odd_sum / odd_count
    return odd_average

# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính trung bình các số lẻ
average = calculate_odd_average(numbers)

print("Trung bình các số lẻ là:", average)

# f
def calculate_odd_non_divisible_by_3_product(numbers):
    product = 1
    
    for num in numbers:
        if num % 2 != 0 and num % 3 != 0:
            product *= num
    
    return product

# Nhập mảng các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tích các phần tử là số lẻ không chia hết cho 3
product = calculate_odd_non_divisible_by_3_product(numbers)

print("Tích các phần tử là số lẻ không chia hết cho 3 là:", product)

# ////////

from functools import reduce

def alculate_odd_non_divisible_by_3_product(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0 and num % 3 != 0]
    
    if not odd_numbers:
        return 0
    
    product = reduce(lambda x, y: x * y, odd_numbers)
    return product

# Nhập mảng các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính tích các phần tử là số lẻ không chia hết cho 3
product = calculate_odd_non_divisible_by_3_product(numbers)

print("Tích các phần tử là số lẻ không chia hết cho 3 là:", product)

# g
def swap_elements(lst, pos1, pos2):
    if pos1 < 0 or pos1 >= len(lst) or pos2 < 0 or pos2 >= len(lst):
        return "Vị trí không hợp lệ"
    
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Vị trí cần đổi chỗ
position1 = 2
position2 = 5

# Đổi chỗ 2 phần tử
result = swap_elements(numbers, position1, position2)

print("Danh sách sau khi đổi chỗ:", result)

# /////////////

# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Vị trí cần đổi chỗ
position1 = 2
position2 = 5

# Kiểm tra vị trí hợp lệ
if 0 <= position1 < len(numbers) and 0 <= position2 < len(numbers):
    # Đổi chỗ 2 phần tử
    numbers[position1], numbers[position2] = numbers[position2], numbers[position1]
    print("Danh sách sau khi đổi chỗ:", numbers)
else:
    print("Vị trí không hợp lệ")


# h
# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Đảo ngược trật tự các phần tử
reversed_numbers = numbers[::-1]

print("Danh sách sau khi đảo ngược:", reversed_numbers)

# /////////
# Nhập danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Đảo ngược trật tự các phần tử
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

print("Danh sách sau khi đảo ngược:", reversed_numbers)

# i
def second_largest(numbers):
    if len(numbers) < 2:
        return "Không đủ số để tìm số lớn thứ nhì"
    
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1]
    return second_largest

# Nhập danh sách các số
numbers = [12, 45, 8, 21, 56, 32, 10, 78]

# Tìm và xuất các số lớn thứ nhì
second_largest_numbers = second_largest(numbers)

print("Các số lớn thứ nhì là:", second_largest_numbers)

# ///////
def scond_largest(numbers):
    if len(numbers) < 2:
        return "Không đủ số để tìm số lớn thứ nhì"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

# Nhập danh sách các số
numbers = [12, 45, 8, 21, 56, 32, 10, 78]

# Tìm và xuất các số lớn thứ nhì
second_largest_numbers = second_largest(numbers)

print("Các số lớn thứ nhì là:", second_largest_numbers)

# j
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def total_sum_of_digits(numbers):
    total = 0
    for num in numbers:
        total += sum_of_digits(num)
    return total

# Nhập danh sách các số
numbers = [123, 456, 789, 101]

# Tính tổng các chữ số của tất cả các số trong danh sách
total_sum = total_sum_of_digits(numbers)

print("Tổng các chữ số của tất cả các số:", total_sum)

# ////////

def otal_sum_of_digits(numbers):
    total = 0
    for num in numbers:
        while num > 0:
            total += num % 10
            num //= 10
    return total

# Nhập danh sách các số
numbers = [123, 456, 789, 101]

# Tính tổng các chữ số của tất cả các số trong danh sách
total_sum = total_sum_of_digits(numbers)

print("Tổng các chữ số của tất cả các số:", total_sum)

# k
def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7]

# Số cần đếm số lần xuất hiện
target_number = 2

# Đếm số lần xuất hiện của số trong danh sách
occurrences = count_occurrences(numbers, target_number)

print("Số lần xuất hiện của", target_number, "là:", occurrences)

# /////////
# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7]

# Số cần đếm số lần xuất hiện
target_number = 2

# Đếm số lần xuất hiện của số trong danh sách
occurrences = numbers.count(target_number)

print("Số lần xuất hiện của", target_number, "là:", occurrences)

# l
def numbers_with_n_occurrences(numbers, n):
    result = []
    for num in numbers:
        if numbers.count(num) == n and num not in result:
            result.append(num)
    return result

# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7, 8, 1, 7]

# Số lần xuất hiện cần kiểm tra
n = 2

# Tìm và xuất các số xuất hiện n lần trong danh sách
numbers_with_n_occurrences_list = numbers_with_n_occurrences(numbers, n)

print(f"Các số xuất hiện {n} lần trong danh sách:", numbers_with_n_occurrences_list)

# ////////

def number_with_n_occurrences(numbers, n):
    num_count = {}
    result = []

    for num in numbers:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == n:
            result.append(num)

    return result

# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7, 8, 1, 7]

# Số lần xuất hiện cần kiểm tra
n = 2

# Tìm và xuất các số xuất hiện n lần trong danh sách
numbers_with_n_occurrences_list = numbers_with_n_occurrences(numbers, n)

print(f"Các số xuất hiện {n} lần trong danh sách:", numbers_with_n_occurrences_list)

# m
def most_frequent_numbers(numbers):
    num_count = {}
    
    for num in numbers:
        num_count[num] = num_count.get(num, 0) + 1
    
    max_count = max(num_count.values())
    
    most_frequent = [num for num, count in num_count.items() if count == max_count]
    
    return most_frequent

# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7, 8, 1, 7]

# Tìm và xuất các số xuất hiện nhiều lần nhất trong danh sách
most_frequent_numbers_list = most_frequent_numbers(numbers)

print("Các số xuất hiện nhiều lần nhất trong danh sách:", most_frequent_numbers_list)

# ///////
from collections import Counter

def ost_frequent_numbers(numbers):
    num_count = Counter(numbers)
    max_count = max(num_count.values())
    
    most_frequent = [num for num, count in num_count.items() if count == max_count]
    
    return most_frequent

# Nhập danh sách các số
numbers = [2, 5, 2, 8, 2, 1, 5, 7, 8, 1, 7]

# Tìm và xuất các số xuất hiện nhiều lần nhất trong danh sách
most_frequent_numbers_list = most_frequent_numbers(numbers)

print("Các số xuất hiện nhiều lần nhất trong danh sách:", most_frequent_numbers_list)








   