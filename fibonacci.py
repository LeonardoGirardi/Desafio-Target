def fibonacci(num) -> str:
    a, b = 0, 1

    while a <= num:
        if a == num:
            return f"Resultado: {num} pertence a sequencia de Fibonacci"  
        a = a + b
        b = a - b

    return f"Resultado: {num} não pertence a sequencia de Fibonacci"

num = 145
print(fibonacci(num))





      