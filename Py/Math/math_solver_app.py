import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class MathSolverApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Math Solver Application")
        self.geometry("800x600")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create tabview
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create tabs
        self.tabview.add("Newton Method")
        self.tabview.add("Bisection Method")
        
        # Setup Newton Method tab
        self.setup_newton_tab()
        
        # Setup Bisection Method tab
        self.setup_bisection_tab()

    def setup_newton_tab(self):
        newton_frame = self.tabview.tab("Newton Method")
        
        # Function selection
        ctk.CTkLabel(newton_frame, text="Select Function:").pack(pady=5)
        self.function_var = ctk.StringVar(value="x²-4x+3")
        functions = ["x²-4x+3", "x²-2", "x³-x-1", "eˣ-3x"]
        self.function_menu = ctk.CTkOptionMenu(newton_frame, values=functions, variable=self.function_var)
        self.function_menu.pack(pady=5)

        # Initial guess
        ctk.CTkLabel(newton_frame, text="Initial guess (x₀):").pack(pady=5)
        self.x0_entry = ctk.CTkEntry(newton_frame)
        self.x0_entry.pack(pady=5)
        self.x0_entry.insert(0, "1.0")

        # Precision
        ctk.CTkLabel(newton_frame, text="Precision:").pack(pady=5)
        self.precision_entry = ctk.CTkEntry(newton_frame)
        self.precision_entry.pack(pady=5)
        self.precision_entry.insert(0, "1e-6")

        # Solve button
        ctk.CTkButton(newton_frame, text="Solve", command=self.solve_newton).pack(pady=20)

        # Result label
        self.newton_result_label = ctk.CTkLabel(newton_frame, text="")
        self.newton_result_label.pack(pady=10)

        # Plot frame
        self.newton_plot_frame = ctk.CTkFrame(newton_frame)
        self.newton_plot_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    def setup_bisection_tab(self):
        bisection_frame = self.tabview.tab("Bisection Method")
        
        # Interval inputs
        interval_frame = ctk.CTkFrame(bisection_frame)
        interval_frame.pack(pady=10, fill="x", padx=20)
        
        ctk.CTkLabel(interval_frame, text="Interval start (a):").pack(side="left", padx=5)
        self.a_entry = ctk.CTkEntry(interval_frame, width=100)
        self.a_entry.pack(side="left", padx=5)
        
        ctk.CTkLabel(interval_frame, text="Interval end (b):").pack(side="left", padx=5)
        self.b_entry = ctk.CTkEntry(interval_frame, width=100)
        self.b_entry.pack(side="left", padx=5)

        # Altitude (iterations)
        alt_frame = ctk.CTkFrame(bisection_frame)
        alt_frame.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(alt_frame, text="Number of iterations:").pack(side="left", padx=5)
        self.alt_entry = ctk.CTkEntry(alt_frame, width=100)
        self.alt_entry.pack(side="left", padx=5)
        self.alt_entry.insert(0, "10")

        # Solve button
        ctk.CTkButton(bisection_frame, text="Solve", command=self.solve_bisection).pack(pady=20)

        # Result display
        self.bisection_result_text = ctk.CTkTextbox(bisection_frame, height=200)
        self.bisection_result_text.pack(fill="both", expand=True, padx=20, pady=10)

    def newton(self, f, df, x0, precision):
        try:
            x = float(x0)
            steps = []
            while True:
                fx = f(x)
                dfx = df(x)
                if abs(fx) < precision:
                    break
                if dfx == 0:
                    raise ValueError("Derivative equals zero. No solution found.")
                correction = fx / dfx
                x = x - correction
                steps.append(x)
                if len(steps) > 100:  # Prevent infinite loops
                    raise ValueError("Method did not converge after 100 iterations")
            return x, steps
        except Exception as e:
            raise ValueError(f"Error in Newton's method: {str(e)}")

    def get_function_and_derivative(self, func_name):
        if func_name == "x²-4x+3":
            return lambda x: x**2 - 4*x + 3, lambda x: 2*x - 4
        elif func_name == "x²-2":
            return lambda x: x**2 - 2, lambda x: 2*x
        elif func_name == "x³-x-1":
            return lambda x: x**3 - x - 1, lambda x: 3*x**2 - 1
        elif func_name == "eˣ-3x":
            return lambda x: np.exp(x) - 3*x, lambda x: np.exp(x) - 3
        else:
            raise ValueError("Unknown function")

    def solve_newton(self):
        try:
            f, df = self.get_function_and_derivative(self.function_var.get())
            x0 = float(self.x0_entry.get())
            precision = float(self.precision_entry.get())
            
            root, steps = self.newton(f, df, x0, precision)
            
            # Update result label
            self.newton_result_label.configure(text=f"Root found at x = {root:.6f}")
            
            # Plot the function and steps
            self.plot_newton_result(f, root, steps)
            
        except Exception as e:
            self.newton_result_label.configure(text=f"Error: {str(e)}")

    def plot_newton_result(self, f, root, steps):
        # Clear previous plot
        for widget in self.newton_plot_frame.winfo_children():
            widget.destroy()

        # Create new plot
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.linspace(root-2, root+2, 1000)
        y = [f(xi) for xi in x]
        ax.plot(x, y, 'b-', label='f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        ax.plot(root, f(root), 'r*', label='Root')
        
        # Plot steps
        if steps:
            x_steps = steps
            y_steps = [f(x) for x in steps]
            ax.plot(x_steps, y_steps, 'g.-', label='Steps')
        
        ax.grid(True)
        ax.legend()
        
        # Embed plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, self.newton_plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def solve_bisection(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            alt = int(self.alt_entry.get())
            
            self.bisection_result_text.delete("0.0", "end")
            
            if alt <= 0:
                self.bisection_result_text.insert("end", "The number of iterations must be positive.\n")
                return
                
            for i in range(alt):
                c = (a + b) / 2
                self.bisection_result_text.insert("end", f"\nIteration {i+1}:\n")
                self.bisection_result_text.insert("end", f"Current interval: [{a}, {b}]\n")
                self.bisection_result_text.insert("end", f"Midpoint c = {c}\n")
                
                # In a real application, you would calculate f(c) here
                # For this demo, we'll ask the user to input f(c)
                self.bisection_result_text.insert("end", f"Please calculate f({c}) and enter the result.\n")
                
            self.bisection_result_text.insert("end", "\nCalculation completed.")
            
        except ValueError as e:
            self.bisection_result_text.insert("end", f"Error: {str(e)}\n")

if __name__ == "__main__":
    app = MathSolverApp()
    app.mainloop()