setm={1,2,}
myset =set(["hello"])
print(myset)
print('''nadine''')

s= '''nadine
            iti'''
print(s)
data=("  & nadine kunrtyuj  &   ")
print(data.strip("& na"))

txt="hello world"[::-1]
print(txt)
txt="hello world"[5::-1]
print(txt)
txt="hello world"[::-2]
print(txt)

data = ["all", "is", "good"]
data2= "****".join(data)
print(data2)
print(data2.split("****"))

a="hello"
print(a*5)

''' *function like micro 
    *function like macro
    *inline function 
    *periodic function '''

def PrintMyName(name= "Nadine"):
    print("My Name is: " + name)
