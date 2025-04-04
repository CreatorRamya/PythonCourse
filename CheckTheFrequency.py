test_dict = {'Coding' : 3, 'is' : 3, 'really' : 3, 'helpfull' : 6, 'for' : 2, 'us': 3}

print("The orginal dictionary : " + str(test_dict))

R = 3

res = 0
for key in test_dict:
    if test_dict[key] == R:
        res = res + 1

print("Frequency of R is :" + str(res))