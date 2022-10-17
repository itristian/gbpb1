
n = int(input("number"))
nres = n + 11*n + 111*n
print(nres)
tc = int(input("tc is "))
p = int(input("p is "))
emp = int(input("employee num is "))
if tc <= p:
print("pribilno")
rentability = p/tc
avg = p/emp
print(f'rentability is {rentability} and average income per employee is {avg}')
else:
print('ubitok')1
a = int(input("first day"))
b = int(input("last day"))
daycount = 0
while a < b:
a = (a*1.1)
print(f'hes ran {round(a, 3)} km on his {daycount}th day')
daycount += 1
print(f'he needed {daycount} days to run {b} km')
