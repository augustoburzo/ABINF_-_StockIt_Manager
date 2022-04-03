import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Ricerca Prodotto.ui"


class RicercaProdottoWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(RicercaProdottoWidget, self).__init__(master, **kw)
        self.menu1 = tk.Menu(self)
        self.submenu1 = tk.Menu(self.menu1, tearoff='false')
        self.menu1.add(tk.CASCADE, menu=self.submenu1, label='File')
        self.configure(menu=self.menu1)
        self.label1 = ttk.Label(self)
        self.label1.configure(background='#fff', font='{Bahnschrift} 12 {}', padding='10', text='Codice Prodotto')
        self.label1.grid(column='0', row='0', sticky='e')
        self.entry1 = ttk.Entry(self)
        self.entry1.configure(font='{Bahnschrift} 12 {bold}', state='readonly', width='10')
        self.entry1.grid(column='1', columnspan='3', row='0', sticky='w')
        self.label2 = ttk.Label(self)
        self.label2.configure(background='#fff', font='{Bahnschrift} 12 {}', padding='10', text='Quantità')
        self.label2.grid(column='4', row='0', sticky='e')
        self.entry2 = ttk.Entry(self)
        self.entry2.configure(font='{bahnschrift} 12 {}', width='3')
        self.entry2.grid(column='5', row='0', sticky='w')
        self.label3 = ttk.Label(self)
        self.label3.configure(background='#fff', font='{Bahnschrift} 12 {}', padding='10', text='Nome Prodotto')
        self.label3.grid(column='0', row='1', sticky='e')
        self.entry3 = ttk.Entry(self)
        self.entry3.configure(width='60')
        self.entry3.grid(column='1', columnspan='3', row='1')
        self.label4 = ttk.Label(self)
        self.label4.configure(background='#fff', font='{Bahnschrift} 12 {}', padding='10', text='Regime IVA')
        self.label4.grid(column='4', row='1', sticky='e')
        self.combobox1 = ttk.Combobox(self)
        self.combobox1.configure(width='10')
        self.combobox1.grid(column='5', row='1', sticky='w')
        self.configure(background='#fff', height='200', width='200')
        self.geometry('800x600')
        self.resizable(False, False)
        self.title('Inserisci prodotto')


if __name__ == '__main__':
    root = tk.Tk()
    widget = RicercaProdottoWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()


