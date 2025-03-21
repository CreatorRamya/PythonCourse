def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2025
        
        if birth_year > current_year:
            raise ValueError("Birth year cannot be in the future!")
        
        age = current_year - birth_year
        print(f"You are {age} years old.")
        
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

calculate_age()