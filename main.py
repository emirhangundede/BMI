import tkinter

window_screen = tkinter.Tk()
window_screen.minsize(height=200, width=300)
window_screen.maxsize(height=200, width=300)

height_label = tkinter.Label(text="Enter Your Height", font=("Arial Bold", 15))
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()

weight_label = tkinter.Label(text="Enter Your Weight", font=("Arial Bold", 15))
weight_label.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

calculate_label = tkinter.Label()


def bmi_calculate():
    calculate = 0
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    calculate = float((weight / height ** 2))
    print(calculate)

    if calculate <= 18.49:
        calculate_label.config(text=f"You are Underweight:{calculate}")
        calculate_label.pack()
    if 18.5 <= calculate <= 24.99:
        calculate_label.config(text=f"You are Normal:{calculate}")
        calculate_label.pack()
    if 25 <= calculate <= 29.99:
        calculate_label.config(text=f"You are Overweight:{calculate}")
        calculate_label.pack()
    if calculate > 30:
        calculate_label.config(text=f"You are Obese:{calculate}")
        calculate_label.pack()

calculate_button = tkinter.Button(text="Calculate", command=bmi_calculate)
calculate_button.pack()

window_screen.mainloop()
