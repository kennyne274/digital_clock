import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("350x180")
window.configure(bg="black")
window.resizable(0, 0)  # 0 = False

# ===== Font settings =====
# If DS-Digital font is not available, you can replace it with Courier
font_time = ("DS-Digital", 65, "bold")
font_date = ("DS-Digital", 16, "bold")

# ===== Date display label =====
date_label = tk.Label(
    window,
    font=font_date,
    bg="#2B2B2B",
    fg="#39FF14"  
)
date_label.pack(pady=(25, 0)) 

# ===== Time display label =====
clock_label = tk.Label(
    window,
    font=font_time,
    bg="#2B2B2B",
    fg="cyan"  
)
clock_label.pack(expand=True)

# ===== Clock update function =====
def clock():
    # Get current date and time
    current_date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%H:%M:%S")

    # Update label text
    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    # Call this function again after 1 second
    window.after(1000, clock)

# Start the clock
clock()
window.mainloop()
