import tkinter as tk
from tkinter import ttk
import serial

#Connect to Arduino
ArduinoData = serial.Serial('', 9600)
Current_Temp = float(ArduinoData.out_waiting)

def handle_ok_button():
    temperature = Current_Temp
    selection = combobox.get()
    
    if selection == "Warm":
        if temperature >= 28:
            message = f"It's warm and the temperature is {temperature}°C."
        elif temperature < 28:
            message = f"Heater has been turned on and the temperature is {temperature}°C"
    elif selection == "Cold":
        if temperature <= 22:
            message = f"It's cold and the temperature is {temperature}°C."
        elif temperature > 22:
            message = f"Air Conditioner has been turned on and the temperature is {temperature}°C"
    else:
        message = "Please select a temperature option."
    
    result_label.config(text=message)

def handle_continue_button():
    window.destroy()
    start_program()

def handle_stop_button():
    window.destroy()

def start_program():
    # Create the main window
    global window
    window = tk.Tk()
    window.geometry("400x200")
    window.title("Temperature Selector")

    # Create a label for temperature
    temp_label = ttk.Label(window, text="Temperature:")
    temp_label.pack()

    # Create a ComboBox
    global combobox
    combobox = ttk.Combobox(window, values=["Warm", "Cold"], state="readonly")
    combobox.pack()

    # Create an Entry field
    global entry
    entry = ttk.Label(window, text=str(Current_Temp)+' Celsius')
    entry.pack()

    # Create an OK button
    ok_button = ttk.Button(window, text="OK", command=handle_ok_button)
    ok_button.pack()

    # Create a label to display the result
    global result_label
    result_label = ttk.Label(window)
    result_label.pack()

    # Create a Continue button
    continue_button = ttk.Button(window, text="Continue", command=handle_continue_button)
    continue_button.pack()

    # Create a Stop button
    stop_button = ttk.Button(window, text="Stop", command=handle_stop_button)
    stop_button.pack()

    # Start the main event loop
    window.mainloop()

# Start the program
if __name__ == "__main__":
    start_program()