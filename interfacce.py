import pathlib
import tkinter as tk
from tkinter import messagebox, END
import tkinter.ttk as ttk


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

class OrdineLiberoWidget(tk.Toplevel):
    def __init__(self, master=None):
        # build ui
        self.toplevelOrdineLibero = tk.Tk() if master is None else tk.Toplevel(master)
        self.frameInserisciOrdine = tk.LabelFrame(self.toplevelOrdineLibero)
        self.labelNomeProdotto = tk.Label(self.frameInserisciOrdine)
        self.labelNomeProdotto.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Nome prodotto:')
        self.labelNomeProdotto.grid(column='0', padx='10', row='0')
        self.entryNomeProdotto = tk.Entry(self.frameInserisciOrdine)
        self.entryNomeProdotto.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entryNomeProdotto.grid(column='1', padx='10', row='0')
        self.labelQnty = tk.Label(self.frameInserisciOrdine)
        self.labelQnty.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Quantità:')
        self.labelQnty.grid(column='2', padx='10', row='0')
        self.entryQntyProdotto = tk.Entry(self.frameInserisciOrdine)
        self.entryQntyProdotto.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='10')
        self.entryQntyProdotto.grid(column='3', padx='10', pady='10', row='0')
        self.labelNote = tk.Label(self.frameInserisciOrdine)
        self.labelNote.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Note:')
        self.labelNote.grid(column='0', padx='10', row='1', sticky='e')
        self.entryNote = tk.Entry(self.frameInserisciOrdine)
        self.entryNote.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entryNote.grid(column='1', padx='10', row='1')
        self.labelCliente = tk.Label(self.frameInserisciOrdine)
        self.labelCliente.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Cliente:')
        self.labelCliente.grid(column='2', padx='10', row='1')
        self.entryCliente = tk.Entry(self.frameInserisciOrdine)
        self.entryCliente.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', width='40')
        self.entryCliente.grid(column='3', columnspan='3', padx='10', pady='10', row='1')
        self.labelDestinazione = tk.Label(self.frameInserisciOrdine)
        self.labelDestinazione.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', text='Destinazione:')
        self.labelDestinazione.grid(column='4', padx='10', row='0')
        self.lbDestinazione = tk.Listbox(self.frameInserisciOrdine)
        self.lbDestinazione.configure(background='#01509e', font='{Bahnschrift} 12 {}', foreground='#fff', height='3')
        self.lbDestinazione.configure(highlightbackground='#fff', highlightcolor='#01509e', width='14')
        self.lbDestinazione.grid(column='5', padx='10', row='0')
        self.btnInserisciOrdine = tk.Button(self.frameInserisciOrdine)
        self.btnInserisciOrdine.configure(activebackground='#016ad3', activeforeground='#aaa', background='#016ad3', font='{Bahnschrift} 12 {}')
        self.btnInserisciOrdine.configure(foreground='#fff', highlightbackground='#01509e', highlightcolor='#fff', padx='20')
        self.btnInserisciOrdine.configure(relief='flat', text='Inserisci ordine')
        self.btnInserisciOrdine.grid(column='0', columnspan='8', padx='10', pady='10', row='2', sticky='ew')
        self.btnInserisciOrdine.configure(command=self.inserisciOrdine)
        self.frameInserisciOrdine.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.frameInserisciOrdine.configure(text='Inserisci ordine', width='200')
        self.frameInserisciOrdine.grid(column='0', padx='10', row='0')
        self.labelframe1 = tk.LabelFrame(self.toplevelOrdineLibero)
        self.lbProdottiInOrdine = tk.Listbox(self.labelframe1)
        self.lbProdottiInOrdine.configure(background='#01509e', font='{Bahnschrift} 12 {}', height='18', highlightbackground='#fff')
        self.lbProdottiInOrdine.configure(highlightcolor='#01509e', width='110')
        self.lbProdottiInOrdine.grid(column='0', padx='5', pady='5', row='0', sticky='ew')
        self.labelframe1.configure(background='#fff', font='{Bahnschrift} 12 {}', foreground='#01509e', height='200')
        self.labelframe1.configure(text='Prodotti in ordine', width='200')
        self.labelframe1.grid(column='0', padx='10', row='1')
        self.toplevelOrdineLibero.configure(background='#fff', height='200', width='200')
        self.toplevelOrdineLibero.geometry('1024x600')
        self.toplevelOrdineLibero.resizable(False, False)
        self.toplevelOrdineLibero.title('Inserisci ordine libero > AB Informatica - StockIt Manager')

        # Main widget
        self.mainwindow = self.toplevelOrdineLibero

    def inserisciOrdine(self):
        #Generazione variabili
        self.nomeProdottoInOrdine = self.entryNomeProdotto.get()
        self.qntyProdottoInOrdine = self.entryQntyProdotto.get()
        self.noteProdottoInOrdine = self.entryNote.get()
        self.clienteProdottoInOrdine = self.entryCliente.get()
        self.magazzinoProdottoInOrdine = self.lbDestinazione.focus_get()

        #Controllo dei campi, se non popolati generano errore
        if self.nomeProdottoInOrdine == "":
            tk.messagebox.showerror(title="Campi incompleti", message="Completa tutti i campi richiesti!")
        else:
            #Dove scrivere i dati raccolti dalla maschera
            print(self.nomeProdottoInOrdine+" "+self.qntyProdottoInOrdine+" "+self.noteProdottoInOrdine+" "
                  +self.clienteProdottoInOrdine)
            #############################################

            #Ripulisci interfaccia
            self.entryNomeProdotto.delete(0, END)
            self.entryQntyProdotto.delete(0, END)
            self.entryNote.delete(0, END)
            self.entryCliente.delete(0, END)


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
        RicercaProdottoWidget()

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


