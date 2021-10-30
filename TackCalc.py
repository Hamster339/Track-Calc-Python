import math
import tkinter


# Function that calculates total distance and time when tacking
def calc(tackLength, angleToWind, straghtLineDistance, speed, result_button):
    try:
        tackLength = int(tackLength)
        angleToWind = int(angleToWind)
        straghtLineDistance = int(straghtLineDistance)
        speed = int(speed)
    except:
        result_button.config(text="Error: Some inputs are not numbers")
    else:
        try:
            distanceGain = tackLength * math.cos(angleToWind)
            numOfTacks = straghtLineDistance // distanceGain

            totalDistance = tackLength * numOfTacks
            time = totalDistance / speed
        except:
            result_button.config(text="Error: invalid inputs")
        else:
            result_button.config(
                text=("Result: " + "Total Distance: " + str(totalDistance) + "nM " + "Time: " + str(time) + "hrs "))


top = tkinter.Tk()
top.title("Navigation Calculator")

# Label and entry button of Length of Tack
L1 = tkinter.Label(top, text="  Length of Tack")
L1.grid(column=0, row=0)
E1 = tkinter.Entry(top, width=5, )
E1.grid(column=0, row=1)

# Label and entry button of Angle to Wind
L2 = tkinter.Label(top, text="  Angle to Wind")
L2.grid(column=1, row=0)
E2 = tkinter.Entry(top, width=5)
E2.grid(column=1, row=1)

# Label and entry button of Straight Line Distance
L3 = tkinter.Label(top, text="  Straight Line Distance")
L3.grid(column=2, row=0)
E3 = tkinter.Entry(top, width=5)
E3.grid(column=2, row=1)

# Label and entry button of Speed
L4 = tkinter.Label(top, text="  Speed")
L4.grid(column=3, row=0)
E4 = tkinter.Entry(top, width=5)
E4.grid(column=3, row=1)

# Submit button
B1 = tkinter.Button(top, text="Calculate", command=lambda: calc(E1.get(), E2.get(), E3.get(), E4.get(), L5))
B1.grid(column=4, row=1)

# Result label
L5 = tkinter.Label(top, text="Result: ")
L5.grid(column=0, row=2, columnspan=4, sticky="w")

top.mainloop()
