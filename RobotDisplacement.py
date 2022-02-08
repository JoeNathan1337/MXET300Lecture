# Jonathan Burgess
# First made: 2/1/2022
# Last update: 2/8/2022
# This program is to calculate the displacement in a global from an origin in a local frame.


import math as m                                            # library math needed for sin and cos functions


theta = float(0)                                            # initialize variables as floats
xdis = float(0)
ydis = float(0)

x = float(input("Initial Global X Displacement: "))         # input the local frame x origin
y = float(input("Initial Global Y Displacement: "))         # input the local frame y origin

more = "Y"


while more == "y" or more == "Y":                           # while loop is for multiple displacements
    theta = float(input("Heading angle in degrees: "))      # input the heading angle relative to global x axis
    theta = theta*m.pi/180                                  # convert degree to radian
    xdis = float(input("Local X displacement: "))           # input the x displacement
    ydis = float(input("Local Y displacement: "))           # input the y displacement
    x += m.cos(theta)*xdis - m.sin(theta)*ydis              # calculate the new x position in global frame
    y += m.sin(theta)*xdis + m.cos(theta)*ydis              # calculate the new y position in global frame
    print("Current Global X Coordinate:", x)                # print new x coordinate
    print("Current Global Y Coordinate:", y)                # print new y coordinate
    more = input("Continue? (Y/N)")                         # ask to continue movement

print("\nFinal global coordinates are:")                    # print final x and y global coordinates
print("(", x, ",", y, ")")
