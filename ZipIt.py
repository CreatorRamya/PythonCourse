s1 = {3, 6, 8}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [20, 30, 50, 70]
list2 = [200, 300, 500, 700]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks = ['reliance', 'infosys', 'tcs']
prices = [2174, 1232, 3724]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}

print('\n'.format(new_dict))