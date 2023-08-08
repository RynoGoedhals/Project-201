from tkinter import *

window = Tk()

window.geometry("500x400")
window.title("Simple Interest Calculator")
window.configure(bg= "white")

def calc_int():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p * r * t) /100
    interest = round(i, 2)

    result_label.destroy()

    message = Label(result_frame, text= "Interest on Rs." + str(p) + " at rate of interest " + str(r) + "% for " + str(t) + " years is Rs." + str(interest), bg= "white", font= ("Calibri", 12), width= 55)
    message.place(x= 20, y= 320)
    message.pack()

app_label = Label(window, text= "Simple Interest Calculator", fg= "black", bg= "white", font= ("Calibri", 20), bd= 5)
app_label.place(x= 100, y= 20)

principle_label = Label(window, text= "Principle:", fg= "black", bg= "white", font= ("Calibri", 12), bd= 1)
principle_label.place(x= 20, y= 100)

principle_entry = Entry(window, text= "", bd= 2, width= 15, bg= "lightgrey")
principle_entry.place(x= 100, y= 102)

rate_label = Label(window, text= "Rate of Interest:", fg= "black", bg= "white", font= ("Calibri", 12), bd= 1)
rate_label.place(x= 20, y= 140)

rate_entry = Entry(window, text= "", bd= 2, width= 15, bg= "lightgrey")
rate_entry.place(x= 140, y= 142)

time_label = Label(window, text= "Time:", fg= "black", bg= "white", font= ("Calibri", 12), bd= 1)
time_label.place(x= 20, y= 180)

time_entry = Entry(window, text= "", bd= 2, width= 15, bg= "lightgrey")
time_entry.place(x= 70, y= 182)

calc_button = Button(window, text= "Calculate", fg= "black", bg= "lightgrey", bd= 4, command= calc_int)
calc_button.place(x= 200, y= 230)

result_frame = LabelFrame(window, text= "Result", bg= "white", font= ("Calibri", 12))
result_frame.pack(padx= 20, pady= 20)
result_frame.place(x= 10, y= 300)

result_label = Label(result_frame, text= "", bg= "white", font= ("Calibri", 12), width= 59)
result_label.place(x= 10,y= 20)
result_label.pack()

window.mainloop()