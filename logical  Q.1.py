# write a python function to check whether a string is a pangram or not

def pangram():
    str="the quick brown fox jumps over the laz dg"
    b="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    a=True
    for i in b:
        if i not in str:
            a=False
    if(a==True):      
            print("true")
    else:
        print("false")
pangram()                         