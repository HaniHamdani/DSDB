class Ex1:

    def __init__(self,n):
        self.n = n

    def run(self):
        S=0
        for i in range(1,self.n+1):
            if((i%3==0) or (i%5==0)):
                S+=i
        return S

    def get_classes(self):
        return (dir(self))

test = Ex1(15)
print(chichi.get_classes())
