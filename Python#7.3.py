def is_in_list(numbers, n):
    return n in numbers


numbers = list(map(int, input("Enter numbers by space: ").split()))
n = int(input("Enter number n: "))


print(is_in_list(numbers, n))