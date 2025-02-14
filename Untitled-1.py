def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введите число: "))
print(f"Факториал {number} равен {factorial(number)}")
