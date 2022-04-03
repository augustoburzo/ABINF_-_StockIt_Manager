import pathlib
import tkinter as tk
import tkinter.ttk as ttk

import guiMagazzino

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Master.ui"

class OrdineLiberoWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(OrdineLiberoWidget, self).__init__(master, **kw)
        self.frameInserisciOrdine = tk.LabelFrame(self)
        self.label1 = tk.Label(self.frameInserisciOrdine)
        self.label1.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Nome prodotto:')
        self.label1.grid(column='0', padx='10', row='0')
        self.entry1 = tk.Entry(self.frameInserisciOrdine)
        self.entry1.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entry1.grid(column='1', padx='10', row='0')
        self.label2 = tk.Label(self.frameInserisciOrdine)
        self.label2.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Quantità:')
        self.label2.grid(column='2', padx='10', row='0')
        self.entry2 = tk.Entry(self.frameInserisciOrdine)
        self.entry2.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='10')
        self.entry2.grid(column='3', padx='10', pady='10', row='0')
        self.label5 = tk.Label(self.frameInserisciOrdine)
        self.label5.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Note:')
        self.label5.grid(column='0', padx='10', row='1', sticky='e')
        self.entry3 = tk.Entry(self.frameInserisciOrdine)
        self.entry3.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entry3.grid(column='1', padx='10', row='1')
        self.label6 = tk.Label(self.frameInserisciOrdine)
        self.label6.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Cliente:')
        self.label6.grid(column='2', padx='10', row='1')
        self.entry4 = tk.Entry(self.frameInserisciOrdine)
        self.entry4.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entry4.grid(column='3', columnspan='3', padx='10', pady='10', row='1')
        self.label7 = tk.Label(self.frameInserisciOrdine)
        self.label7.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Destinazione:')
        self.label7.grid(column='4', padx='10', row='0')
        self.listbox2 = tk.Listbox(self.frameInserisciOrdine)
        self.listbox2.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', height='3')
        self.listbox2.configure(highlightbackground='#fff', highlightcolor='#01509e', width='14')
        self.listbox2.grid(column='5', padx='10', row='0')
        self.btnInserisciOrdine = tk.Button(self.frameInserisciOrdine)
        self.btnInserisciOrdine.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnInserisciOrdine.configure(foreground='#fff', highlightbackground='#01509e', highlightcolor='#fff', padx='20')
        self.btnInserisciOrdine.configure(relief='flat', text='Inserisci ordine')
        self.btnInserisciOrdine.grid(column='0', columnspan='8', padx='10', pady='10', row='2', sticky='ew')
        self.frameInserisciOrdine.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.frameInserisciOrdine.configure(text='Inserisci ordine', width='200')
        self.frameInserisciOrdine.grid(column='0', padx='10', row='0')
        self.labelframe1 = tk.LabelFrame(self)
        self.listbox1 = tk.Listbox(self.labelframe1)
        self.listbox1.configure(background='#01509e', font='{Bahnschrift} 12 {}', height='18', highlightbackground='#fff')
        self.listbox1.configure(highlightcolor='#01509e', width='110')
        self.listbox1.grid(column='0', padx='5', pady='5', row='0', sticky='ew')
        self.labelframe1.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.labelframe1.configure(text='Prodotti in ordine', width='200')
        self.labelframe1.grid(column='0', padx='10', row='1')
        self.configure(background='#fff', height='200', width='200')
        self.geometry('1024x600')
        self.resizable(False, False)
        self.title('Inserisci ordine libero > AB Informatica - StockIt Manager')

class OrdiniWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(OrdiniWidget, self).__init__(master, **kw)
        self.frameInOrdine = tk.LabelFrame(self)
        self.boxInOrdine = tk.Listbox(self.frameInOrdine)
        self.boxInOrdine.configure(background='#01509e', font='{Bahnschrift} 12 {}', height='8', highlightbackground='#fff')
        self.boxInOrdine.configure(highlightcolor='#01509e', width='90')
        self.boxInOrdine.grid(column='0', padx='5', pady='5', row='0', sticky='ew')
        self.frameInOrdine.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.frameInOrdine.configure(text='Prodotti in ordine', width='200')
        self.frameInOrdine.grid(column='0', padx='10', row='0')
        self.frameInConsegna = tk.LabelFrame(self)
        self.boxInConsegna = tk.Listbox(self.frameInConsegna)
        self.boxInConsegna.configure(background='#01509e', font='{Bahnschrift} 12 {}', height='8', highlightbackground='#fff')
        self.boxInConsegna.configure(highlightcolor='#01509e', width='90')
        self.boxInConsegna.grid(column='0', padx='5', pady='5', row='0', sticky='ew')
        self.frameInConsegna.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.frameInConsegna.configure(text='Prodotti in consegna', width='200')
        self.frameInConsegna.grid(column='0', padx='10', row='1')
        self.frameRicevuti = tk.LabelFrame(self)
        self.boxRicevuti = tk.Listbox(self.frameRicevuti)
        self.boxRicevuti.configure(background='#01509e', font='{Bahnschrift} 12 {}', height='8', highlightbackground='#fff')
        self.boxRicevuti.configure(highlightcolor='#01509e', width='90')
        self.boxRicevuti.grid(column='0', padx='5', pady='5', row='0', sticky='ew')
        self.frameRicevuti.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.frameRicevuti.configure(text='Prodotti ricevuti', width='200')
        self.frameRicevuti.grid(column='0', padx='10', row='2')
        self.frameButtons = tk.Frame(self)
        self.btnOrdineMagazzino = tk.Button(self.frameButtons)
        self.btnOrdineMagazzino.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnOrdineMagazzino.configure(foreground='#fff', pady='15', relief='flat', text='Ordine magazzino')
        self.btnOrdineMagazzino.grid(column='0', padx='10', row='0', sticky='ew')
        self.btnOrdineMagazzino.configure(command=self.ordineMagazzino)
        self.btnOrdineLibero = tk.Button(self.frameButtons)
        self.btnOrdineLibero.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnOrdineLibero.configure(foreground='#fff', pady='15', relief='flat', text='Ordine libero')
        self.btnOrdineLibero.grid(column='0', padx='10', row='1', sticky='ew')
        self.btnOrdineLibero.configure(command=self.ordineLibero)
        self.btnInConsegna = tk.Button(self.frameButtons)
        self.btnInConsegna.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnInConsegna.configure(foreground='#fff', pady='15', relief='flat', text='Metti in consegna')
        self.btnInConsegna.grid(column='0', padx='10', row='2', sticky='ew')
        self.btnInConsegna.configure(command=self.inConsegna)
        self.btnConsegnato = tk.Button(self.frameButtons)
        self.btnConsegnato.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnConsegnato.configure(foreground='#fff', pady='15', relief='flat', text='Consegnato')
        self.btnConsegnato.grid(column='0', padx='10', row='3', sticky='ew')
        self.btnConsegnato.configure(command=self.consegnato)
        self.btnEliminaOrdine = tk.Button(self.frameButtons)
        self.btnEliminaOrdine.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnEliminaOrdine.configure(foreground='#fff', pady='15', relief='flat', text='Elimina ordine')
        self.btnEliminaOrdine.grid(column='0', padx='10', row='4', sticky='ew')
        self.btnEliminaOrdine.configure(command=self.eliminaOrdine)
        self.btnTuttiInConsegna = tk.Button(self.frameButtons)
        self.btnTuttiInConsegna.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnTuttiInConsegna.configure(foreground='#fff', pady='15', relief='flat', text='Tutti in consegna')
        self.btnTuttiInConsegna.grid(column='0', padx='10', row='5', sticky='ew')
        self.btnTuttiInConsegna.configure(command=self.tuttiInConsegna)
        self.btnTuttiConsegnati = tk.Button(self.frameButtons)
        self.btnTuttiConsegnati.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnTuttiConsegnati.configure(foreground='#fff', pady='15', relief='flat', text='Tutti consegnati')
        self.btnTuttiConsegnati.grid(column='0', padx='10', row='6', sticky='ew')
        self.btnTuttiConsegnati.configure(command=self.tuttiConsegnati)
        self.btnRimettiConsegna = tk.Button(self.frameButtons)
        self.btnRimettiConsegna.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnRimettiConsegna.configure(foreground='#fff', pady='15', relief='flat', text='Rimetti in consegna')
        self.btnRimettiConsegna.grid(column='0', padx='10', row='7', sticky='ew')
        self.btnRimettiConsegna.configure(command=self.rimettiConsegna)
        self.btnSvuota = tk.Button(self.frameButtons)
        self.btnSvuota.configure(activebackground='#016ad3', activeforeground='#eee', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnSvuota.configure(foreground='#fff', pady='15', relief='flat', text='Svuota ricevuti')
        self.btnSvuota.grid(column='0', padx='10', row='8', sticky='ew')
        self.btnSvuota.configure(command=self.svuotaRicevuti)
        self.frameButtons.configure(background='#fff', height='200', width='160')
        self.frameButtons.grid(column='1', pady='10', row='0', rowspan='3', sticky='ns')
        self.frameButtons.rowconfigure('all', pad='3')
        self.configure(background='#fff', height='200', width='200')
        self.geometry('1024x600')
        self.iconbitmap('barcode.ico')
        self.resizable(False, False)
        self.title('Ordini > AB Informatica - StockIt Manager')

    def ordineMagazzino(self):
        guiMagazzino.RicercaProdottoWidget()

    def ordineLibero(self):
        OrdineLiberoWidget()

    def inConsegna(self):
        pass

    def consegnato(self):
        pass

    def eliminaOrdine(self):
        pass

    def tuttiInConsegna(self):
        pass

    def tuttiConsegnati(self):
        pass

    def rimettiConsegna(self):
        pass

    def svuotaRicevuti(self):
        pass


