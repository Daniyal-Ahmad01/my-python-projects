def add(a):
    try:
        a=int(input("Enter a number:"))
        return(a)
    except:
        print("This is an errror be careful")
        return(a)
    finally:
        print("NOICE")
ac=int(input("Enter a number:"))
print(add(ac))