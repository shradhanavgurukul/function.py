# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print(max(numbers_list))


# a=[1,2,3,4,5,6]
# print(len(a))


def say_hello(name):
    print("hello",name)
    print("Aap kaise ho?")
say_hello("Aatif")    


# MULTIPLE FUNCTION ARGUMENT

# def add_numbers(number1,number2):
#     print("main do numbers ko add karunga")
#     print(number1+number2)
# add_numbers(120,50)
# num_x=134
# name="Rinki"
# print(num_x,name)    




# def say_hello_people(name_x,name_y,name_z,name_a):
#     print("Namaste",name_x)
#     print("Alah hafiz",name_y)
#     print("Bonjour",name_z)
#     print("Hello",name_a)
# say_hello_people("Imitiyaz","Rishabh","Rahul","Vidya")
# say_hello_people("Steve","Sawata","Shakrundin","Rajeev") 



# Arbitary Argument

# def icecream(*flavours):
#     for flavour in flavours:
#         print("i love"+flavour)
# icecream("chocolate","butterscotch","vanilla","strawberry")



# PARAMETER VALUE
# def attendance(name,status="absent"):
#     print(name,"is",status,"today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")    