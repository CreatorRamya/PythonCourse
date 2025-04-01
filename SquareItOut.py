def filter_squares(start, end):
    """Prints squares of numbers and separates even and odd ones."""
    for num in range(start, end + 1):
        square = num ** 2
        print(f"{num}^2 = {square} ({'Even' if square % 2 == 0 else 'Odd'})")

start_range = int(input("Start: "))
end_range = int(input("End: "))
filter_squares(start_range, end_range)
