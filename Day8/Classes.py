#pascal naming conventions
class Point:
    def move(self):
        print("Move")
    def Draw(self):
        print("Draw")



point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.Draw()

point2 = Point()
