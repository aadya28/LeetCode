n = 243
product = 1 
s = 0
while n >0 :
    remainder = n % 10
    n = int(n / 10)
    product = product * remainder
    s = s + remainder
result = product - s
print(result)
