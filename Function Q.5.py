# def check_numbers():
#     j=int(input("enter the number"))
#     k=int(input("enter the number"))
#     if j%2==0 :
#         print(j," even number hai")
#     elif k%2==0:
#         print(k,"even number hai")    
#     else:
#         print("Dono number even nahi hai")    
# check_numbers()   

         
def check_numbers_list(j,k):
    i=0
    while i<len(j):
        if j[i]%2==0:
            print(i,"even no")
        else:
            print(i,"odd no")
        i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])                


