def perfect_function(num):
    sum=0
    i=1
    while i<1000:
        if 1000%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print("is a perfect number",i)
    else:
        print("is not a perfect number",i)
perfect_function(6)            



                



                

