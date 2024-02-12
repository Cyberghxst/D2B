import customtkinter as ctk
from typing import Any
from PIL import Image
import re, os, dotenv

dotenv.load_dotenv()

class Utils():
    """
    A Utility class for various methods.
    """
    def isbinary(entry: str | int):
        """
        Check if the provided number is a valid binary.
        """
        return False if re.match(r'^[01]+$', entry) == None else True
    
    def resolve_binary(binary: Any):
        """
        Resolves a binary number.
        """
        return str(binary)[2:]
    
    def bin2dec(entry: Any):
        """
        Converts a binary number to its decimal form.
        """
        return int(entry, 2)
    
    def dec2bin(entry: Any):
        """
        Converts a decimal number to its binary form.
        """
        return Utils.resolve_binary(bin(int(entry)))

class Graphic():
    """
    Load an image from local paths.
    """
    def  __init__(self, image_path: str):
        self._image = Image.open(image_path)

    def get_image(self):
        """
        Retrieves the loaded image.
        """
        return self._image

class ErrorDialog():
    """
    Represents an error dialog.
    """
    def __init__(self, title: str, message: str, width: int | None = None, height: int | None = None):
        self._corner_radius: int = 20
        self._dimentions: list[str] = []
        self.message: str = message
        self._window = ctk.CTk()

        # Handling dialog width.
        if width == None:
            self._dimentions.append('400')
        else:
            self._dimentions.append(str(width))
        
        # Handling dialog height.
        if height == None:
            self._dimentions.append('100')
        else:
            self._dimentions.append(str(height))
        
        # Window settings.
        self._window.title(title)
        self._window.geometry('x'.join(self._dimentions))

    def close(self):
        """
        Closes the error dialog.
        """
        self._window.destroy()

    def launch(self):
        """
        Launches the dialog error.
        """
        label = ctk.CTkLabel(
            master=self._window,
            text=self.message,
            font=ctk.CTkFont(family='Arial', size=16, weight='bold'),
            anchor=ctk.CENTER,
        )
        button = ctk.CTkButton(
            master=self._window,
            anchor=ctk.CENTER,
            text='OK',
            command=self.close,
            corner_radius=self._corner_radius,
            fg_color='#414141',
            hover_color='#212121'
        )
        label.pack_configure(
            pady=10
        )
        button.pack()
        self._window.mainloop()
        return self._window
    
class BinaryConverter():
    """
    Represents a binary to decimal converter window.
    """
    def __init__(self, width: int | None = None, height: int | None = None):
        # Window variables.
        self._name = os.getenv('CREATOR_NAME')
        self._button_corner_radius = 20
        self._dimentions: list[str] = []
        self._window = ctk.CTk()
        self._author = ctk.CTkLabel(
            master=self._window,
            text=f'Creado por: {self._name}'.upper(),
            font=ctk.CTkFont(family='Arial', weight='bold', size=10),
        )
        self._converter_title = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Arial', weight='bold', size=12),
            text='CONVERSOR BINARIO A DECIMAL'
        )
        self._entry = ctk.CTkEntry(
            master=self._window,
            placeholder_text='1000101'
        )
        self._result_title = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Arial', size=12, weight='bold'),
            text='RESULTADO'
        )
        self._result_placeholder = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Consolas', size=12),
            text='Sin resultados.'
        )
        self._convert_button = ctk.CTkButton(
            master=self._window,
            text='Convertir',
            corner_radius=self._button_corner_radius,
            command=self.on_convert
        )
        self._exit_button = ctk.CTkButton(
            master=self._window,
            text='Salir',
            corner_radius=self._button_corner_radius,
            command=self.close
        )

        # Handling dialog width.
        if width == None:
            self._dimentions.append('400')
        else:
            self._dimentions.append(str(width))
        
        # Handling dialog height.
        if height == None:
            self._dimentions.append('300')
        else:
            self._dimentions.append(str(height))

        # Window settings
        self._window.title('Conversor de Binario a Decimal')
        self._window.geometry('x'.join(self._dimentions))

    def get_window(self):
        """
        Returns the CTK window.
        """
        return self._window
    
    def close(self):
        """
        Close the converter window.
        """
        self._window.destroy()

    def init(self):
        """
        Starts the main loop for the converter window.
        """
        self._pack()
        self._window.mainloop()

    def on_convert(self):
        """
        Binary to digital converter program.
        """
        error_window = ErrorDialog('Oops!', 'Informe un valor binário válido.')
        if not Utils.isbinary(self._entry.get()):
            self._window.wait_window(error_window.launch())
        self._result_placeholder.configure(
            text=f'{Utils.bin2dec(self._entry.get())}'
        )

    def _pack(self):
        """
        Pack all components to this window.
        """
        self._converter_title.pack_configure(pady=5)
        self._author.pack_configure(pady=5)
        self._entry.pack_configure(pady=5)
        self._convert_button.pack_configure(pady=5)
        self._exit_button.pack_configure(pady=5)
        self._result_title.pack_configure(ipady=5)
        self._result_placeholder.pack_configure(pady=2)

class DecimalConverter():
    def __init__(self, width: int | None = None, height: int | None = None):
        # Window variables.
        self._name = os.getenv('CREATOR_NAME')
        self._button_corner_radius = 20
        self._dimentions: list[str] = []
        self._window = ctk.CTk()
        self._author = ctk.CTkLabel(
            master=self._window,
            text=f'Creado por: {self._name}'.upper(),
            font=ctk.CTkFont(family='Arial', weight='bold', size=10),
        )
        self._converter_title = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Arial', weight='bold', size=12),
            text='CONVERSOR DECIMAL A BINARIO'
        )
        self._entry = ctk.CTkEntry(
            master=self._window,
            placeholder_text='2683'
        )
        self._result_title = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Arial', size=12, weight='bold'),
            text='RESULTADO'
        )
        self._result_placeholder = ctk.CTkLabel(
            master=self._window,
            font=ctk.CTkFont(family='Consolas', size=12),
            text='Sin resultados.'
        )
        self._convert_button = ctk.CTkButton(
            master=self._window,
            text='Convertir',
            corner_radius=self._button_corner_radius,
            command=self.on_convert
        )
        self._exit_button = ctk.CTkButton(
            master=self._window,
            text='Salir',
            corner_radius=self._button_corner_radius,
            command=self.close
        )

        # Handling dialog width.
        if width == None:
            self._dimentions.append('400')
        else:
            self._dimentions.append(str(width))
        
        # Handling dialog height.
        if height == None:
            self._dimentions.append('300')
        else:
            self._dimentions.append(str(height))

        # Window settings
        self._window.title('Conversor de Decimal a Binario')
        self._window.geometry('x'.join(self._dimentions))

    def get_window(self):
        """
        Returns the CTK window.
        """
        return self._window
    
    def close(self):
        """
        Close the converter window.
        """
        self._window.destroy()

    def init(self):
        """
        Starts the main loop for the converter window.
        """
        self._pack()
        self._window.mainloop()

    def on_convert(self):
        """
        Decimal to binary converter program.
        """
        error_window = ErrorDialog('Oops!', 'Informe un valor decimal válido.')
        if not self._entry.get().isdecimal():
            self._window.wait_window(error_window.launch())
        self._result_placeholder.configure(
            text=f'{Utils.dec2bin(self._entry.get())}'
        )

    def _pack(self):
        """
        Pack all components to this window.
        """
        self._converter_title.pack_configure(pady=5)
        self._author.pack_configure(pady=5)
        self._entry.pack_configure(pady=5)
        self._convert_button.pack_configure(pady=5)
        self._exit_button.pack_configure(pady=5)
        self._result_title.pack_configure(ipady=5)
        self._result_placeholder.pack_configure(pady=2)

class Program():
    """
    Represents an entire program.
    """
    def __init__(self, name: str):
        # Program variables.
        self._name = os.getenv('CREATOR_NAME')
        self._button_corner_radius = 20
        self._window = ctk.CTk()
        self.name = name

        # Window components
        self._author = ctk.CTkLabel(
            master=self._window,
            text=f'Creado por: {self._name}'.upper(),
            font=ctk.CTkFont(family='Arial', weight='bold', size=10),
        )
        self._title = ctk.CTkLabel(
            master=self._window,
            text=self.name.upper(),
            font=ctk.CTkFont(family='Arial', size=20, weight='bold')
        )
        self._instruct = ctk.CTkLabel(
            master=self._window,
            text='Porfavor, seleccione un conversor.',
            font=ctk.CTkFont(family='Arial', size=16)
        )
        self._bin2dec_button = ctk.CTkButton(
            master=self._window,
            text='Binario a Decimal',
            command=self.binary_window,
            corner_radius=self._button_corner_radius
        )
        self._dec2bin_button = ctk.CTkButton(
            master=self._window,
            text='Decimal a Binario',
            command=self.decimal_window,
            corner_radius=self._button_corner_radius
        )
        self._exit_button = ctk.CTkButton(
            master=self._window,
            text='Salir',
            command=self.close,
            corner_radius=self._button_corner_radius
        )
        
        # Window settings.
        self._window.title(self.name)
        self._window.geometry('380x220')

    def binary_window(self):
        """
        Launches the binary to decimal conversion window.
        """
        window = BinaryConverter()
        window.init()
        return window
    
    def decimal_window(self):
        """
        Launches the decimal to binary conversion window.
        """
        window = DecimalConverter()
        window.init()
        return window

    def close(self):
        """
        Close the program window.
        """
        self._window.destroy()

    def init(self):
        """
        Starts the main loop for the program window.
        """
        self._pack()
        self._window.mainloop()

    def _pack(self):
        self._title.pack_configure(side='top', padx=10, pady=5)
        self._instruct.pack_configure(side='top', padx=10, pady=2)
        self._bin2dec_button.pack_configure(side='top', padx=10, pady=2)
        self._dec2bin_button.pack_configure(side='top', padx=10, pady=2)
        self._exit_button.pack_configure(side='top', padx=10, pady=2)
        self._author.pack_configure(side='top', padx=10, pady=5)
