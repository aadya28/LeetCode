def reverse_a_number(num):
    ans = 0
    while num > 0:
        digit = num % 10
        ans = ((ans*10)+digit)
        num = int (num/10)    
    return ans

num = 1234
print(reverse_a_number(num)) 