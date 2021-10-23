def charactor(string):
    uppercount=0
    lowercount=0
    for ch in string:
        if ch.islower():
            lowercount+=1
        elif ch.isupper:
            uppercount+=1
    print("lower",lowercount)
    print("upper",uppercount)
charactor("Shraddha Going To Maraket")         

    