def multiply(limit):
    i=1
    sum=0
    while i<limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
multiply(11)