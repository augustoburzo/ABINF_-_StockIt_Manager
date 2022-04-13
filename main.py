import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, NO, YES
import mysql.connector
from fpdf import FPDF
import tkinter.simpledialog
import tkinter.messagebox
from datetime import date

import databaseOperations

columnsOrdini = ('numOrdine', 'nomeProdotto', 'quantita', 'note', 'nomeCliente', 'puntoVendita')
columnsComunicazioni = ('numComunicazione', 'autore', 'messaggio', 'data')
columnsAssistenza = ('numAssistenza', 'nomeCliente', 'contattoCliente', 'prodotto', 'difettoProdotto', 'dataConsegna',
                     'note', 'statoPratica')

#FINESTRA CHAT#########################################################################################################

class ChatWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(ChatWidget, self).__init__(master, **kw)
        self.lfChat = ttk.Labelframe(self)
        self.lbChat = tk.Listbox(self.lfChat)
        self.lbChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lbChat.bind('<Double-1>', self.rispondi, add='')
        self.lfChat.configure(height='200', text='Chat utenti', width='200')
        self.lfChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frmNuovoMessaggio = ttk.Frame(self)
        self.frmBoxTesto = ttk.Frame(self.frmNuovoMessaggio)
        self.textMessaggio = tk.Text(self.frmBoxTesto)
        self.textMessaggio.configure(height='6', width='50')
        self.textMessaggio.pack(expand='true', fill='x', pady='5', side='top')
        self.textMessaggio.bind('<Return>', self.inviaMessaggio, add='')
        self.frmBoxTesto.configure(height='100', width='200')
        self.frmBoxTesto.pack(expand='true', fill='x', side='left')
        self.frmButton = ttk.Frame(self.frmNuovoMessaggio)
        self.btnInviaMessaggio = ttk.Button(self.frmButton)
        self.img_send = tk.PhotoImage(file='send.png')
        self.btnInviaMessaggio.configure(image=self.img_send, text='Invia')
        self.btnInviaMessaggio.pack(expand='true', fill='y', pady='5', side='top')
        self.btnInviaMessaggio.configure(command=self.inviaMessaggio)
        self.frmButton.configure(height='100', width='100')
        self.frmButton.pack(expand='true', fill='y', side='top')
        self.frmNuovoMessaggio.configure(height='100', width='200')
        self.frmNuovoMessaggio.pack(fill='x', padx='5', side='top')
        self.configure(height='200', width='200')
        self.geometry('800x600')

    def rispondi(self, event=None):
        pass

    def inviaMessaggio(self, event=None):
        pass


#FINESTRA UTENTI#######################################################################################################

class UtentiWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(UtentiWidget, self).__init__(master, **kw)
        self.lfInserisciUtente = ttk.Labelframe(self)
        self.frmLbl = ttk.Frame(self.lfInserisciUtente)
        self.lblNomeUtente = ttk.Label(self.frmLbl)
        self.lblNomeUtente.configure(text='Nome utente:')
        self.lblNomeUtente.pack(anchor='e', side='top')
        self.lblPassword = ttk.Label(self.frmLbl)
        self.lblPassword.configure(text='Password:')
        self.lblPassword.pack(anchor='e', pady='1', side='top')
        self.lblRuolo = ttk.Label(self.frmLbl)
        self.lblRuolo.configure(text='Ruolo:')
        self.lblRuolo.pack(anchor='e', pady='1', side='top')
        self.lblPuntoVendita = ttk.Label(self.frmLbl)
        self.lblPuntoVendita.configure(text='Punto vendita:')
        self.lblPuntoVendita.pack(anchor='e', pady='1', side='top')
        self.frmLbl.configure(height='200', width='200')
        self.frmLbl.pack(fill='y', padx='5', pady='5', side='left')
        self.frmEntry = ttk.Frame(self.lfInserisciUtente)
        self.entryNomeUtente = ttk.Entry(self.frmEntry)
        self.entryNomeUtente.pack(fill='x', side='top')
        self.entryPassword = ttk.Entry(self.frmEntry)
        self.entryPassword.pack(fill='x', side='top')
        self.comboRuolo = ttk.Combobox(self.frmEntry)
        self.comboRuolo.configure(values='operatore manager master')
        self.comboRuolo.pack(fill='x', side='top')
        self.entryPuntoVendita = ttk.Entry(self.frmEntry)
        self.entryPuntoVendita.pack(fill='x', side='top')
        self.frmEntry.configure(height='200', width='200')
        self.frmEntry.pack(fill='both', padx='5', pady='5', side='top')
        self.lfInserisciUtente.configure(height='200', text='Inserisci o modifica utente', width='200')
        self.lfInserisciUtente.pack(anchor='n', expand='false', fill='x', padx='5', pady='5', side='top')
        self.lfUtenti = ttk.Labelframe(self)
        self.tblUtenti_cols = ['idx', 'nomeUtente', 'password', 'ruolo', 'puntoVendita']
        self.tblUtenti_dcols = ['idx', 'nomeUtente', 'password', 'ruolo', 'puntoVendita']
        self.tblUtenti = ttk.Treeview(self.lfUtenti, columns=self.tblUtenti_cols, show='headings')
        self.tblUtenti.column('idx', anchor='w',stretch='false',width='67',minwidth='20')
        self.tblUtenti.column('nomeUtente', anchor='w',stretch='true',width='200',minwidth='20')
        self.tblUtenti.column('password', anchor='w',stretch='true',width='200',minwidth='20')
        self.tblUtenti.column('ruolo', anchor='w',stretch='false',width='100',minwidth='20')
        self.tblUtenti.column('puntoVendita', anchor='w',stretch='false',width='200',minwidth='20')
        self.tblUtenti.heading('idx', anchor='w',text='Prog.')
        self.tblUtenti.heading('nomeUtente', anchor='w',text='Nome utente')
        self.tblUtenti.heading('password', anchor='w',text='Password')
        self.tblUtenti.heading('ruolo', anchor='w',text='Ruolo')
        self.tblUtenti.heading('puntoVendita', anchor='w',text='Punto Vendita')
        self.tblUtenti.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.tblUtenti.bind('<Double-1>', self.OnClickTbl, add='')
        self.lfUtenti.configure(height='200', text='Utenti', width='200')
        self.lfUtenti.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame7 = ttk.Frame(self)
        self.button1 = ttk.Button(self.frame7)
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.button1.configure(image=self.img_plus, text='button1', command=self.inserisciUtente)
        self.button1.pack(padx='5', pady='5', side='right')
        self.button3 = ttk.Button(self.frame7)
        self.img_clean = tk.PhotoImage(file='clean.png')
        self.button3.configure(image=self.img_clean, text='button1', command=self.svuotaCampi)
        self.button3.pack(padx='5', pady='5', side='right')
        self.button4 = ttk.Button(self.frame7)
        self.img_delete = tk.PhotoImage(file='delete.png')
        self.button4.configure(image=self.img_delete, text='button1', command=self.eliminaUtente)
        self.button4.pack(padx='5', pady='5', side='right')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(fill='x', side='top')
        self.configure(height='200', width='200')
        self.geometry('800x600')

        self.aggiornaUtenti()

    def inserisciUtente(self):
        utenteNomeUtente = self.entryNomeUtente.get()
        utentePassword = self.entryPassword.get()
        utenteRuolo = self.comboRuolo.get()
        utentePuntoVendita = self.entryPuntoVendita.get()

        databaseOperations.Utenti(0, 0, utenteNomeUtente, utentePassword, utenteRuolo, utentePuntoVendita)

        self.entryNomeUtente.delete(0, END)
        self.entryPassword.delete(0, END)
        self.comboRuolo.delete(0, END)
        self.entryPuntoVendita.delete(0, END)

        self.aggiornaUtenti()

    def svuotaCampi(self):
        self.entryNomeUtente.delete(0, END)
        self.entryPassword.delete(0, END)
        self.comboRuolo.delete(0, END)
        self.entryPuntoVendita.delete(0, END)

    def eliminaUtente(self):
        indice = self.tblUtenti.focus()
        idx = self.tblUtenti.item(indice)
        valore = idx['values'][0]
        databaseOperations.Utenti(1, valore, nomeUtente='', password='', ruolo='', puntoVendita='')
        self.aggiornaUtenti()

    def OnClickTbl(self, event):
        indice = self.tblUtenti.focus()
        idx = self.tblUtenti.item(indice)
        valore = idx['values'][0]
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        _searchSQL = "SELECT * FROM users WHERE idx = '%s';"
        self.cursor.execute(_searchSQL, (valore,))
        utente = self.cursor.fetchone()

        self.entryNomeUtente.delete(0, END)
        self.entryPassword.delete(0, END)
        self.comboRuolo.delete(0, END)
        self.entryPuntoVendita.delete(0, END)

        self.entryNomeUtente.insert(0, utente[1])
        self.entryPassword.insert(0, utente[2])
        self.comboRuolo.insert(0, utente[3])
        self.entryPuntoVendita.insert(0, utente[4])

    def aggiornaUtenti(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM users")
        utenti = self.cursor.fetchall()

        self.tblUtenti.delete(*self.tblUtenti.get_children())

        for utente in utenti:
            self.tblUtenti.insert("", END, values=utente)

#FINESTRA NUOVA COMUNICAZIONE##########################################################################################

class NuovaComunicazioneWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(NuovaComunicazioneWidget, self).__init__(master, **kw)
        self.lfNuovaComunicazione = ttk.Labelframe(self)
        self.text1 = tk.Text(self.lfNuovaComunicazione)
        self.text1.configure(height='10', state='normal', width='50')
        self.text1.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lfNuovaComunicazione.configure(height='200', text='Nuova comunicazione', width='200')
        self.lfNuovaComunicazione.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frmPulsanti = ttk.Frame(self)
        self.btnComInserisciComunicazione = ttk.Button(self.frmPulsanti)
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.btnComInserisciComunicazione.configure(image=self.img_plus, text='Inserisci comunicazione')
        self.btnComInserisciComunicazione.pack(padx='5', pady='5', side='right')
        self.btnComInserisciComunicazione.configure(command=self.inserisciComunicazione)
        self.btnComSvuotaCampi = ttk.Button(self.frmPulsanti)
        self.img_clean = tk.PhotoImage(file='clean.png')
        self.btnComSvuotaCampi.configure(image=self.img_clean, text='Svuota campi')
        self.btnComSvuotaCampi.pack(padx='5', pady='5', side='right')
        self.btnComSvuotaCampi.configure(command=self.svuotaCampi)
        self.frmPulsanti.configure(height='70', width='200')
        self.frmPulsanti.pack(expand='false', fill='x', side='top')
        self.configure(height='200', takefocus=True, width='200')
        self.geometry('800x600')

    def inserisciComunicazione(self):
        messaggio = self.text1.get(1.0, END)
        data = str(date.today())
        databaseOperations.Comunicazioni(0,0,nomeUtente,messaggio,data)
        self.svuotaCampi()
        self.destroy()

    def svuotaCampi(self):
        self.text1.delete(1.0, END)


# FINESTRA ASSISTENZA###################################################################################################


class AssistenzaWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(AssistenzaWidget, self).__init__(master, **kw)
        self.lfNuovaPratica = ttk.Labelframe(self)
        self.frameAssLabel = ttk.Frame(self.lfNuovaPratica)
        self.lblAssNomeCliente = ttk.Label(self.frameAssLabel)
        self.lblAssNomeCliente.configure(text='Nome cliente:')
        self.lblAssNomeCliente.pack(anchor='e', expand='true', side='top')
        self.lblAssContattoCliente = ttk.Label(self.frameAssLabel)
        self.lblAssContattoCliente.configure(text='Contatto cliente:')
        self.lblAssContattoCliente.pack(anchor='e', expand='true', side='top')
        self.lblAssProdotto = ttk.Label(self.frameAssLabel)
        self.lblAssProdotto.configure(text='Prodotto:')
        self.lblAssProdotto.pack(anchor='e', expand='true', side='top')
        self.lblAssDifetto = ttk.Label(self.frameAssLabel)
        self.lblAssDifetto.configure(text='Difetto riscontrato:')
        self.lblAssDifetto.pack(anchor='e', expand='true', side='top')
        self.lblAssNote = ttk.Label(self.frameAssLabel)
        self.lblAssNote.configure(padding='5', text='Note:')
        self.lblAssNote.pack(anchor='e', expand='false', ipady='70', side='top')
        self.frameAssLabel.configure(width='200')
        self.frameAssLabel.pack(expand='false', fill='y', padx='5', pady='5', side='left')
        self.frameEntryAss = ttk.Frame(self.lfNuovaPratica)
        self.entryAssNomeCliente = ttk.Entry(self.frameEntryAss)
        self.entryAssNomeCliente.configure(width='60')
        self.entryAssNomeCliente.pack(expand='true', fill='x', side='top')
        self.entryAssContattoCliente = ttk.Entry(self.frameEntryAss)
        self.entryAssContattoCliente.configure(width='60')
        self.entryAssContattoCliente.pack(expand='true', fill='x', side='top')
        self.entryAssProdotto = ttk.Entry(self.frameEntryAss)
        self.entryAssProdotto.configure(width='60')
        self.entryAssProdotto.pack(expand='true', fill='x', side='top')
        self.entryAssDifetto = ttk.Entry(self.frameEntryAss)
        self.entryAssDifetto.configure(width='60')
        self.entryAssDifetto.pack(expand='true', fill='x', side='top')
        self.textAssNote = tk.Text(self.frameEntryAss)
        self.textAssNote.configure(height='10', width='35')
        self.textAssNote.pack(expand='true', fill='both', side='top')
        self.frameEntryAss.configure(height='200', width='200')
        self.frameEntryAss.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.btnNuovaAssistenza = ttk.Button(self.lfNuovaPratica)
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.btnNuovaAssistenza.configure(image=self.img_plus, text='Inserisci')
        self.btnNuovaAssistenza.pack(expand='true', padx='5', pady='5', side='top')
        self.btnNuovaAssistenza.configure(command=self.nuovaAssistenza)
        self.vuoto1 = ttk.Frame(self.lfNuovaPratica)
        self.vuoto1.configure(height='185', width='64')
        self.vuoto1.pack(side='top')
        self.lfNuovaPratica.configure(height='200', text='Nuova Pratica Assistenza', width='200')
        self.lfNuovaPratica.pack(expand='false', fill='x', padx='5', pady='5', side='top')
        self.lfPraticheInCorso = ttk.Labelframe(self)
        self.treeview1 = ttk.Treeview(self.lfPraticheInCorso, columns=columnsAssistenza, show='headings')
        self.treeview1.pack(expand='true', fill='both', side='top')
        self.treeview1.heading('numAssistenza', text='Prog.')
        self.treeview1.column(0, width=40, stretch=NO)
        self.treeview1.heading('nomeCliente', text='Nome cliente')
        self.treeview1.heading('contattoCliente', text='Contatto cliente')
        self.treeview1.heading('prodotto', text='Prodotto')
        self.treeview1.heading('difettoProdotto', text='Difetto riscontrato')
        self.treeview1.heading('dataConsegna', text='Data di consegna')
        self.treeview1.column(5, width=100, stretch=NO)
        self.treeview1.heading('note', text='Note')
        self.treeview1.heading('statoPratica', text='Stato pratica')
        self.lfPraticheInCorso.configure(height='200', text='Pratiche in corso', width='200')
        self.lfPraticheInCorso.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame3 = ttk.Frame(self)
        self.btnInLavorazione = ttk.Button(self.frame3)
        self.btnInLavorazione.configure(text='Pratica in lavorazione')
        self.btnInLavorazione.pack(expand='true', fill='x', side='left')
        self.btnInLavorazione.configure(command=self.praticaLavorazione)
        self.btnPraticaLavorata = ttk.Button(self.frame3)
        self.btnPraticaLavorata.configure(text='Pratica lavorata')
        self.btnPraticaLavorata.pack(expand='true', fill='x', side='left')
        self.btnPraticaLavorata.configure(command=self.praticaLavorata)
        self.btnPraticaRestituita = ttk.Button(self.frame3)
        self.btnPraticaRestituita.configure(text='Pratica restituita')
        self.btnPraticaRestituita.pack(expand='true', fill='x', side='left')
        self.btnPraticaRestituita.configure(command=self.praticaRestituita)
        if operatore == 'manager' or 'master':
            self.btnEliminaPratica = ttk.Button(self.frame3)
            self.btnEliminaPratica.configure(text='Elimina pratica')
            self.btnEliminaPratica.pack(expand='true', fill='x', side='left')
            self.btnEliminaPratica.configure(command=self.eliminaPratica)
        self.frame3.configure(height='200', width='200')
        self.frame3.pack(fill='x', padx='5', side='top')
        self.sizegrip3 = ttk.Sizegrip(self)
        self.sizegrip3.pack(anchor='se', side='top')
        self.configure(height='200', width='200')
        self.geometry('800x600')
        self.minsize(1360, 680)
        # self.state('zoomed')
        self.title('Gestione Assistenza | AB Informatica - StockIt Manager')

        self.aggiornamentoOrdini()

    def nuovaAssistenza(self):
        self.nomeCliente = self.entryAssNomeCliente.get()
        self.nomeCliente = self.nomeCliente + " - P. vendita: " + puntoVendita
        self.contattoCliente = self.entryAssContattoCliente.get()
        self.prodotto = self.entryAssProdotto.get()
        self.difettoProdotto = self.entryAssDifetto.get()
        self.note = self.textAssNote.get(1.0, END)
        self.data = date.today()

        # INSERISCE I DATI NEL DATABASE
        databaseOperations.GestioneAssistenza(0, 0, nomeCliente=self.nomeCliente, contattoCliente=self.contattoCliente,
                                              prodotto=self.prodotto, difettoProdotto=self.difettoProdotto,
                                              note=self.note, dataConsegna=self.data)

        # AGGIORNA LA TABELLA ASSISTENZE
        self.aggiornamentoOrdini()

        # AZZERA I CAMPI
        self.entryAssNomeCliente.delete(0, END)
        self.entryAssContattoCliente.delete(0, END)
        self.entryAssProdotto.delete(0, END)
        self.entryAssDifetto.delete(0, END)
        self.textAssNote.delete(1.0, END)

    def praticaLavorazione(self):
        indice = self.treeview1.focus()
        idx = self.treeview1.item(indice)
        valore = idx['values'][0]
        databaseOperations.GestioneAssistenza(1, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.aggiornamentoOrdini()

    def praticaLavorata(self):
        indice = self.treeview1.focus()
        idx = self.treeview1.item(indice)
        valore = idx['values'][0]
        databaseOperations.GestioneAssistenza(2, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.aggiornamentoOrdini()

    def praticaRestituita(self):
        indice = self.treeview1.focus()
        idx = self.treeview1.item(indice)
        valore = idx['values'][0]
        databaseOperations.GestioneAssistenza(3, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.aggiornamentoOrdini()

    def eliminaPratica(self):
        indice = self.treeview1.focus()
        idx = self.treeview1.item(indice)
        valore = idx['values'][0]
        databaseOperations.GestioneAssistenza(4, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.aggiornamentoOrdini()

    def aggiornamentoOrdini(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM assistenzaProdotti")
        ordini = self.cursor.fetchall()

        # PULISCE TABELLA
        self.treeview1.delete(*self.treeview1.get_children())

        for ordine in ordini:
            self.treeview1.insert("", END, values=ordine)


# FINESTRA ORDINI#######################################################################################################
class OrdiniWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):

        super(OrdiniWidget, self).__init__(master, **kw)  # INIZIO BUILD INTERFACCIA ORDINI
        self.lfNuovoOrdine = ttk.Labelframe(self)
        self.frameLabelOrdine = ttk.Frame(self.lfNuovoOrdine)
        self.lblOrdNomeProdotto = ttk.Label(self.frameLabelOrdine)
        self.lblOrdNomeProdotto.configure(text='Nome prodotto:')
        self.lblOrdNomeProdotto.pack(anchor='e', expand='true', side='top')
        self.lblOrdQuantita = ttk.Label(self.frameLabelOrdine)
        self.lblOrdQuantita.configure(text='Quantità:')
        self.lblOrdQuantita.pack(anchor='e', expand='true', side='top')
        self.lblOrdNote = ttk.Label(self.frameLabelOrdine)
        self.lblOrdNote.configure(text='Note:')
        self.lblOrdNote.pack(anchor='e', expand='true', side='top')
        self.lblNomeCliente = ttk.Label(self.frameLabelOrdine)
        self.lblNomeCliente.configure(text='Nome cliente:')
        self.lblNomeCliente.pack(anchor='e', expand='true', side='top')
        self.frameLabelOrdine.configure(width='200')
        self.frameLabelOrdine.pack(expand='false', fill='y', padx='5', pady='5', side='left')
        self.frameEntryOrdine = ttk.Frame(self.lfNuovoOrdine)
        self.entryNomeProdotto = ttk.Entry(self.frameEntryOrdine)
        self.entryNomeProdotto.configure(width='60')
        self.entryNomeProdotto.pack(expand='true', fill='x', side='top')
        self.entryQuantita = ttk.Entry(self.frameEntryOrdine)
        self.entryQuantita.configure(width='60')
        self.entryQuantita.pack(expand='true', fill='x', side='top')
        self.entryNoteProdotto = ttk.Entry(self.frameEntryOrdine)
        self.entryNoteProdotto.configure(width='60')
        self.entryNoteProdotto.pack(expand='true', fill='x', side='top')
        self.entryNomeCliente = ttk.Entry(self.frameEntryOrdine)
        self.entryNomeCliente.configure(width='60')
        self.entryNomeCliente.pack(expand='true', fill='x', side='top')
        self.frameEntryOrdine.configure(height='200', width='200')
        self.frameEntryOrdine.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.btnNuovoOrdine = ttk.Button(self.lfNuovoOrdine)
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.btnNuovoOrdine.configure(image=self.img_plus, text='Inserisci')
        self.btnNuovoOrdine.pack(expand='true', fill='y', padx='5', pady='5', side='top')
        self.btnNuovoOrdine.configure(command=self.nuovoOrdine)
        self.lfNuovoOrdine.configure(height='200', text='Nuovo Ordine', width='200')
        self.lfNuovoOrdine.pack(expand='false', fill='x', padx='5', pady='5', side='top')
        self.lfNuoviOrdini = ttk.Labelframe(self)

        # TABELLA ORDINI DA EVADERE E DEFINIZIONI#######################################################################
        self.tblOrdiniDaEvadere = ttk.Treeview(self.lfNuoviOrdini, columns=columnsOrdini, show='headings')
        self.tblOrdiniDaEvadere.pack(expand='true', fill='both', side='top')
        self.tblOrdiniDaEvadere.heading('numOrdine', text='Prog.')
        self.tblOrdiniDaEvadere.column(0, width=40, stretch=NO)
        self.tblOrdiniDaEvadere.heading('nomeProdotto', text='Nome Prodotto')
        self.tblOrdiniDaEvadere.heading('quantita', text='Quantità')
        self.tblOrdiniDaEvadere.column(2, width=67, stretch=NO)
        self.tblOrdiniDaEvadere.heading('note', text='Note')
        self.tblOrdiniDaEvadere.column(3, width=100, stretch=YES)
        self.tblOrdiniDaEvadere.heading('nomeCliente', text='Nome cliente')
        self.tblOrdiniDaEvadere.column(4, width=300, stretch=NO)
        self.tblOrdiniDaEvadere.heading('puntoVendita', text='Punto Vendita')
        self.tblOrdiniDaEvadere.column(5, width=300, stretch=NO)
        ################################################################################################################

        self.lfNuoviOrdini.configure(height='200', text='Ordini da evadere', width='200')
        self.lfNuoviOrdini.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lfOrdiniEvasi = ttk.Labelframe(self)

        # TABELLA ORDINI EVASI##########################################################################################
        self.tblOrdiniEvasi = ttk.Treeview(self.lfOrdiniEvasi, columns=columnsOrdini, show='headings')
        self.tblOrdiniEvasi.pack(expand='true', fill='both', side='top')
        self.tblOrdiniEvasi.heading('numOrdine', text='Prog.')
        self.tblOrdiniEvasi.column(0, width=40, stretch=NO)
        self.tblOrdiniEvasi.heading('nomeProdotto', text='Nome Prodotto')
        self.tblOrdiniEvasi.heading('quantita', text='Quantità')
        self.tblOrdiniEvasi.column(2, width=67, stretch=NO)
        self.tblOrdiniEvasi.heading('note', text='Note')
        self.tblOrdiniEvasi.column(3, width=100, stretch=YES)
        self.tblOrdiniEvasi.heading('nomeCliente', text='Nome cliente')
        self.tblOrdiniEvasi.column(4, width=300, stretch=NO)
        self.tblOrdiniEvasi.heading('puntoVendita', text='Punto Vendita')
        self.tblOrdiniEvasi.column(5, width=300, stretch=NO)
        ################################################################################################################

        self.lfOrdiniEvasi.configure(height='200', text='Ordini evasi', width='200')
        self.lfOrdiniEvasi.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.framePulsantiInf = ttk.Frame(self)
        self.btnEliminaOrdine = ttk.Button(self.framePulsantiInf)
        self.btnEliminaOrdine.configure(text='Elimina ordine')
        self.btnEliminaOrdine.pack(expand='true', fill='x', side='left')
        self.btnEliminaOrdine.configure(command=self.eliminaOrdine)
        self.btnEvadiOrdine = ttk.Button(self.framePulsantiInf)
        self.btnEvadiOrdine.configure(text='Evadi ordine')
        self.btnEvadiOrdine.pack(expand='true', fill='x', side='left')
        self.btnEvadiOrdine.configure(command=self.evadiOrdine)
        self.btnOrdineConsegnato = ttk.Button(self.framePulsantiInf)
        self.btnOrdineConsegnato.configure(text='Ordine consegnato')
        self.btnOrdineConsegnato.pack(expand='true', fill='x', side='left')
        self.btnOrdineConsegnato.configure(command=self.ordineConsegnato)
        self.framePulsantiInf.configure(height='200', width='200')
        self.framePulsantiInf.pack(fill='x', padx='5', side='top')
        self.sizegrip2 = ttk.Sizegrip(self)
        self.sizegrip2.pack(anchor='se', side='top')
        self.configure(height='200', width='200')
        self.geometry('800x600')
        self.minsize(1024, 680)
        self.title('Gestione Ordini | AB Informatica - StockIt Manager')

        self.aggiornamentoOrdini()

    def nuovoOrdine(self):
        self.nomeProdotto = self.entryNomeProdotto.get()
        self.quantita = self.entryQuantita.get()
        self.note = self.entryNoteProdotto.get()
        self.nomeCliente = self.entryNomeCliente.get()

        # INSERISCE I DATI NEL DATABASE
        databaseOperations.GestioneOrdini(0, 0, self.nomeProdotto, self.quantita, self.note, self.nomeCliente, puntoVendita)

        # AGGIORNA LA TABELLA ORDINI
        self.aggiornamentoOrdini()

        # AZZERA I CAMPI
        self.entryNomeProdotto.delete(0, END)
        self.entryQuantita.delete(0, END)
        self.entryNoteProdotto.delete(0, END)
        self.entryNomeCliente.delete(0, END)

    def eliminaOrdine(self):
        indice = self.tblOrdiniDaEvadere.focus()
        idx = self.tblOrdiniDaEvadere.item(indice)
        valore = idx['values'][0]

        databaseOperations.GestioneOrdini(3, valore, nomeCliente='', nomeProdotto='', note='', quantity='', puntoVendita='')

        self.aggiornamentoOrdini()

    def evadiOrdine(self):
        indice = self.tblOrdiniDaEvadere.focus()
        idx = self.tblOrdiniDaEvadere.item(indice)
        valore = idx['values'][0]

        databaseOperations.GestioneOrdini(1, valore, nomeCliente='', nomeProdotto='', note='', quantity='', puntoVendita='')

        self.aggiornamentoOrdini()

    def ordineConsegnato(self):
        indice = self.tblOrdiniEvasi.focus()
        idx = self.tblOrdiniEvasi.item(indice)
        valore = idx['values'][0]

        databaseOperations.GestioneOrdini(2, valore, nomeCliente='', nomeProdotto='', note='', quantity='', puntoVendita='')

        self.aggiornamentoOrdini()

    def aggiornamentoOrdini(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM orders_to_ship")
        ordini = self.cursor.fetchall()

        # PULISCE TABELLA
        self.tblOrdiniDaEvadere.delete(*self.tblOrdiniDaEvadere.get_children())

        for ordine in ordini:
            self.tblOrdiniDaEvadere.insert("", END, values=ordine)

        self.cursor.execute("SELECT * FROM orders_shipped")
        ordini = self.cursor.fetchall()

        # PULISCE TABELLA
        self.tblOrdiniEvasi.delete(*self.tblOrdiniEvasi.get_children())

        for ordine in ordini:
            self.tblOrdiniEvasi.insert("", END, values=ordine)


# FINESTRA STAMPE#######################################################################################################
class StampeWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(StampeWidget, self).__init__(master, **kw)
        self.lfStampeOrdini = ttk.Labelframe(self)
        self.btnStampaNuoviOrdini = ttk.Button(self.lfStampeOrdini)
        self.btnStampaNuoviOrdini.configure(text='Stampa nuovi ordini')
        self.btnStampaNuoviOrdini.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaNuoviOrdini.configure(command=self.stampaOrdini)
        self.btnStampaOrdiniEvasi = ttk.Button(self.lfStampeOrdini)
        self.btnStampaOrdiniEvasi.configure(text='Stampa ordini evasi')
        self.btnStampaOrdiniEvasi.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaOrdiniEvasi.configure(command=self.stampaEvasi)
        self.btnStampaOrdiniConsegnati = ttk.Button(self.lfStampeOrdini)
        self.btnStampaOrdiniConsegnati.configure(text='Stampa ordini consegnati')
        self.btnStampaOrdiniConsegnati.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaOrdiniConsegnati.configure(command=self.stampaConsegnati)
        self.lfStampeOrdini.configure(height='200', text='Stampe Ordini', width='200')
        self.lfStampeOrdini.pack(expand='true', fill='both', pady='5', side='top')
        self.lfStampeAssistenza = ttk.Labelframe(self)
        self.btnStampaNuovePratiche = ttk.Button(self.lfStampeAssistenza)
        self.btnStampaNuovePratiche.configure(text='Stampa nuove pratiche')
        self.btnStampaNuovePratiche.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaNuovePratiche.configure(command=self.stampaNuovePratiche)
        self.btnStampaPraticheInLavorazione = ttk.Button(self.lfStampeAssistenza)
        self.btnStampaPraticheInLavorazione.configure(text='Stampa pratiche in lavorazione')
        self.btnStampaPraticheInLavorazione.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaPraticheInLavorazione.configure(command=self.stampaPraticheLavorazione)
        self.btnStampaPraticheLavorate = ttk.Button(self.lfStampeAssistenza)
        self.btnStampaPraticheLavorate.configure(text='Stampa pratiche lavorate')
        self.btnStampaPraticheLavorate.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaPraticheLavorate.configure(command=self.stampaPraticheLavorate)
        self.lfStampeAssistenza.configure(height='200', text='Stampe Assistenza', width='200')
        self.lfStampeAssistenza.pack(expand='true', fill='both', pady='5', side='top')
        self.lfStampeCassa = ttk.Labelframe(self)
        self.btnReportData = ttk.Button(self.lfStampeCassa)
        self.btnReportData.configure(text='Stampa report per data')
        self.btnReportData.pack(expand='true', fill='x', padx='5', side='top')
        self.btnReportData.configure(command=self.stampaReportData)
        self.btnReportMese = ttk.Button(self.lfStampeCassa)
        self.btnReportMese.configure(text='Stampa report per mese')
        self.btnReportMese.pack(expand='true', fill='x', padx='5', side='top')
        self.btnReportMese.configure(command=self.stampaReportMese)
        self.btnReportAnno = ttk.Button(self.lfStampeCassa)
        self.btnReportAnno.configure(text='Stampa report per anno')
        self.btnReportAnno.pack(expand='true', fill='x', padx='5', side='top')
        self.btnReportAnno.configure(command=self.stampaReportAnno)
        self.lfStampeCassa.configure(height='200', text='Stampe Cassa', width='200')
        self.lfStampeCassa.pack(expand='true', fill='both', pady='5', side='top')
        self.lfStampeBuoniSpesa = ttk.Labelframe(self)
        self.btnBuoniReportTotale = ttk.Button(self.lfStampeBuoniSpesa)
        self.btnBuoniReportTotale.configure(text='Stampa report totale')
        self.btnBuoniReportTotale.pack(expand='true', fill='x', padx='5', side='top')
        self.btnBuoniReportTotale.configure(command=self.stampaReportBuoni)
        self.btnBuoniStampaReportCarta = ttk.Button(self.lfStampeBuoniSpesa)
        self.btnBuoniStampaReportCarta.configure(text='Stampa report per carta')
        self.btnBuoniStampaReportCarta.pack(expand='true', fill='x', padx='5', side='top')
        self.btnBuoniStampaReportCarta.configure(command=self.stampaReportPerCarta)
        self.lfStampeBuoniSpesa.configure(height='200', text='Stampe Buoni Spesa', width='200')
        self.lfStampeBuoniSpesa.pack(expand='true', fill='both', pady='5', side='top')
        self.lfStampeComunicazioni = ttk.Labelframe(self)
        self.btnStampaComunicazione = ttk.Button(self.lfStampeComunicazioni)
        self.btnStampaComunicazione.configure(text='Stampa comunicazione')
        self.btnStampaComunicazione.pack(expand='true', fill='x', padx='5', side='top')
        self.btnStampaComunicazione.configure(command=self.stampaComunicazione)
        self.lfStampeComunicazioni.configure(height='200', text='Stampe Comunicazioni', width='200')
        self.lfStampeComunicazioni.pack(expand='true', fill='both', pady='5', side='top')
        self.configure(height='200', width='200')
        self.geometry('300x480')
        self.resizable(False, False)

    def stampaOrdini(self):
        pass

    def stampaEvasi(self):
        pass

    def stampaConsegnati(self):
        pass

    def stampaNuovePratiche(self):
        pass

    def stampaPraticheLavorazione(self):
        pass

    def stampaPraticheLavorate(self):
        pass

    def stampaReportData(self):
        pass

    def stampaReportMese(self):
        pass

    def stampaReportAnno(self):
        pass

    def stampaReportBuoni(self):
        pass

    def stampaReportPerCarta(self):
        pass

    def stampaComunicazione(self):
        pass


# FINESTRA PRINCIPALE###################################################################################################


def finestraStampe():
    StampeWidget(root)


class StockItApp:
    def __init__(self, master=None):
        # build ui
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM orders_to_ship")
        self.orders_to_ship = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM comunicazioni")
        self.comunicazioni = self.cursor.fetchall()

        self.masterFrame = ttk.Frame(master)
        self.style = ttk.Style(master)

        self.frmPulsantiSup = ttk.Frame(self.masterFrame)
        self.btnStampa = ttk.Button(self.frmPulsantiSup)
        self.img_printer = tk.PhotoImage(file='printer.png')
        self.btnStampa.configure(image=self.img_printer, text='Cassa')
        self.btnStampa.pack(expand='false', padx='5', pady='5', side='right')
        self.btnStampa.configure(command=finestraStampe)
        self.btnOrdini = ttk.Button(self.frmPulsantiSup)
        self.img_box1 = tk.PhotoImage(file='box1.png')
        self.btnOrdini.configure(image=self.img_box1, text='Ordini')
        self.btnOrdini.pack(expand='false', padx='5', side='left')
        self.btnOrdini.configure(command=self.finestraOrdini)
        self.btnAssistenza = ttk.Button(self.frmPulsantiSup)
        self.img_callcenter = tk.PhotoImage(file='call-center.png')
        self.btnAssistenza.configure(image=self.img_callcenter, text='Cassa')
        self.btnAssistenza.pack(expand='false', padx='5', side='left')
        self.btnAssistenza.configure(command=self.finestraAssistenza)
        self.btnCassa = ttk.Button(self.frmPulsantiSup)
        self.img_money = tk.PhotoImage(file='money.png')
        self.btnCassa.configure(image=self.img_money, text='Cassa')
        self.btnCassa.pack(expand='false', padx='5', side='left')
        self.btnCassa.configure(command=self.finestraCassa)
        self.btnChat = ttk.Button(self.frmPulsantiSup)
        self.img_chat = tk.PhotoImage(file='chat.png')
        self.btnChat.configure(image=self.img_chat, text='Cassa', style='')
        self.style.configure('Die.TButton', background='#f00')
        self.btnChat.pack(expand='false', padx='5', side='left')
        self.btnChat.configure(command=self.finestraChat)
        self.btnBuoni = ttk.Button(self.frmPulsantiSup)
        self.img_creditcard = tk.PhotoImage(file='credit-card.png')
        self.btnBuoni.configure(image=self.img_creditcard, text='Cassa')
        self.btnBuoni.pack(expand='false', padx='5', side='left')
        self.btnBuoni.configure(command=self.finestraFidelity)
        if operatore == 'manager' or 'master':
            self.btnSettings = ttk.Button(self.frmPulsantiSup)
            self.img_settings = tk.PhotoImage(file='settings.png')
            self.btnSettings.configure(image=self.img_settings, text='Cassa')
            self.btnSettings.pack(expand='false', padx='5', side='left')
            self.btnSettings.configure(command=self.finestraFidelity)
        if operatore == 'master':
            self.btnUsers = ttk.Button(self.frmPulsantiSup)
            self.img_users = tk.PhotoImage(file='user.png')
            self.btnUsers.configure(image=self.img_users, text='Cassa')
            self.btnUsers.pack(expand='false', padx='5', side='left')
            self.btnUsers.configure(command=self.finestraUtenti)
        self.frmPulsantiSup.configure(height='40', width='1024')
        self.frmPulsantiSup.pack(expand='false', fill='x', side='top')
        self.lfComunicazioni = ttk.Labelframe(self.masterFrame)
        # TABELLA COMUNICAZIONI E DEFINIZIONI###########################################################################
        self.tblComunicazioni = ttk.Treeview(self.lfComunicazioni, columns=columnsComunicazioni, show='headings')
        self.tblComunicazioni.pack(expand='true', fill='both', padx='4', pady='4', side='top')
        self.tblComunicazioni.heading('numComunicazione', text='Prog.')
        self.tblComunicazioni.column(0, width=40, stretch=NO)
        self.tblComunicazioni.heading('autore', text='Autore')
        self.tblComunicazioni.column(1, width=250, stretch=NO)
        self.tblComunicazioni.heading('messaggio', text='Messaggio')
        self.tblComunicazioni.heading('data', text='Data')
        self.tblComunicazioni.column(3, width=180, stretch=NO)
        self.tblComunicazioni.bind("<Double-1>", self.OnDoubleClickComunicazioni)


        ################################################################################################################

        self.lfComunicazioni.configure(height='200', text='Comunicazioni', width='200')  # LABELFRAME COMUNICAZIONI
        self.lfComunicazioni.pack(expand='true', fill='both', pady='5', side='top')
        self.lfOrdiniDaEvadere = ttk.Labelframe(self.masterFrame)

        # TABELLA ORDINI DA EVADERE E DEFINIZIONI#######################################################################
        self.tblOrdiniDaEvadere = ttk.Treeview(self.lfOrdiniDaEvadere, columns=columnsOrdini, show='headings')
        self.tblOrdiniDaEvadere.pack(expand='true', fill='both', padx='4', pady='4', side='top')
        self.tblOrdiniDaEvadere.heading('numOrdine', text='Prog.')
        self.tblOrdiniDaEvadere.column(0, width=40, stretch=NO)
        self.tblOrdiniDaEvadere.heading('nomeProdotto', text='Nome Prodotto')
        self.tblOrdiniDaEvadere.heading('quantita', text='Quantità')
        self.tblOrdiniDaEvadere.column(2, width=67, stretch=NO)
        self.tblOrdiniDaEvadere.heading('note', text='Note')
        self.tblOrdiniDaEvadere.column(3, width=100, stretch=YES)
        self.tblOrdiniDaEvadere.heading('nomeCliente', text='Nome Cliente')
        self.tblOrdiniDaEvadere.column(4, width=300, stretch=NO)
        self.tblOrdiniDaEvadere.heading('puntoVendita', text='Punto Vendita')
        self.tblOrdiniDaEvadere.column(5, width=300, stretch=NO)
        ################################################################################################################

        self.lfOrdiniDaEvadere.configure(height='200', text='Ordini da evadere', width='200')
        self.lfOrdiniDaEvadere.pack(expand='true', fill='both', side='top')
        self.sizegrip1 = ttk.Sizegrip(self.masterFrame)
        self.sizegrip1.pack(anchor='se', side='bottom')
        self.frmPulsantiInf = ttk.Frame(self.masterFrame)
        self.btnStampaOrdini = ttk.Button(self.frmPulsantiInf)
        self.btnStampaOrdini.configure(text='Stampa ordini')
        self.btnStampaOrdini.pack(expand='false', ipadx='10', ipady='6', side='left')
        self.btnStampaOrdini.configure(command=self.stampaOrdini)
        self.btnInserisciOrdine = ttk.Button(self.frmPulsantiInf)
        self.btnInserisciOrdine.configure(text='Inserisci ordine')
        self.btnInserisciOrdine.pack(expand='false', ipadx='10', ipady='6', side='left')
        self.btnInserisciOrdine.configure(command=self.finestraInserisciOrdine)
        self.btnOrdineEvaso = ttk.Button(self.frmPulsantiInf)
        self.btnOrdineEvaso.configure(text='Ordine evaso')
        self.btnOrdineEvaso.pack(expand='false', ipadx='10', ipady='6', side='left')
        self.btnOrdineEvaso.configure(command=self.ordineEvaso)
        self.btnAggiornaOrdini = ttk.Button(self.frmPulsantiInf)
        self.btnAggiornaOrdini.configure(text='Invia & Ricevi')
        self.btnAggiornaOrdini.pack(expand='false', ipadx='10', ipady='6', side='left')
        self.btnAggiornaOrdini.configure(command=self.aggiornamentoOrdini)
        self.btnInserisciComunicazione = ttk.Button(self.frmPulsantiInf)
        self.btnInserisciComunicazione.configure(text='Inserisci comunicazione')
        self.btnInserisciComunicazione.pack(expand='false', ipadx='10', ipady='6', side='right')
        self.btnInserisciComunicazione.configure(command=self.inserisciComunicazione)
        self.btnEliminaComunicazione = ttk.Button(self.frmPulsantiInf)
        self.btnEliminaComunicazione.configure(text='Elimina comunicazione')
        self.btnEliminaComunicazione.pack(expand='false', ipadx='10', ipady='6', side='right')
        self.btnEliminaComunicazione.configure(command=self.eliminaComunicazione)
        self.frmPulsantiInf.configure(height='60', width='1024')
        self.frmPulsantiInf.pack(expand='false', fill='x', padx='5', side='bottom')
        self.masterFrame.configure(height='200', width='1024')
        self.masterFrame.pack(expand='true', fill='both', side='top')

        self.aggiornamentoOrdini()
        self.autoAggiornamentoDaemon()


        # Main widget
        self.mainwindow = self.masterFrame

    def run(self):
        self.mainwindow.mainloop()

    @staticmethod
    def finestraOrdini():
        OrdiniWidget(root)

    @staticmethod
    def finestraAssistenza():
        AssistenzaWidget(root)

    @staticmethod
    def finestraUtenti():
        UtentiWidget(root)

    def finestraCassa(self):
        pass

    def finestraChat(self):
        self.btnChat.configure(style='')
        ChatWidget(root)

    def finestraFidelity(self):
        pass

    def stampaOrdini(self):
        pass

    @staticmethod
    def finestraInserisciOrdine():
        OrdiniWidget(root)

    def ordineEvaso(self):
        indice = self.tblOrdiniDaEvadere.focus()
        idx = self.tblOrdiniDaEvadere.item(indice)
        valore = idx['values'][0]

        databaseOperations.GestioneOrdini(1, valore, nomeCliente='', nomeProdotto='', note='', quantity='')

        self.aggiornamentoOrdini()

    def OnDoubleClickComunicazioni(self, event):
        item = self.tblComunicazioni.identify('item', event.x, event.y)
        indice = self.tblComunicazioni.focus()
        idx = self.tblComunicazioni.item(indice)
        valore = idx['values'][0]
        autore = idx['values'][1]
        messaggio = idx['values'][2]
        title = str(valore) + " - " + str(autore)
        tkinter.messagebox.showinfo(title="Comunicazione n."+title, message=messaggio + "\nAutore: " + autore, icon=None)


    def inserisciComunicazione(self):
        NuovaComunicazioneWidget()

    def eliminaComunicazione(self):
        indice = self.tblComunicazioni.focus()
        idx = self.tblComunicazioni.item(indice)
        valore = idx['values'][0]
        autore = idx['values'][1]

        if autore == nomeUtente or operatore == 'master':
            databaseOperations.Comunicazioni(1, valore, 0, 0, 0)
            self.aggiornamentoOrdini()
            tkinter.messagebox.showinfo(title='Comunicazione eliminata', message='Comunicazione eliminata con successo')

        else:
            tkinter.messagebox.showerror(title='Impossibile eliminare', message="Non puoi eliminare comunicazioni di "
                                                                                "cui non sei l'autore")

    def aggiornamentoOrdini(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM orders_to_ship")
        ordini = self.cursor.fetchall()

        self.tblOrdiniDaEvadere.delete(*self.tblOrdiniDaEvadere.get_children())

        for ordine in ordini:
            self.tblOrdiniDaEvadere.insert("", END, values=ordine)

        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM comunicazioni")
        comunicazioni = self.cursor.fetchall()

        self.tblComunicazioni.delete(*self.tblComunicazioni.get_children())

        for comunicazione in comunicazioni:
            messaggio = comunicazione[2].replace("\n", " ")
            nuovaComunicazione = [comunicazione[0], comunicazione[1], messaggio, comunicazione[3]]
            self.tblComunicazioni.insert("", END, values=nuovaComunicazione)

        self.cursor.close()
        self.mydb.close()

    def ricercaAggiornamenti(self):
        while 1:
            try:
                #time.sleep(1)
                mydb = mysql.connector.connect(option_files='connector.cnf')
                cursor = mydb.cursor()
                file1changed = False
                file2changed = False
                cursor.execute("SELECT * FROM orders_to_ship")
                NEWorders_to_ship = cursor.fetchall()
                cursor.execute("SELECT * FROM comunicazioni")
                NEWcomunicazioni = cursor.fetchall()
                cursor.close()
                mydb.close()
                if NEWorders_to_ship != self.orders_to_ship:
                    file1changed = True
                    # time.sleep(1)
                elif NEWcomunicazioni != self.comunicazioni:
                    file2changed = True
                    # time.sleep(1)
                else:
                    file1changed = False
                    file2changed = False

                if (file1changed or file2changed) == True:
                    self.orders_to_ship = NEWorders_to_ship
                    self.comunicazioni = NEWcomunicazioni

                    self.btnChat.configure(style='Die.TButton')
                    self.aggiornamentoOrdini()

                else:
                    pass
            except:
                print("error")

    @staticmethod
    def aggiornamentoInterfacce():
        UtentiWidget.aggiornaUtenti()
        AssistenzaWidget.aggiornamentoOrdini()
        OrdiniWidget.aggiornamentoOrdini()

    def autoAggiornamentoDaemon(self):
        newthread = threading.Thread(target=self.ricercaAggiornamenti)
        newthread.daemon = True
        newthread.start()
        print("Daemon STARTED\n")


operatore = 0

if __name__ == '__main__':

    databaseOperations.VerificaDatabase()

    root = tk.Tk()
    root.minsize(width=700, height=650)
    root.geometry('1024x650')
    root.state('zoomed')
    root.title('AB Informatica - StockIt Manager')
    root.iconbitmap('barcode.ico')

    try:
        password = tkinter.simpledialog.askstring('Password', 'Inserisci password\t\t\t', show='*')
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users WHERE password = %s", (password,))
        users = cursor.fetchall()
        user = users[0]
        nomeUtente = user[1]
        passwordUtente = user[2]
        operatore = user[3]
        puntoVendita = user[4]
        print(nomeUtente)
    except:
        tkinter.messagebox.showerror(title='Accesso errato', message="Impossibile effettuare l'accesso.\n"
                                                                     "Password errata o database irraggiungibile")
        exit()

    app = StockItApp(root)
    app.run()
