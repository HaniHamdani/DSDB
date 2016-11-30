class Fib1:

    def __init__(self,n):
        self.n = n

    def fib(self,m):
        if(m<2):
            return m
        else:
            return self.fib(m-1)+self.fib(m-2)
#Cet algorithme présente la solution récursive du problème
#Sa complexité est exponentielle

    def run(self):
        S=0
        for i in range(1,self.n+1):
            S+=self.fib(i)
        return S

class Fib2:

    def __init__(self,n):
        self.n = n

    def fib(self,m):
        a, b = 0, 1
        for i in range(0, m):
            a, b = b, a + b
        return a
#Cet algorithme est léger en mémoire et en quantité de traitement

    def run(self):
        S=0
        for i in range(1,self.n+1):
            S+=self.fib(i)
        return S

class Fib3:

    def __init__(self,n):
        self.n = n

    def fib(self,m):
        T = [0, 1]
        for i in range(1, m):
            T.append(T[-1] + T[-2])
        return T[m]
#Cet algorithme stocke chaque élément de la suite de Fibonacci dans une liste
#ce qui peut être gourmand en mémoire surtout pour un grand n

    def run(self):
        S=0
        for i in range(1,self.n+1):
            S+=self.fib(i)
        return S

def get_classes(s1,s2,s3):
    return (dir(s1)+dir(s2)+dir(s3))

test1 = Fib1(15)
print(test1.run())
test2 = Fib2(15)
print(test2.run())
test3 = Fib3(15)
print(test3.run())
print(get_classes(test1,test2,test3))
