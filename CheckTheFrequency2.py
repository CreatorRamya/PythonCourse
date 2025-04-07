def check_value_frequency(input_dict, target_value):
    frequency = list(input_dict.values()).count(target_value)
    return frequency

test_dict = {
    'a': 100,
    'b': 200,
    'c': 100,
    'd': 300,
    'e': 100
}

try:
    target = int(input("Enter the value to check frequency: "))
    result = check_value_frequency(test_dict, target)
    print(f"The value {target} appears {result} time(s) in the dictionary.")
except ValueError:
    print("Please enter a valid integer.")