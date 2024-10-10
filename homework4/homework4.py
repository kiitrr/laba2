import random

def find_multiples(): 
    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    while True:
        try:
            x = int(input("Введите цифру X (от 1 до 9) для поиска кратных чисел: "))
            if x < 1 or x > 9:
                raise ValueError("Цифра должна быть от 1 до 9.")
