import tkinter
from triangle_package_v2 import triangle



#createing basic window
window = tkinter.Tk()
window.title("Area of triangle")
window.geometry("852x480")

#adding lables and fields to window
tkinter.Label(window, text="Base (b):").grid(row=1)
tkinter.Label(window, text="Height (h):").grid(row=2)
tkinter.Label(window,text="Area= ").grid(row=3)

txtVal1= tkinter.Entry(window, width=15)
txtVal1.grid(column=1, row=1)
txtVal1.focus()

txtVal2= tkinter.Entry(window, width=15)
txtVal2.grid(column=1, row=2)

areaCalculated = tkinter.Entry(window, width=15)
areaCalculated.grid(column=1, row=3)

def calculate():
    areaCalculated.delete(0, "end")
    b = txtVal1.get()
    h = txtVal2.get()
    area = triangle.calculate_area(float(h),float(b))
    areaCalculated.insert(0,area)

def close():
    window.destroy()

btn = tkinter.Button(window, text="Calculate", command= calculate)
btn.grid(column=0, row=4)

btn = tkinter.Button(window, text="Exit", command= close)
btn.grid(column=1, row=4)




#needs to be at the end of the code
window.mainloop()