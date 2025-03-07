def mirrored_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

size = int(input("Enter the size of the triangle: "))
mirrored_triangle(size)
