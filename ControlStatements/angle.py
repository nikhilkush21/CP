angle=int(input("Enter angle in degree: "))
if (angle < 90):
    print("Acute angle")
elif(angle == 90):
    print("Right angle")
elif(angle > 90 and angle < 180):
    print("Obtuse angle")
