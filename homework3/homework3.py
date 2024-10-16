#Реализовать функцию, которая будет запрашивать дату рождения
пользователя в формате день/месяц/год и выдавать его возраст в
зависимости от сегодняшнего дня. 


from datetime import datetime

def calculate_age():
    while True:
        birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
        try:
            birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
            break  
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат дд/мм/гггг.")

    today = datetime.now()
    age = today.year - birth_date.year


    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  

    print(f"Ваш возраст: {age} лет.")

calculate_age()
