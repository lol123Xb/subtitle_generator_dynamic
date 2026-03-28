import customtkinter as ctk


class SubtitleOverlay:
    def __init__(self, overlay_queue):
        self.overlay_queue = overlay_queue

        self.app = ctk.CTk()
        self.app.geometry("1000x120+500+950")  # "{width}x{height}+{x_offset}+{y_offset}"
        self.app.overrideredirect(True)
        self.app.attributes("-topmost", True)
        self.app.attributes("-alpha", 0.85)

        self.label = ctk.CTkLabel(
            self.app,
            text="",
            font=("Arial", 28),
            wraplength=900
        )
        self.label.pack(expand=True, fill="both")

        self.update_text()

    def update_text(self):
        try:
            text = self.overlay_queue.get_nowait()
            self.label.configure(text=text)
        except:
            pass

        self.app.after(200, self.update_text)

    def run(self):
        self.app.mainloop()
