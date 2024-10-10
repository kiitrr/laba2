def get_number():
    for num in range(30):
        if num % 2 != 0:  
            yield num

def main():
    odd_numbers = list(get_number()) 

    
