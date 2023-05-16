import customtkinter as ctk

class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.geometry('500x500')
        self.title = 'QR CODE'
        
        self._main_window()
    
    def generate_qr_code(self):
            pass

    def _main_window(self):
        display_frame = ctk.CTkFrame(master = self)
        display_frame.pack(pady = 20, padx = 100, fill = 'both', expand = True) 

        label = ctk.CTkLabel(master = display_frame, text = 'QR Code Configuration', font = ('Roboto', 20))
        label.pack()

        entry_qr_color_r = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter QR Code color value - R', width = 300, justify = 'center')
        entry_qr_color_r.pack(pady = 12, padx = 10)

        entry_qr_color_g = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter QR Code color value - G', width = 300, justify = 'center')
        entry_qr_color_g.pack(pady = 12, padx = 10)

        entry_qr_color_b = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter QR Code color value - B', width = 300, justify = 'center')
        entry_qr_color_b.pack(pady = 12, padx = 10)

        entry_bg_color_r = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter background color value - R', width = 300, justify = 'center')
        entry_bg_color_r.pack(pady = 12, padx = 10)

        entry_bg_color_g = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter background color value - G', width = 300, justify = 'center')
        entry_bg_color_g.pack(pady = 12, padx = 10)

        entry_bg_color_b = ctk.CTkEntry(master = display_frame, placeholder_text = 'Enter background color value - B', width = 300, justify = 'center')
        entry_bg_color_b.pack(pady = 12, padx = 10)

        button = ctk.CTkButton(master = display_frame, text = 'Generate QR Code', command = self.generate_qr_code())
        button.pack(pady = 12, padx = 10)


janela = Root()
janela.mainloop()