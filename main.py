import tkinter as tk
from tkinter import ttk, messagebox

try:
    from courses_data import COURSES
except Exception:
    COURSES = {}


def get_program_list():
    return sorted(COURSES.keys())


def get_levels():
    return ["Level 1", "Level 2", "Level 3", "Level 4"]


def safe_insert_text(text_widget, content):
    text_widget.configure(state="normal")
    text_widget.insert(tk.END, content)
    text_widget.configure(state="disabled")

def on_get_recommendations(program_name, level_name, text_widget):
    try:
        text_widget.configure(state="normal")
        text_widget.delete("1.0", tk.END)
        text_widget.configure(state="disabled")

        if not program_name:
            messagebox.showwarning("Input required", "Please select a program")
            return

        if not level_name:
            messagebox.showwarning("Input required", "Please select a level")
            return

        program = COURSES.get(program_name)
        if not program:
            messagebox.showerror("Not found", f"Program '{program_name}' not found.")
            return

        levels = program.get("levels", {})
        level = levels.get(level_name)
        if not level:
            messagebox.showinfo("No courses", "No courses found for this combination")
            return

        for sem_name, modules in level.items():
            safe_insert_text(text_widget, f"{sem_name}:\n")
            for mod in modules:
                code = mod.get("code", "")
                name = mod.get("name", "")
                credits = mod.get("credits", "")
                core = " (core)" if mod.get("core") else ""
                prereq = mod.get("prerequisite")
                prereq_str = f" - prereq: {prereq}" if prereq else ""
                safe_insert_text(text_widget, f"  {code}: {name} [{credits} credits]{core}{prereq_str}\n")
            safe_insert_text(text_widget, "\n")

    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred. Please check console for details.")
        print("Error in on_get_recommendations:", e, file=sys.stderr)

def center_window(root, width=600, height=400):
    """Center the tkinter window on the screen."""
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def build_gui():
    root = tk.Tk()
    root.title("Course Recommender System")
    window_width = 600
    window_height = 400
    center_window(root, window_width, window_height)

    # Styling
    header_font = ("Arial", 16, "bold")
    label_font = ("Arial", 12, "bold")
    normal_font = ("Arial", 10)

    bg_color = "#f5f7fb"
    header_bg = "#2b6cb0"
    btn_bg = "#3182ce"
    btn_fg = "white"

    root.configure(bg=bg_color)

    # Padding used consistently
    PAD = {"padx": 10, "pady": 10}

    # Header
    header = tk.Label(root, text="Course Recommender System", font=header_font, bg=header_bg, fg="white")
    header.grid(row=0, column=0, columnspan=3, sticky="ew")

    # Program label and combobox
    lbl_program = ttk.Label(root, text="Select Your Program", font=label_font, background=bg_color)
    lbl_program.grid(row=1, column=0, sticky="w", **PAD)

    program_var = tk.StringVar()
    cmb_program = ttk.Combobox(root, textvariable=program_var, state="readonly", font=normal_font)
    cmb_program["values"] = get_program_list()
    cmb_program.grid(row=1, column=1, sticky="ew", **PAD)

    # Level label and combobox
    lbl_level = ttk.Label(root, text="Select Your Level", font=label_font, background=bg_color)
    lbl_level.grid(row=2, column=0, sticky="w", **PAD)

    level_var = tk.StringVar()
    cmb_level = ttk.Combobox(root, textvariable=level_var, state="readonly", font=normal_font)
    cmb_level["values"] = get_levels()
    cmb_level.grid(row=2, column=1, sticky="ew", **PAD)

    # Results text area with scrollbar (read-only)
    txt_frame = tk.Frame(root)
    txt_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", **PAD)

    txt_results = tk.Text(txt_frame, height=12, wrap="word", state="disabled", font=normal_font)
    scrollbar = ttk.Scrollbar(txt_frame, orient="vertical", command=txt_results.yview)
    txt_results.configure(yscrollcommand=scrollbar.set)
    txt_results.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Button with styled appearance
    def on_enter(e):
        btn.configure(background="#2b6cb0")

    def on_leave(e):
        btn.configure(background=btn_bg)

    btn = tk.Button(root, text="Get Recommended Courses", bg=btn_bg, fg=btn_fg, font=label_font,
                    activebackground="#2b6cb0", relief="raised",
                    command=lambda: on_get_recommendations(program_var.get(), level_var.get(), txt_results))
    btn.grid(row=4, column=0, columnspan=3, **PAD)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    # Configure grid weights so results expand
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Set initial focus and simple instructional text
    safe_insert_text(txt_results, "Select a program and level, then click 'Get Recommended Courses' to view modules.\n")

    # Set focus to the program combobox to make the UI keyboard friendly
    cmb_program.focus_set()

    # Start the GUI loop
    root.mainloop()


if __name__ == "__main__":
    build_gui()
