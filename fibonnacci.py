def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]

n = int(input("Введіть кількість чисел Фібоначчі для виведення: "))
fib_sequence = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {fib_sequence}")
