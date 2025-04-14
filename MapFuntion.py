numbers1 = [3, 4, 5]
numbers2 = [6, 7, 8]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

nums = [3, 4, 5, 6, 7]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Squares of the numbers in the list are: ")
print(square)