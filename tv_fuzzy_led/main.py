from system import tv_variables, tv_rules, tv_model
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import tkinter as tk

class LedSystem():
    def __init__(self, variables, rules, model):
        self.variables = variables
        self.rules = rules
        self.model = model

        # Objects to draw into pykinter
        self.canvas = None
        self.toolbar = None

    def set_root(self, window):
        self.window = window 

    def plot(self, distance, light_intensity):
        self.model.plot(
            variables=self.variables,
            rules=self.rules,
            distance=distance,
            light_intensity=light_intensity)

    def slider(self):
        label_frame1 = tk.LabelFrame(self.window, text="Distance", padx=0, pady=0)
        label_frame2 = tk.LabelFrame(self.window, text="Light intensity", padx=0, pady=0)

        self.w1 = tk.Scale(label_frame1, from_=2.0, to=10.0, orient=tk.HORIZONTAL, digits=3, resolution=0.1, length=200)
        self.w1.set(6.0)
        self.w1.pack()
        self.w2 = tk.Scale(label_frame2, from_=0.0, to=100.0, orient=tk.HORIZONTAL, digits=4, resolution=0.1, length=200)
        self.w2.set(50.0)
        self.w2.pack()

        label_frame1.pack(side="top", padx=10, pady=5)
        label_frame2.pack(side="top", padx=10, pady=5)

    def display(self):
        # the figure that will contain the plot
        fig = plt.figure(figsize=(20,10))
        self.plot(self.w1.get(), self.w2.get())
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        if self.canvas: self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(fig,
                                master = self.window)  
        self.canvas.draw()
    
        # creating the Matplotlib toolbar
        if self.toolbar: self.toolbar.destroy()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.window)
        self.toolbar.update()
        
        self.canvas.get_tk_widget().pack()

    def custom_input(self):
        value = self.ask_entry(self.window, "Enter the distance(2 - 10m):")

        try:
            self.w1.set(float(value))
        except ValueError as e:
            self.w1.set(6.0)

        value = self.ask_entry(self.window, "Enter the light intensity(0 - 100%):")
        try:
            self.w2.set(float(value))
        except ValueError as e:
            self.w2.set(50.0)
        

    def ask_entry(self, root, prompt):
        dialog = EntryFrame(root, prompt=prompt)
        return dialog.show()

    def quit(self):
        self.window.destroy()
        exit()


class EntryFrame:
    def __init__(self, parent, prompt="", default=""):
        self.popup = tk.Toplevel(parent)
        self.popup.title(prompt)
        self.popup.transient(parent)
        self.selection = tk.StringVar()
        self.label = None

        frame = tk.LabelFrame(self.popup, text=default, padx=0, pady=0)
        frame.pack(padx=50, pady=50)

        label = tk.Label(frame, text=prompt)
        frame_entry = tk.Frame(frame)

        frame_entry.pack(side="bottom", fill="x")
        label.pack(side="top", fill="x", padx=20, pady=10)
        self.entry = tk.Entry(
            frame_entry, width=35, borderwidth=5, textvariable=self.selection
        )
        self.entry.pack(side="top", fill="x", padx=20, pady=10)

        submit = tk.Button(frame, text="Submit", command=self.popup.destroy)
        submit.pack(side="top")

    def show(self):
        self.popup.wait_window(self.popup)
        return self.selection.get()

       
if __name__ == '__main__':
    system = LedSystem(tv_variables, tv_rules, tv_model)
    
    # the main Tkinter window
    window = tk.Tk()
    system.set_root(window)
    
    # setting the title 
    window.title('TV Led brightness Fuzzy System')
    
    # dimensions of the main window
    window.geometry("1000x900")
    
    # button that displays the plot
    plot_button = tk.Button(master = window, 
                        command = system.display,
                        height = 2, 
                        width = 10,
                        text = "Plot")

    plot_button.pack()
  
    # button that displays the plot
    custom_button = tk.Button(master = window, 
                        command = system.custom_input,
                        height = 2, 
                        width = 10,
                        text = "Custom Input")

    custom_button.pack()
    system.slider()

    window.protocol("WM_DELETE_WINDOW", system.quit)
    tk.Button(window, text="Quit", command=system.quit).pack()

    # run the gui
    window.mainloop()               

