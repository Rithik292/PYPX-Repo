import tkinter as tk
import customtkinter as ctk


# --- Main App Controller (visual refresh) ---
class PodcastApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x560")
        self.title("Podcast Action")

        # Modern default: dark appearance with green accent
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Variable to control dark/light toggle in Settings
        self.dark_mode_var = tk.BooleanVar(value=(ctk.get_appearance_mode() == "dark"))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Left sidebar
        side = ctk.CTkFrame(self, width=180, corner_radius=8, fg_color="#143B29")
        side.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)

        # App name
        ctk.CTkLabel(side, text="PYPX", text_color="#B8F5C7", font=("Arial", 18, "bold")).pack(pady=(18, 12))

        # Navigation buttons (clean, consistent)
        nav_btn_config = dict(fg_color="transparent", hover_color="#1F6A3F", width=150, height=44, corner_radius=10)
        ctk.CTkButton(side, text="Home", command=lambda: self.show_frame("HomePage"), **nav_btn_config).pack(pady=6)
        ctk.CTkButton(side, text="Settings", command=lambda: self.show_frame("SettingsPage"), **nav_btn_config).pack(pady=6)
        ctk.CTkButton(side, text="About", command=lambda: self.show_frame("AboutPage"), **nav_btn_config).pack(pady=6)

        # Right / main container
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew", padx=12, pady=8)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Register pages
        self.frames = {}
        for F in (HomePage, SettingsPage, AboutPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def toggle_appearance(self):
        # Called from SettingsPage switch
        if self.dark_mode_var.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")



# --- HomePage Class (refreshed layout & styling) ---
class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller

        # Grid setup to center the action card vertically when window is large/fullscreen
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Top title area (kept compact)
        top = ctk.CTkFrame(self, fg_color="transparent")
        top.grid(row=1, column=0, sticky="ew", pady=(8, 0))
        top.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(top, text="PYPX Action - Podcast", font=("Arial", 24, "bold")).pack(pady=(6, 0))
        ctk.CTkLabel(top, text="Quick actions", font=("Arial", 12), text_color="#9EE6A6").pack(pady=(0, 12))

        # Center card to hold main buttons (placed in middle row)
        card = ctk.CTkFrame(self, fg_color="#1A1A1A", corner_radius=12, border_width=1, border_color="#2E6F40")
        card.grid(row=2, column=0, sticky="nsew", padx=24, pady=12)
        card.grid_rowconfigure((0, 1), weight=1)
        card.grid_columnconfigure((0, 1), weight=1)

        PAD = 12
        btn_style = dict(width=160, height=100, corner_radius=12, fg_color="#2E6F40", hover_color="#3D8E52", font=("Arial", 14, "bold"))

        ctk.CTkButton(card, text="▶ Ep 1", **btn_style).grid(row=0, column=0, padx=PAD, pady=PAD, sticky="nsew")
        ctk.CTkButton(card, text="▶ Ep 2", **btn_style).grid(row=0, column=1, padx=PAD, pady=PAD, sticky="nsew")
        ctk.CTkButton(card, text="▶ Ep 3", **btn_style).grid(row=1, column=0, padx=PAD, pady=PAD, sticky="nsew")
        ctk.CTkButton(card, text="▶ Ep 4", **btn_style).grid(row=1, column=1, padx=PAD, pady=PAD, sticky="nsew")


# --- SettingsPage Class (add dark-mode toggle) ---
class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller

        ctk.CTkLabel(self, text="Application Settings", font=("Arial", 22, "bold")).pack(pady=(18, 6))

        # Dark mode toggle
        switch = ctk.CTkSwitch(self, text="Dark Mode", variable=self.controller.dark_mode_var, command=self.controller.toggle_appearance)
        switch.pack(pady=(6, 12))

        # Simple navigation button
        ctk.CTkButton(self, text="← Back to Home", command=lambda: self.controller.show_frame("HomePage")).pack(pady=18)


class AboutPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        # Intentionally empty — user will fill content later
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        # Provide an empty, visible textbox the user can edit later
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        textbox = ctk.CTkTextbox(self, width=600, corner_radius=8)
        textbox.insert("0.0", "Our Podcast Aims to spread awareness about Migration and Community Displacement and we wish you also promote awareness, we are the movement Crew from PYP 5F")
        textbox.grid(row=0, column=0, sticky="nsew", padx=18, pady=18)

# --- Run the application ---
if __name__ == "__main__":
    app = PodcastApp()
    app.mainloop()



