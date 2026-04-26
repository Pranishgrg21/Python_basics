"""Question 1> Loop through a list of numbers and print their squares."""

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    square = num * num
    print(square)


"""Question 2> Calculate the total bill from a list of prices using a for loops"""

prices = [100, 200, 300, 400, 500]
total = 0

for price in prices:
    total = total + price
print("Total bill:",total)


"""Question 3> Store student marks in a dictionary and print the average mark."""

marks= {"Ram": 85,"Sita": 95, "Hari": 90}
total = 0

for mark in marks.values():
    total = total + mark
average = total / len(marks)
print("Average marks:", average)

"""Question 4> Count the number of even numbers in a list using a for loop."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for num in numbers:
    if num % 2 == 0:
        count = count + 1
print("Number of even numbers:", count)


"""Question 5> Apply a 10 percent discount to each product price in a list"""

prices = [100, 200, 300, 400, 500]

for price in prices:
    dicsounted = price * 0.9
    print("Discounted price:", dicsounted)


""" Total Price ma discount lagau na paryo vanay yesari 
    prices = [100, 200, 300, 400, 500]

    total = sum(prices)
    discounted_price = total * 0.9

    print("Total price:", total)
    print("Discounted total:", discounted_total)

    ani for loop method ma chai yesari 

    prices = [100, 200, 300, 400, 500]

    total = 0

    for price in prices:
        total = total + price
    
    disocunted_price = total * 0.9

    print("Total Price:", total)
    print("Discounted price:", discounted price)
"""

"""Question 6> Use a while loop to print numbers from 10 down to 1."""

numbers = 10

while numbers > 0:
    print(numbers)
    numbers = numbers - 1

"""Question 7> Merge two lists into one new list using a for loop"""

List1 = [1, 2, 3]
list2 = [4, 5, 6]

result = []

for item in List1:
    result.append(item)
for item in list2:
    result.append(item)

print(result)

"""Question 8> Find the maximum number in a list without using the max function"""
numbers = [24, 45, 98, 27, 92]

max_num = numbers[0]

for num in numbers:
    max_num = num > max_num
    max_num = num
print("Maximum number:", max_num)


"""Question 9> Create a dictionary from two separate lists (key and values)"""

keys = ["Name", "age", "city"]
values = ["Ram", "24", "Pokhara"]

students = {}

for i in range(len(keys)):
    students[keys[i]] = values[i]
print(students)

"""
    keys = ["Name", "age", "city"]
    values = ["Ram", "24", "Pokhara"]

    students = dict(zip(keys, values))

    print(students)
"""

"""Question 10> Remove dulpicates from a list using a loop and a dictionary"""

""" Code Flow
List -> set ma convert
set le duplicates automatically hataucha
feri list ma convert garcha

items = [1, 2, 2, 3, 4, 4, 5]

unique_items = list(set(items))
print(unique_items)

"""


"""Code Flow
list bata chai ek ek element lincha 
check garcha (already cha ki chaina) chaina vanay add gardincha
cha vane skip garcha


items = [1, 2, 2, 3, 4, 4, 5]

uniques_numbers = []

for num in items:
    if num not in uniques_numbers:
        uniques_numbers.append(num)

print(uniques_numbers)

"""

"""
List -> dict banaucha (keys = numbers)
dict ma duplicate key hudaina -> remove garcha
keys lai list ma convert garcha

items = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(dict.fromkeys(items))

print(unique_numbers)

"""

items = [1, 2, 2, 3, 4, 4, 5]
result = []

for item in items:
    if item not in result:
        result.append(item)
print(result)


"""Question 11> Print the multiplication table for a given number using a for loop"""

num = int(input("Enter the number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

"""Question 12> Calculate the factorial of a number using a while loop"""

num = int(input("Enter the number: "))
original_num = num

factorial = 1

while num > 1:
    factorial = factorial * num
    num = num - 1
# print("Factorial:", factorial)
print(f"Factorial {original_num}: {factorial}")

"""Question 13> Check if a list is a palindrome using a for loop"""

list = [1, 2, 3, 2, 1]

is_palindrome = True

for i in range(len(list) // 2):
    if list[i] != list[len(list) -1 -i]:
        is_palindrome = False
        break
print("Is Palindrome:", is_palindrome) 

"""Question 14> Sort a list of numbers in ascending order using bubble sort with loops"""
numbers = [64, 34, 25, 12, 22, 11, 90, 75, 80]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j+1]:
           numbers[j], numbers[j + 1] = numbers[j+1], numbers[j]
print("Sorted list:", numbers)

"""Question 15> Count occurances of each character in a string using a dictionary"""

text = "Pranish"
count = {}
for char in text:
    if char in count:
        count[char] = char + 1
    else:
        count[char] = 1
print(count)

"""Question 16> Update values in a dictionary based on a condition using for loop."""

marks = {"Pranish": 70, "Gurung": 45, "Rai": 40}
for student, mark in marks.items():
    if mark < 50:
        marks[student] = mark + 5
print(marks)

"""Question 17> Use nested for loops to print a right-angled triangle pattern of stars."""

rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

    """
        rows = 5
        for i in range(rows, 0, -1):
            for j in range(i):
                print("*", end="")
            print()
    """

"""Question 18> Convert a list of tuples into a dictionary using a for loop"""

tuples = [("name", "Ram"), ("age", 20), ("city", "Pokhara")]
result = {}
for key, value in tuples:
    result[key] = value
print(result)

"""Question 19> Find common elements between two lists using a for loop"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
common = []
for item in list_1:
    if item in list2:
        common.append(item)
print(common)


"""Question 20> Count the total number of vowesl in a list of strings using a for loop"""

words = ["Apple", "Banana", "Cherry"]
vowels = "aeiouAEIOU"
total = 0
for word in words:
    for char in word:
        if char in vowels:
            total = total + 1
print("Total vowels:", total)
