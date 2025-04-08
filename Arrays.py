import array as arr

array_num = arr.array('i', [1, 2, 4, 5, 6, 8, 9,])
print("Original array: "+str(array_num))

print("Number of occurences of the number 3 in the said array: " +str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))
