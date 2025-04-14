numbers = [1, 4, 6, 3, 8, 10, 7]

even = [x for x in numbers if x%2==0]
print("List of even numbers from the listed are: ", even)

#Dictionary Comprehension

myDict = {str(x): x**2 for x in [3, 5, 6, 7, 8]}
print(myDict)

#map function

def square(n):
    return n*n

numbers = (3, 6, 5, 2)
result = map(square, numbers)
print(list(result))