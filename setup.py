from cx_Freeze import setup, Executable

# List of executables and their configurations
executables = [
    Executable('main.py', base=None)  # Replace 'your_script.py' with your main Python script
]

# Setup configuration
setup(
    name='main64',
    version='1.0',
    description='Your application description',
    executables=executables
)
