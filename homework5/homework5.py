#Определите функцию генератора get_number(), которая
возвращает нечетные числа из диапазона range(30). Используйте цикл for,
чтобы найти и вывести первое, пятое и последнее возращенной значение.

def get_number():
    for num in range(30):
        if num % 2 != 0: 
            yield num

def main():
    odd_numbers = list(get_number()) 

   
    if len(odd_numbers) < 5:
        print("Недостаточно нечетных чисел в диапазоне.")
        return

    print("Первое нечетное число:", odd_numbers[0])
    print("Пятое нечетное число:", odd_numbers[4])
    print("Последнее нечетное число:", odd_numbers[-1])


main()
