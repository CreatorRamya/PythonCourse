L = [5, 6, 8, 2, 12, 7, 10 ]
print("Original List : ", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("average = ", avg)

L.sort()

print("Smallest element is: ", L[0])
print("Largest element is: ", L[-1] )