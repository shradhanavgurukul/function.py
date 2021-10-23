def sumofdigit(number):
    sum=0
    moduls=0
    while number!=0:
        moduls=number%10
        sum=sum+moduls
        number/=10
    return sum
print(sumofdigit(123))        