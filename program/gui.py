# gui.py

import tkinter as tk
from tkinter import messagebox
from scanner import scan_range


def start_scan():
    target = entry_target.get()
    start_port = entry_start.get()
    end_port = entry_end.get()

    if not target or not start_port or not end_port:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except ValueError:
        messagebox.showerror("Error", "Ports must be numbers!")
        return

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Scanning {target}...\n\n")

    results = scan_range(target, start_port, end_port)

    if results:
        for port, service in results:
            result_box.insert(tk.END, f"Port {port} is OPEN ({service})\n")
    else:
        result_box.insert(tk.END, "No open ports found.\n")


def create_gui():
    global entry_target, entry_start, entry_end, result_box

    window = tk.Tk()
    window.title("GUI-Based TCP Port Scanner")
    window.geometry("500x400")

    tk.Label(window, text="Target IP:").pack()
    entry_target = tk.Entry(window, width=30)
    entry_target.pack()

    tk.Label(window, text="Start Port:").pack()
    entry_start = tk.Entry(window, width=10)
    entry_start.pack()

    tk.Label(window, text="End Port:").pack()
    entry_end = tk.Entry(window, width=10)
    entry_end.pack()

    tk.Button(window, text="Start Scan", command=start_scan).pack(pady=10)

    result_box = tk.Text(window, height=15, width=60)
    result_box.pack()

    window.mainloop()