txt = "hello, my name is nadine"
y = txt.capitalize()

myTuple = ("John", "Peter", "Vicky")
z = "#".join(myTuple)

txt2 = "I like bananas"
c = txt2.replace("bananas", "apples")

while(1):
    x = input("What number you whant to press?\n1) caplitize  2) Join  3) Replace\n")
    x = int (x)
    if x == 1:
            print (y)
        
    if x == 2:
            print (z)
        
    if x == 3:
            print (c)
    
    if x == '\n':
        exit()
    