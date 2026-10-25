def get_even_odd_numbers(n):
    even_numbers = []
    odd_numbers = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return even_numbers, odd_numbers

evens, odds = get_even_odd_numbers(10)
print("Even numbers:", evens)   # 输出: [2, 4, 6, 8, 10]
print("Odd numbers:", odds)     # 输出: [1, 3, 5, 7, 9]
