from datetime import datetime

def calculate_age():
    while True:
        birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
        try:
            birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
            break  
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат дд/мм/гггг.")


