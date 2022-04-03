import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Ricerca Prodotto.ui"


class RicercaProdottoWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(RicercaProdottoWidget, self).__init__(master, **kw)
        self.labelframe1 = tk.LabelFrame(self)
        self.lblNomeProdotto = tk.Label(self.labelframe1)
        self.lblNomeProdotto.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e',
                                       text='Nome prodotto:')
        self.lblNomeProdotto.grid(column='0', row='0')
        self.entryNomeProdotto = tk.Entry(self.labelframe1)
        self.entryNomeProdotto.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff',
                                         relief='flat')
        self.entryNomeProdotto.configure(takefocus=False, width='40')
        self.entryNomeProdotto.grid(column='1', columnspan='3', row='0')
        self.lblCode = tk.Label(self.labelframe1)
        self.lblCode.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', justify='left')
        self.lblCode.configure(text='Codice:')
        self.lblCode.grid(column='4', row='0')
        self.entryCodice = tk.Entry(self.labelframe1)
        self.entryCodice.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', relief='flat')
        self.entryCodice.configure(takefocus=False, width='15')
        self.entryCodice.grid(column='5', row='0')
        self.lblEAN = tk.Label(self.labelframe1)
        self.lblEAN.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', justify='left')
        self.lblEAN.configure(text='EAN:')
        self.lblEAN.grid(column='6', row='0')
        self.entryEAN = tk.Entry(self.labelframe1)
        self.entryEAN.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', relief='flat')
        self.entryEAN.configure(takefocus=False, width='19')
        self.entryEAN.grid(column='7', row='0')
        self.btnRicerca = tk.Button(self.labelframe1)
        self.btnRicerca.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3',
                                  font='{Bahnschrift} 12 {}')
        self.btnRicerca.configure(foreground='#fff', highlightbackground='#01509e', highlightcolor='#fff', padx='20')
        self.btnRicerca.configure(relief='flat', text='Ricerca')
        self.btnRicerca.grid(column='0', columnspan='8', padx='10', pady='10', row='1', sticky='ew')
        self.labelframe1.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.labelframe1.configure(relief='groove', text='Ricerca prodotto', width='1004')
        self.labelframe1.grid(column='0', padx='10', row='0', sticky='ew')
        self.labelframe1.rowconfigure('all', pad='10')
        self.labelframe1.columnconfigure('all', pad='20')
        self.frame1 = tk.Frame(self)
        self.mainBox = tk.Listbox(self.frame1)
        self.mainBox.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', height='17')
        self.mainBox.configure(relief='flat', width='110')
        self.mainBox.grid(column='0', row='0')
        self.frame1.configure(background='#fff', height='200', width='200')
        self.frame1.grid(column='0', padx='10', pady='10', row='1')
        self.frame2 = tk.Frame(self)
        self.btnModificaProdotto = tk.Button(self.frame2)
        self.btnModificaProdotto.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3',
                                           font='{Bahnschrift} 14 {}')
        self.btnModificaProdotto.configure(foreground='#fff', pady='30', relief='flat', text='Modifica prodotto')
        self.btnModificaProdotto.grid(column='0', columnspan='1', ipadx='10', padx='10', row='0', sticky='ew')
        self.btnModificaQuantita = tk.Button(self.frame2)
        self.btnModificaQuantita.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3',
                                           font='{Bahnschrift} 14 {}')
        self.btnModificaQuantita.configure(foreground='#fff', pady='30', relief='flat', text='Modifica quantità')
        self.btnModificaQuantita.grid(column='1', columnspan='1', ipadx='10', padx='10', row='0', sticky='ew')
        self.btnStampaElenco = tk.Button(self.frame2)
        self.btnStampaElenco.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3',
                                       font='{Bahnschrift} 14 {}')
        self.btnStampaElenco.configure(foreground='#fff', padx='7', pady='30', relief='flat')
        self.btnStampaElenco.configure(text='Stampa elenco')
        self.btnStampaElenco.grid(column='2', columnspan='1', ipadx='10', padx='10', row='0', sticky='ew')
        self.btnOrdinaProdotto = tk.Button(self.frame2)
        self.btnOrdinaProdotto.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3',
                                         font='{Bahnschrift} 14 {}')
        self.btnOrdinaProdotto.configure(foreground='#fff', padx='7', pady='30', relief='flat')
        self.btnOrdinaProdotto.configure(text='Ordina prodotto')
        self.btnOrdinaProdotto.grid(column='3', columnspan='1', ipadx='10', padx='10', row='0', sticky='ew')
        self.frame2.configure(background='#fff', width='1000')
        self.frame2.grid(column='0', padx='15', row='2', sticky='ew')
        self.frame2.grid_anchor('n')
        self.frame2.rowconfigure('all', pad='10')
        self.frame2.columnconfigure('all', pad='20')
        self.configure(background='#fff', height='200', highlightbackground='#01509e', highlightcolor='#fff')
        self.configure(width='200')
        self.geometry('1024x600')
        self.iconbitmap('search.ico')
        self.resizable(False, False)
        self.title('Ricerca Prodotto > AB Informatica - StockIt Manager')


if __name__ == '__main__':
    root = tk.Tk()
    widget = RicercaProdottoWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()
