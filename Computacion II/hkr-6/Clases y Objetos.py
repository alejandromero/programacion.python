class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def reset(self):
        self.x=0
        self.y=0
    def calculate_distance(self,otherPoint):
        D=((otherPoint.x-self.x)**2 + (otherPoint.y-self.y)**2 )**0.5
        return D

distances=[]
for i in range((int(raw_input())/2)):
    distances.append(Point(*map(int,raw_input().split())).calculate_distance(Point(*map(int,raw_input().split()))))

for i in distances:
    print i
