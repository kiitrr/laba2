# Написать игру «камень-ножницы-бумага»
import rando

def get_user_choice():
    while True:
        user_input = input("Выберите: камень, ножницы или бумага: ").lower()
        if user_input in ['камень', 'ножницы', 'бумага']:
            return user_input
        else:
            print("Неверный ввод. Пожалуйста, выберите камень, ножницы или бумагу.")

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == 'камень' and computer == 'ножницы') or \
         (user == 'ножницы' and computer == 'бумага') or \
         (user == 'бумага' and computer == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Ваш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
