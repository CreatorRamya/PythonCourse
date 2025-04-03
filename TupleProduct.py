def calculate_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

product1 = calculate_product(tup1)
product2 = calculate_product(tup2)

print(f"The product of elements in tup1 is: {product1}")
print(f"The product of elements in tup2 is: {product2}")
