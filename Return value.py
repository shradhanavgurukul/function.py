# def add_numbers(number_x,number_y):
#     number_sum=number_x+number_y
#     return number_sum
# sum1=add_numbers(20,40)
# print(sum1)
# sum2=add_numbers(560,23)
# a=1234
# b=12
# sum3=add_numbers(a,b)
# print(sum2)
# print(sum3)
# numbers_a=add_numbers(20,40)/add_numbers(5,1)
# print(numbers_a)




# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4))


def add_numbers_more(number_x, number_y):
    number_sum = number_x + number_y
    print ("Hello from NavGurukul ;)")
    return number_sum
    number_sum = number_x + number_x
    print ("Kya main yahan tak pahunchunga?")
    return number_sum
sum6 = add_numbers_more(100, 20)


def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"
        print ("Kya main print ho payungi? :-(")
mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu)



def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print ("Kya main print ho payungi? :-(")
    return food
    print ("Lekin main toh pakka nahi print hounga :'(")
print(menu("tuesday"))

