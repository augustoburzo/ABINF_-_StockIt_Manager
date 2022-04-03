# This file is used for defining Ttk styles.
# Use the 'style' object to define styles.

# Pygubu Designer will need to know which style definition file you wish to use
# in your project.

# To specify a style definition file in Pygubu Designer:
# Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

# In Pygubu Designer:
# Assuming that you have specified a style definition file,
# - Use the 'style' combobox drop-down menu in Pygubu Designer to select a style that you have defined.
# - Changes made to the chosen style definition file will be automatically reflected in Pygubu Designer.
# ----------------------

# Example code:
style.configure('TLabel', background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', justify='left')
#style.configure('TEntry', background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', relief='flat')
style.configure('TFrame', background='#fff')
style.configure('TLabelFrame', background='#fff', relief='groove')