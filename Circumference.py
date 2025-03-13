import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative. Please enter a valid value.")
        else:
            circumference = calculate_circumference(radius)
            print(f"The circumference of the circle is: {circumference:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
