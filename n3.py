#1
e = ['Element', 'start', 'finish']
def append(*args):
    for i in args:
        e.insert(-1, i)
    return(e)
print(append(1,'x',3))
#2
def new(*args):
    t = 0
    c = {}
    for i in args:
        c.update({i: t +1})
        t+=1
    return(c)
print(new('x','y','z'))
#3
def qq(*args):
    a= []
    b =[]
    for i in args:
        if i % 2==0:
            a.append(i)
            b.append(i**2)
        else:
            b.append(i**2)
    return(a,b)
print(qq(1,2,3,4,5))
