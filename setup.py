from cx_Freeze import setup, Executable
import sys

# Inclua os pacotes adicionais necessários
packages = ["tkinter", "customtkinter", "pyperclip"]

# Determina o base para o executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Isso é usado para aplicações com GUI

# Configuração do executável
executables = [
    Executable(
        script="main1.py",  # Substitua por seu script Python
        base=base,
        target_name="Selector.exe"  # Nome do executável gerado
    )
]

# Configuração do setup
setup(
    name="MeuSelectorDeCores",
    version="1.0",
    description="Meu Selector de Cores em Tkinter",
    options={
        "build_exe": {
            "packages": packages,
            "include_files": []
        }
    },
    executables=executables
)
