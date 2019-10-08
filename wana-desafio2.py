import numpy as np

def string_intersection(st1,st2):
    output= ""
    for i in st1:
        if i in st2 and not i in output:
            output += i

    return print("Answer: ", len(output))

if __name__ =="__main__":
    while 1:
        a = input("Write a string, please:\n")
        b = input("Write a second string, please:\n")
        string_intersection(a,b)
        stop = input("Have you done (y/N)?")    
        if stop == "y":
            break

    

    
