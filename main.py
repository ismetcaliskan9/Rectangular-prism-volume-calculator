length = int(input("enter an integer that represents length in feet "))
width = int(input("enter an integer that represents width in feet "))
height = int(input("enter an integer that represents height in feet "))


def prism_vol_calculator(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(prism_vol_calculator(length, width, height)) + " cubic feet. ")