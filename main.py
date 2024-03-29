import ctypes
import sys
import threading
import time
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.ttk as ttk
from datetime import date
from tkinter import END, NO, YES, ANCHOR
from idlelib.tooltip import Hovertip


import _tkinter
import mysql.connector
from PIL import ImageTk, Image
from toastify import notify


import PDFOperations
import databaseOperations

columnsOrdini = ('numOrdine', 'nomeProdotto', 'quantita', 'note', 'nomeCliente', 'puntoVendita')
columnsComunicazioni = ('numComunicazione', 'autore', 'messaggio', 'data')
columnsAssistenza = ('numAssistenza', 'nomeCliente', 'contattoCliente', 'prodotto', 'difettoProdotto', 'dataConsegna',
                     'note', 'statoPratica')


# FINESTRA MODIFICA CLIENTE#############################################################################################
class ModificaFidWidget(tk.Toplevel):
    def __init__(self, nomeCliente, numeroCarta, indirizzoCliente, contattoCliente, master=None, **kw):
        super(ModificaFidWidget, self).__init__(master, **kw)
        self.labelframe3 = ttk.Labelframe(self)
        self.frame20 = ttk.Frame(self.labelframe3)
        self.label8 = ttk.Label(self.frame20)
        self.label8.configure(text='Nome cliente:')
        self.label8.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label9 = ttk.Label(self.frame20)
        self.label9.configure(text='Numero carta:')
        self.label9.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label12 = ttk.Label(self.frame20)
        self.label12.configure(text='Indirizzo:')
        self.label12.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label17 = ttk.Label(self.frame20)
        self.label17.configure(text='Contatto:')
        self.label17.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.frame20.configure(height='70', width='200')
        self.frame20.pack(expand=False, fill='y', side='left')
        self.frame21 = ttk.Frame(self.labelframe3)
        self.entry7 = ttk.Entry(self.frame21)
        self.entry7.pack(expand=True, fill='x', padx=5, pady=0, side='top')
        self.entry7.insert(0, nomeCliente)
        self.entryNumeroCarta = ttk.Entry(self.frame21)
        self.entryNumeroCarta.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entryNumeroCarta.insert(0, numeroCarta)
        self.entryIndirizzo = ttk.Entry(self.frame21)
        self.entryIndirizzo.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entryIndirizzo.insert(0, indirizzoCliente)
        self.entryContatto = ttk.Entry(self.frame21)
        self.entryContatto.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entryContatto.insert(0, contattoCliente)
        self.frame21.configure(height=60, width=200)
        self.frame21.pack(expand=True, fill='both', pady=5, side='left')
        self.frame26 = ttk.Frame(self.labelframe3)
        self.btnInserisciCarta = ttk.Button(self.frame26)
        self.img_refresh = tk.PhotoImage(file='images/refresh.png')
        self.btnInserisciCarta.configure(image=self.img_refresh, text='button13')
        self.btnInserisciCarta.pack(expand=True, fill='y', padx=5, pady=5, side='top')
        self.btnInserisciCarta.configure(command=self.inserisciCarta)
        self.frame26.configure(height='200', width='200')
        self.frame26.pack(expand=True, fill='both', side='top')
        self.labelframe3.configure(height=80, text='Modifica cliente', width=200)
        self.labelframe3.pack(expand=True, fill='both', padx=5, pady=5, side='top')
        self.configure(height=200, width=200)
        self.geometry('640x200')
        self.title('Modifica cliente | AB Informatica - StockIt Manager')

    def inserisciCarta(self):
        numeroCarta = self.entryNumeroCarta.get()
        nomeCliente = self.entry7.get()
        indirizzoCliente = self.entryIndirizzo.get()
        contattoCliente = self.entryContatto.get()

        databaseOperations.Fidelity(numeroCarta=numeroCarta, nomeUtente=nomeCliente,
                                    indirizzoCliente=indirizzoCliente,
                                    contattoCliente=contattoCliente).aggiornaCliente()
        self.destroy()
        RicercaFidClienteWidget(root).aggiornamentoCarte()


# FINESTRA INSERISCI FIDELITY###########################################################################################
class InserisciFidWidget(tk.Toplevel):
    def __init__(self, nomeCliente, numeroCarta, master=None, **kw):
        super(InserisciFidWidget, self).__init__(master, **kw)
        self.labelframe3 = ttk.Labelframe(self)
        self.frame20 = ttk.Frame(self.labelframe3)
        self.label8 = ttk.Label(self.frame20)
        self.label8.configure(text='Nome cliente:')
        self.label8.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label9 = ttk.Label(self.frame20)
        self.label9.configure(text='Numero carta:')
        self.label9.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label12 = ttk.Label(self.frame20)
        self.label12.configure(text='Indirizzo:')
        self.label12.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label17 = ttk.Label(self.frame20)
        self.label17.configure(text='Contatto:')
        self.label17.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.label13 = ttk.Label(self.frame20)
        self.label13.configure(text='Credito iniziale:')
        self.label13.pack(anchor='e', expand=True, padx=5, pady=4, side='top')
        self.frame20.configure(height=70, width=200)
        self.frame20.pack(expand=False, fill='y', side='left')
        self.frame21 = ttk.Frame(self.labelframe3)
        self.entry7 = ttk.Entry(self.frame21)
        self.entry7.pack(expand=True, fill='x', padx=5, pady=0, side='top')
        self.entry7.insert(0, nomeCliente)
        self.entryNumeroCarta = ttk.Entry(self.frame21)
        self.entryNumeroCarta.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entryNumeroCarta.insert(0, numeroCarta)
        self.entryIndirizzo = ttk.Entry(self.frame21)
        self.entryIndirizzo.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entryContatto = ttk.Entry(self.frame21)
        self.entryContatto.pack(expand=True, fill='x', padx=5, pady=5, side='top')
        self.entry11 = ttk.Entry(self.frame21)
        self.entry11.pack(expand=True, fill='x', padx=5, pady=0, side='top')
        self.frame21.configure(height=60, width=200)
        self.frame21.pack(expand=True, fill='both', pady=5, side='left')
        self.frame26 = ttk.Frame(self.labelframe3)
        self.btnInserisciCarta = ttk.Button(self.frame26)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.btnInserisciCarta.configure(image=self.img_plus, text='button13')
        self.btnInserisciCarta.pack(expand=True, fill='y', padx=5, pady=5, side='top')
        self.btnInserisciCarta.configure(command=self.inserisciCarta)
        self.frame26.configure(height=200, width=200)
        self.frame26.pack(expand=True, fill='both', side='top')
        self.labelframe3.configure(height=80, text='Inserisci cliente', width=200)
        self.labelframe3.pack(expand=True, fill='both', padx=5, pady=5, side='top')
        self.configure(height=200, width=200)
        self.geometry('640x200')
        self.title('Inserisci cliente | AB Informatica - StockIt Manager')

    def inserisciCarta(self):
        numeroCarta = self.entryNumeroCarta.get()
        nomeCliente = self.entry7.get()
        indirizzoCliente = self.entryIndirizzo.get()
        contattoCliente = self.entryContatto.get()
        credito = self.entry11.get()

        databaseOperations.Fidelity(numeroCarta=numeroCarta, nomeUtente=nomeCliente,
                                    indirizzoCliente=indirizzoCliente, creditoCliente=credito,
                                    contattoCliente=contattoCliente).inserisciCliente()
        self.destroy()
        RicercaFidClienteWidget(root).aggiornamentoCarte()


# FINESTRA FIDELITY GESTIONE CLIENTE####################################################################################
class FidClienteWidget(tk.Toplevel):
    def __init__(self, nomeCliente, numeroCarta, indirizzoCliente, contattoCliente, creditoCliente, master=None, **kw):
        super(FidClienteWidget, self).__init__(master, **kw)

        global carta
        carta = str(numeroCarta)
        global credito
        credito = creditoCliente
        aggiungiCredito = tk.DoubleVar()
        sottraiCredito = tk.DoubleVar()

        self.labelframe2 = ttk.Labelframe(self)
        self.frame10 = ttk.Frame(self.labelframe2)
        self.label6 = ttk.Label(self.frame10)
        self.label6.configure(text='Nome cliente:')
        self.label6.pack(anchor='e', expand=True, padx='5', pady='5', side='top')
        self.label7 = ttk.Label(self.frame10)
        self.label7.configure(text='Numero carta:')
        self.label7.pack(anchor='e', expand=True, padx=5, pady='5', side='top')
        self.frame10.configure(height='70', width='200')
        self.frame10.pack(expand=False, padx='10', side='left')
        self.frame11 = ttk.Frame(self.labelframe2)
        self.labelNomeCliente = ttk.Label(self.frame11)
        self.labelNomeCliente.configure(text=nomeCliente)
        self.labelNomeCliente.pack(anchor='w', padx='5', pady='5', side='top')
        self.labelNumeroCarta = ttk.Label(self.frame11)
        self.labelNumeroCarta.configure(text=numeroCarta)
        self.labelNumeroCarta.pack(anchor='w', padx='5', pady='5', side='top')
        self.frame11.configure(height='60', width='250')
        self.frame11.pack(fill='x', pady='5', side='left')
        self.frame14 = ttk.Frame(self.labelframe2)
        self.label10 = ttk.Label(self.frame14)
        self.label10.configure(text='Indirizzo:')
        self.label10.pack(anchor='e', padx='5', pady='5', side='top')
        self.label11 = ttk.Label(self.frame14)
        self.label11.configure(text='Contatto:')
        self.label11.pack(anchor='e', padx='5', pady='5', side='top')
        self.frame14.configure(height='60', width='200')
        self.frame14.pack(fill='x', padx='10', pady='5', side='left')
        self.frame15 = ttk.Frame(self.labelframe2)
        self.labelIndirizzo = ttk.Label(self.frame15)
        self.labelIndirizzo.configure(text=indirizzoCliente)
        self.labelIndirizzo.pack(anchor='w', padx='5', pady='5', side='top')
        self.labelContatto = ttk.Label(self.frame15)
        self.labelContatto.configure(text=contattoCliente)
        self.labelContatto.pack(anchor='w', padx='5', pady='5', side='top')
        self.frame15.configure(height='60', width='250')
        self.frame15.pack(fill='x', pady='5', side='left')
        self.frame17 = ttk.Frame(self.labelframe2)
        self.labelCredito = ttk.Label(self.frame17)
        self.labelCredito.configure(font='{Arial} 20 {bold}', text=creditoCliente)
        self.labelCredito.pack(anchor='w', padx='5', pady='5', side='top')
        self.frame17.configure(height='60', width='250')
        self.frame17.pack(fill='x', pady='5', side='right')
        self.frame16 = ttk.Frame(self.labelframe2)
        self.label15 = ttk.Label(self.frame16)
        self.label15.configure(text='Credito:')
        self.label15.pack(anchor='e', padx='5', pady='5', side='top')
        self.frame16.configure(height='60', width='250')
        self.frame16.pack(fill='x', padx='10', pady='5', side='right')
        self.labelframe2.configure(height='80', text='Cliente', width='200')
        self.labelframe2.pack(fill='x', padx='5', pady='5', side='top')
        self.frame12 = ttk.Frame(self)
        self.lfAggiungiCredito = ttk.Labelframe(self.frame12)
        self.entryAggiungiCredito = ttk.Entry(self.lfAggiungiCredito, textvariable=aggiungiCredito)
        self.aggiungi = tk.DoubleVar(value=0.00)
        self.entryAggiungiCredito.configure(font='{Arial} 36 {}', justify='center', textvariable=self.aggiungi,
                                            width=4)
        _text_ = '''0.00'''
        self.entryAggiungiCredito.delete('0', 'end')
        self.entryAggiungiCredito.pack(expand=True, fill='both', side='top')
        self.entryAggiungiCredito.bind('<Return>', lambda a: self.aggiungiCredito())
        self.buttonAggiungi = ttk.Button(self.lfAggiungiCredito)
        self.img_income = tk.PhotoImage(file='images/income.png')
        self.buttonAggiungi.configure(image=self.img_income, text='button6')
        self.buttonAggiungi.pack(expand=True, fill='both', side='top')
        self.buttonAggiungi.configure(command=self.aggiungiCredito)
        self.lfAggiungiCredito.configure(height='200', text='Aggiungi credito', width='200')
        self.lfAggiungiCredito.pack(expand=True, fill='both', side='left')
        self.lfSottraiCredito = ttk.Labelframe(self.frame12)
        self.entrySottraiCredito = ttk.Entry(self.lfSottraiCredito, textvariable=sottraiCredito)
        self.entrySottraiCredito.bind('<Return>', lambda a: self.sottraiCredito())
        self.sottrai = tk.DoubleVar(value=0.00)
        self.entrySottraiCredito.configure(font='{Arial} 36 {}', justify='center', textvariable=self.sottrai, width=4)
        _text_ = '''0.00'''
        self.entrySottraiCredito.delete('0', 'end')
        self.entrySottraiCredito.pack(expand=True, fill='both', side='top')
        self.buttonSottrai = ttk.Button(self.lfSottraiCredito)
        self.img_outcome = tk.PhotoImage(file='images/outcome.png')
        self.buttonSottrai.configure(image=self.img_outcome, text='button6')
        self.buttonSottrai.pack(expand=True, fill='both', side='top')
        self.buttonSottrai.configure(command=self.sottraiCredito)
        self.lfSottraiCredito.configure(height='200', text='Sottrai credito', width='200')
        self.lfSottraiCredito.pack(expand=True, fill='both', side='left')
        self.frame12.configure(height='200', width='200')
        self.frame12.pack(expand=True, fill='both', padx='5', pady='5', side='top')
        self.img_creditcard = tk.PhotoImage(file='images/credit-card.png')
        self.configure(height='600', width='800')
        self.geometry('800x600')
        title = 'Gestione cliente: ' + nomeCliente + ' | AB Informatica - StockIt Manager'
        self.title(title)
        self.iconphoto(True, self.img_creditcard)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        RicercaFidClienteWidget(root)
        self.destroy()

    def aggiungiCredito(self):
        try:
            creditoAggiornato = databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
            nuovoCredito = float(creditoAggiornato) + float(self.entryAggiungiCredito.get())
            databaseOperations.Fidelity(numeroCarta=carta, creditoCliente=nuovoCredito).aggiornaCredito()
            databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
            creditoAggiornato = databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
            self.entryAggiungiCredito.delete(0, END)
            self.labelCredito.configure(text=creditoAggiornato)
        except ValueError:
            pass

    def sottraiCredito(self):
        try:
            creditoAggiornato = databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
            nuovoCredito = float(creditoAggiornato) - float(self.entrySottraiCredito.get())
            if nuovoCredito >= 0:
                databaseOperations.Fidelity(numeroCarta=carta, creditoCliente=nuovoCredito) .aggiornaCredito()
                databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
                creditoAggiornato = databaseOperations.Fidelity(numeroCarta=carta).verificaCredito()
                self.entrySottraiCredito.delete(0, END)
                self.labelCredito.configure(text=creditoAggiornato)
            elif nuovoCredito < 0:
                tkinter.messagebox.showerror(parent=self, title='Credito insufficiente',
                                             message="L'operazione non è consentita, credito insufficiente")
        except ValueError:
            pass


# FINESTRA FIDELITY RICERCA CLIENTE#####################################################################################
class RicercaFidClienteWidget(tk.Toplevel):

    def __init__(self, master=None, **kw):
        super(RicercaFidClienteWidget, self).__init__(master, **kw)
        self.labelframe1 = ttk.Labelframe(self)
        self.frame6 = ttk.Frame(self.labelframe1)
        self.labelNomeClienteFid = ttk.Label(self.frame6)
        self.labelNomeClienteFid.configure(text='Nome cliente:')
        self.labelNomeClienteFid.pack(anchor='e', expand=True, padx=5, pady=5, side='top')
        self.labelNumeroCartaFid = ttk.Label(self.frame6)
        self.labelNumeroCartaFid.configure(text='Numero carta:')
        self.labelNumeroCartaFid.pack(anchor='e', expand=True, padx='5', pady='5', side='top')
        self.frame6.configure(height='70', width='200')
        self.frame6.pack(expand=False, side='left')
        self.frame8 = ttk.Frame(self.labelframe1)
        self.entry2 = ttk.Entry(self.frame8)
        self.entry2.pack(expand=True, fill='x', padx='5', pady='5', side='top')
        self.entry3 = ttk.Entry(self.frame8)
        self.entry3.pack(expand=True, fill='x', padx='5', pady='5', side='top')
        self.entry3.focus_force()
        self.frame8.configure(height='60', width='200')
        self.frame8.pack(expand=True, fill='x', pady='5', side='left')

        #TODO: Integrare fuznione camera nell'eseguibile
        '''self.frame13 = ttk.Frame(self.labelframe1)
        self.buttonCamera = ttk.Button(self.frame13)
        self.img_qrcode = tk.PhotoImage(file='images/qr-code.png')
        self.buttonCamera.configure(image=self.img_qrcode, text='Camera')
        self.buttonCamera.pack(padx='5', pady='5', side='top')
        self.buttonCamera.configure(command=self.scanTessera)
        self.frame13.configure(height='200', width='200')
        self.frame13.pack(side='left')'''
        self.labelframe1.configure(height='80', text='Ricerca cliente', width='200')
        self.labelframe1.pack(fill='x', padx='5', pady='5', side='top')
        self.button11 = ttk.Button(self)
        self.button11.configure(text='Ricerca cliente')
        self.button11.pack(fill='x', padx='5', side='top')
        self.button11.configure(command=self.ricercaCliente)
        self.frame9 = ttk.Frame(self)
        self.treeview2 = ttk.Treeview(self.frame9)
        self.treeview2_cols = ['columnCarta', 'columnNomeCliente', 'columnIndirizzo', 'columnContatto', 'columnCredito']
        self.treeview2_dcols = ['columnCarta', 'columnNomeCliente', 'columnIndirizzo', 'columnContatto',
                                'columnCredito']
        self.treeview2.configure(columns=self.treeview2_cols, show='headings')
        self.treeview2.column('columnCarta', anchor='w', stretch=True, width=200, minwidth=20)
        self.treeview2.column('columnNomeCliente', anchor='w', stretch=True, width=200, minwidth=20)
        self.treeview2.column('columnIndirizzo', anchor='w', stretch=True, width=200, minwidth=20)
        self.treeview2.column('columnContatto', anchor='w', stretch=True, width=200, minwidth=20)
        self.treeview2.column('columnCredito', anchor='w', stretch=True, width=200, minwidth=20)
        self.treeview2.heading('columnCarta', anchor='w', text='Numero carta')
        self.treeview2.heading('columnNomeCliente', anchor='w', text='Nome cliente')
        self.treeview2.heading('columnIndirizzo', anchor='w', text='Indirizzo')
        self.treeview2.heading('columnContatto', anchor='w', text='Contatto')
        self.treeview2.heading('columnCredito', anchor='w', text='Credito')
        self.treeview2.pack(expand=True, fill='both', side='top')
        self.treeview2.bind('<Double-1>', self.callback, add='')
        self.treeview2.bind('<Button-3>', self.popup)
        self.treeview2.yview_moveto(1)
        self.frame9.configure(height=200, width=200)
        self.frame9.pack(expand=True, fill='both', padx=5, pady=5, side='top')
        self.img_creditcard = tk.PhotoImage(file='images/credit-card.png')
        self.configure(height=600, width=800)
        self.geometry('1024x600')
        self.iconphoto(True, self.img_creditcard)
        self.title('Ricerca clienti | AB Informatica - StockIt Manager')

        self.aggiornamentoCarte()

    def eliminaCliente(self):
        elimina = tkinter.messagebox.askyesno(parent=self, title='Eliminare card?', message='Intendi eliminare '
                                                                                            'definitivamente la card?')

        if elimina:

            curItems = self.treeview2.selection()
            for idx in curItems:
                index = self.treeview2.item(idx)
                valore = index['values'][0]
                databaseOperations.Fidelity(numeroCarta=valore).eliminaCliente()

            self.aggiornamentoCarte()

        else:
            pass
#todo::::::POPUP
    def popup(self, event):
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Modifica", command=self.modificaCliente)
        m.add_command(label="Elimina", command=self.eliminaCliente)

        iid = self.treeview2.identify_row(event.y)
        if iid:
            self.treeview2.selection_set(iid)
            self.treeview2.focus(iid)
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        else:
            pass

    def modificaCliente(self):
        indice = self.treeview2.focus()
        idx = self.treeview2.item(indice)
        numeroCarta = str(idx['values'][0])
        if numeroCarta[0] != '0':
            numeroCarta = '0' + numeroCarta
        nomeCliente = idx['values'][1]
        indirizzoCliente = idx['values'][2]
        contattoCliente = idx['values'][3]
        self.destroy()
        ModificaFidWidget(nomeCliente=nomeCliente, numeroCarta=numeroCarta, indirizzoCliente=indirizzoCliente,
                          contattoCliente=contattoCliente)

    '''def scanTessera(self):
        self.entry3.delete(0, END)
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(3, 1024)
        cap.set(4, 768)

        code = 0

        while code == 0:

            success, img = cap.read()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                if myData != code:
                    self.entry3.insert(END, myData)
                    code = myData
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        # playsound("beep.wav")
        self.ricercaCliente()'''

    def ricercaCliente(self):
        nomeCliente = self.entry2.get()
        numeroCarta = self.entry3.get()
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)

        ordini = databaseOperations.Fidelity(nomeUtente=nomeCliente, numeroCarta=numeroCarta).ricercaCliente()

        if numeroCarta or nomeCliente != '':
            self.treeview2.delete(*self.treeview2.get_children())
            if self.is_empty(ordini):
                nuovaCarta = tkinter.messagebox.askyesno(parent=self.frame6, title='Card non presente',
                                                         message='La card inserita non è presente a sistema, inserire?')

                if nuovaCarta:
                    self.destroy()
                    InserisciFidWidget(nomeCliente=nomeCliente, numeroCarta=numeroCarta, master=root)

                else:
                    pass

            else:
                for ordine in ordini:
                    self.treeview2.insert("", END, values=ordine)
        else:
            tkinter.messagebox.showerror(parent=self, title='Compilare i campi', message='Compilare i campi richiesti')

    def callback(self, event):
        indice = self.treeview2.focus()
        idx = self.treeview2.item(indice)
        numeroCarta = '0' + str(idx['values'][0])
        nomeCliente = idx['values'][1]
        indirizzoCliente = idx['values'][2]
        contattoCliente = idx['values'][3]
        creditoCliente = idx['values'][4]
        self.destroy()
        FidClienteWidget(nomeCliente=nomeCliente, numeroCarta=str(numeroCarta), indirizzoCliente=indirizzoCliente,
                         contattoCliente=contattoCliente, creditoCliente=creditoCliente)

    def is_empty(self, any_structure):
        if any_structure:
            return False
        else:
            return True

    def aggiornamentoCarte(self):
        self.treeview2.delete(*self.treeview2.get_children())
        ordini = databaseOperations.Fidelity().selezionaClienti()

        for ordine in ordini:
            self.treeview2.insert("", END, values=ordine)


# FINESTRA CASSA########################################################################################################
class CassaWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.incassoTotale = tk.StringVar()
        self.corrispettivo = tk.StringVar()
        self.fatturato = tk.StringVar()
        self.contanti = tk.StringVar()
        self.pos = tk.StringVar()
        self.finanziamenti = tk.StringVar()
        self.bonifici = tk.StringVar()
        self.assegni = tk.StringVar()
        self.acconti = tk.StringVar()
        self.preincassato = tk.StringVar()

        iconaCassa = tk.PhotoImage(file='images/money.png')

        super(CassaWidget, self).__init__(master, **kw)
        self.lfReportGiornata = ttk.Labelframe(self)
        self.lfTotali = ttk.Labelframe(self.lfReportGiornata)
        self.frame1 = ttk.Frame(self.lfTotali)
        self.lblIncassoTotale = ttk.Label(self.frame1)
        self.lblIncassoTotale.configure(text='Incasso totale:')
        self.lblIncassoTotale.pack(anchor='e', pady=5, side='top')
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text='Corrispettivo:')
        self.label3.pack(anchor='e', pady=5, side='top')
        self.label4 = ttk.Label(self.frame1)
        self.label4.configure(text='Fatturato:')
        self.label4.pack(anchor='e', pady=5, side='top')
        self.frame1.configure(height=200, width=150)
        self.frame1.pack(padx=5, side='left')
        self.frame4 = ttk.Frame(self.lfTotali)
        self.entryIncassoTot = ttk.Entry(self.frame4, textvariable=self.incassoTotale)
        self.entryIncassoTot.pack(expand=True, fill='x', pady=4, side='top')
        self.entryCorrispettivo = ttk.Entry(self.frame4, textvariable=self.corrispettivo)
        self.entryCorrispettivo.pack(expand=True, fill='x', pady='4', side='top')
        self.entryFatturato = ttk.Entry(self.frame4, textvariable=self.fatturato)
        self.entryFatturato.pack(expand=True, fill='x', pady='4', side='top')
        self.frame4.configure(height='80', width='200')
        self.frame4.pack(expand=True, fill='x', padx='5', side='left')
        self.lfTotali.configure(height='200', text='Totali Giornata', width='200')
        self.lfTotali.pack(expand=False, fill='x', padx='5', pady='5', side='top')
        self.lfDettaglio = ttk.Labelframe(self.lfReportGiornata)
        self.frame6 = ttk.Frame(self.lfDettaglio)
        self.label5 = ttk.Label(self.frame6)
        self.label5.configure(text='Contanti:')
        self.label5.pack(anchor='e', pady='10', side='top')
        self.label6 = ttk.Label(self.frame6)
        self.label6.configure(text='POS:')
        self.label6.pack(anchor='e', pady='10', side='top')
        self.label7 = ttk.Label(self.frame6)
        self.label7.configure(text='Finanziamenti:')
        self.label7.pack(anchor='e', pady='10', side='top')
        self.label8 = ttk.Label(self.frame6)
        self.label8.configure(text='Bonifici:')
        self.label8.pack(anchor='e', pady='10', side='top')
        self.label9 = ttk.Label(self.frame6)
        self.label9.configure(text='Assegni:')
        self.label9.pack(anchor='e', pady='10', side='top')
        self.label10 = ttk.Label(self.frame6)
        self.label10.configure(text='Acconti:')
        self.label10.pack(anchor='e', pady='10', side='top')
        self.label11 = ttk.Label(self.frame6)
        self.label11.configure(text='Già incassato:')
        self.label11.pack(anchor='e', pady='10', side='top')
        self.label12 = ttk.Label(self.frame6)
        self.label12.configure(text='Data:')
        self.label12.pack(anchor='e', pady=10, side='top')
        self.frame6.configure(height='200', width='100')
        self.frame6.pack(expand=True, fill='both', side='left')
        self.frame8 = ttk.Frame(self.lfDettaglio)
        self.entryContanti = ttk.Entry(self.frame8, textvariable=self.contanti)
        self.entryContanti.pack(pady='9', side='top')
        self.entryPOS = ttk.Entry(self.frame8, textvariable=self.pos)
        self.entryPOS.pack(pady='9', side='top')
        self.entryFinanziamenti = ttk.Entry(self.frame8, textvariable=self.finanziamenti)
        self.entryFinanziamenti.pack(pady='9', side='top')
        self.entryBonifici = ttk.Entry(self.frame8, textvariable=self.bonifici)
        self.entryBonifici.pack(pady='9', side='top')
        self.entryAssegni = ttk.Entry(self.frame8, textvariable=self.assegni)
        self.entryAssegni.pack(pady='9', side='top')
        self.entryAcconti = ttk.Entry(self.frame8, textvariable=self.acconti)
        self.entryAcconti.pack(pady='9', side='top')
        self.entry = ttk.Entry(self.frame8, textvariable=self.preincassato)
        self.entry.pack(pady='9', side='top')
        self.entryData = ttk.Entry(self.frame8)
        self.entryData.pack(pady=9, side='top')
        self.entryData.insert(END, str(date.today()))
        self.btnQuadratura = ttk.Button(self.frame8)
        self.btnQuadratura.configure(text='Quadratura')
        self.btnQuadratura.pack(fill='x', padx='5', pady='10', side='top')
        self.btnQuadratura.configure(command=self.quadratura)
        self.lblQuadratura = ttk.Label(self.frame8, text='0,00')
        self.lblQuadratura.pack(side='top')

        self.btnInviaIncasso = ttk.Button(self.frame8)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.btnInviaIncasso.configure(image=self.img_plus, text='button7')
        self.btnInviaIncasso.pack(expand=False, fill='both', padx='5', pady='5', side='bottom')
        self.btnInviaIncasso.configure(command=self.inviaIncasso)
        self.label14 = ttk.Label(self.frame8)
        self.label14.configure(text='Invia incassi:')
        self.label14.pack(pady='5', side='bottom')
        self.frame8.configure(height='200', width='100')
        self.frame8.pack(expand=True, fill='both', side='left')
        self.lfDettaglio.configure(height='200', text='Dettaglio Giornata', width='200')
        self.lfDettaglio.pack(expand=True, fill='both', padx='5', pady='5', side='top')
        self.lfReportGiornata.configure(height='200', text='Report Giornata', width='200')
        self.lfReportGiornata.pack(expand=False, fill='both', padx='5', pady='5', side='left')
        self.separator1 = ttk.Separator(self)
        self.separator1.configure(orient='vertical')
        self.separator1.pack(ipady='250', side='left')
        self.lfStorico = ttk.Labelframe(self)
        self.tblStoricoGiornate = ttk.Treeview(self.lfStorico)
        self.tblStoricoGiornate_cols = ['incassoTotale', 'corrispettivo', 'fatturato', 'contanti', 'pos',
                                        'finanziamenti', 'bonifici', 'assegni', 'acconti', 'preincassati', 'data',
                                        'cassaPuntoVendita']
        self.tblStoricoGiornate_dcols = ['incassoTotale', 'corrispettivo', 'fatturato', 'contanti', 'pos',
                                         'finanziamenti', 'bonifici', 'assegni', 'acconti', 'preincassati', 'data',
                                         'cassaPuntoVendita']
        self.tblStoricoGiornate.configure(columns=self.tblStoricoGiornate_cols, show='headings')

        self.tblStoricoGiornate.column('incassoTotale', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('corrispettivo', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('fatturato', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('contanti', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('pos', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('finanziamenti', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('bonifici', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('assegni', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('acconti', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('preincassati', anchor='w', stretch=True, width=80, minwidth=20)
        self.tblStoricoGiornate.column('data', anchor='w', stretch=True, width=100, minwidth=20)
        self.tblStoricoGiornate.column('cassaPuntoVendita', anchor='w', stretch=True, width=80, minwidth=20)

        self.tblStoricoGiornate.heading('incassoTotale', anchor='w', text='Incasso totale')
        self.tblStoricoGiornate.heading('corrispettivo', anchor='w', text='Corrispettivo')
        self.tblStoricoGiornate.heading('fatturato', anchor='w', text='Fatturato')
        self.tblStoricoGiornate.heading('contanti', anchor='w', text='Contanti')
        self.tblStoricoGiornate.heading('pos', anchor='w', text='POS')
        self.tblStoricoGiornate.heading('finanziamenti', anchor='w', text='Finanziamenti')
        self.tblStoricoGiornate.heading('bonifici', anchor='w', text='Bonifici')
        self.tblStoricoGiornate.heading('assegni', anchor='w', text='Assegni')
        self.tblStoricoGiornate.heading('acconti', anchor='w', text='Acconti')
        self.tblStoricoGiornate.heading('preincassati', anchor='w', text='Già incassati')
        self.tblStoricoGiornate.heading('data', anchor='w', text='Data')
        self.tblStoricoGiornate.heading('cassaPuntoVendita', anchor='w', text='Punto vendita')
        self.tblStoricoGiornate.pack(expand='true', fill='both', side='top')
        self.tblStoricoGiornate.yview_moveto(1)
        self.frame9 = ttk.Frame(self.lfStorico)
        self.frame9.configure(height='70', width='200')
        self.frame9.pack(fill='x', side='top')
        self.btnEliminaGiornata = ttk.Button(self.frame9)
        self.btnEliminaGiornata.configure(text='Elimina record', padding=10, command=self.eliminaRecord)
        self.btnEliminaGiornata.pack(expand='true', fill='y', anchor='e', side='right')
        self.lfStorico.configure(height='200', text='Storico Giornate', width='200')
        self.lfStorico.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.configure(height='200', width='200')
        self.geometry('1366x700')
        self.iconphoto(False, iconaCassa)
        self.title('Gestione Cassa | AB Informatica - StockIt Manager')

        self._default_ = 0

        self.entry.insert(0, self._default_)
        self.entryContanti.insert(0, self._default_)
        self.entryPOS.insert(0, self._default_)
        self.entryBonifici.insert(0, self._default_)
        self.entryAssegni.insert(0, self._default_)
        self.entryAcconti.insert(0, self._default_)
        self.entryFinanziamenti.insert(0, self._default_)
        self.entryFatturato.insert(0, self._default_)
        self.entryCorrispettivo.insert(0, self._default_)

        self.aggiornaCasse()
        self.focus_force()



    def quadratura(self):
        self.entryIncassoTot.delete(0, END)
        bonifici = 0
        # incassoTotale = float(self.incassoTotale.get())
        try:
            corrispettivo = float(self.corrispettivo.get())
            fatturato = float(self.fatturato.get())
            contanti = float(self.contanti.get())
            pos = float(self.pos.get())
            finanziamenti = float(self.finanziamenti.get())
            bonifici = float(self.bonifici.get())
            assegni = float(self.assegni.get())
            acconti = float(self.acconti.get())
            preincassato = float(self.preincassato.get())
            sommaCorrispettivi = corrispettivo + fatturato
            self.entryIncassoTot.insert(0, str(sommaCorrispettivi))
            incassoTotale = float(self.incassoTotale.get())
        except ValueError:
            tkinter.messagebox.showerror(parent=self, title='Valore non corretto',
                                         message='Il valore inserito non è un numero')
            self.entryIncassoTot.delete(0, END)
            self.entryCorrispettivo.delete(0, END)
            self.entryFatturato.delete(0, END)
            self.entryContanti.delete(0, END)
            self.entryPOS.delete(0, END)
            self.entryFinanziamenti.delete(0, END)
            self.entryAssegni.delete(0, END)
            self.entryBonifici.delete(0, END)
            self.entryAcconti.delete(0, END)
            self.entry.delete(0, END)
            ####
            self.entry.insert(0, self._default_)
            self.entryContanti.insert(0, self._default_)
            self.entryPOS.insert(0, self._default_)
            self.entryBonifici.insert(0, self._default_)
            self.entryAssegni.insert(0, self._default_)
            self.entryAcconti.insert(0, self._default_)
            self.entryFinanziamenti.insert(0, self._default_)
            self.entryFatturato.insert(0, self._default_)
            self.entryCorrispettivo.insert(0, self._default_)


        try:
            totale = contanti + pos + finanziamenti + bonifici + assegni - acconti + preincassato
            quadratura = totale - incassoTotale
            quadratura = round(quadratura, 2)
            # self.entryQuadratura.insert(0, str(quadratura))
            self.lblQuadratura.configure(text=quadratura)
            if quadratura != 0:
                tkinter.messagebox.showerror(parent=self.frame1, title="Squadratura",
                                             message="È stata riscontrata una squadratura di €" + str(quadratura))

        except UnboundLocalError:
            pass



    def eliminaRecord(self):
        indice = self.tblStoricoGiornate.focus()
        selezione = self.tblStoricoGiornate.item(indice)

        try:
            data = selezione['values'][10]
            negozio = selezione['values'][11]
            importo = selezione['values'][0]
            if negozio == puntoVendita:
                eliminaVoce = tkinter.messagebox.askyesno(parent=self.frame8, title='Eliminare voce?',
                                                          message='Sei sicuro di voler eliminare la voce selezionata?')
                if eliminaVoce:
                    databaseOperations.Cassa(1, data=data, puntoVendita=puntoVendita, incassoTotale=importo)

            else:
                tkinter.messagebox.showerror(parent=self, title="Errore Punto Vendita",
                                             message="Non puoi eliminare i record degli altri Punti Vendita")

        except IndexError:
            tkinter.messagebox.showerror(parent=self, title="Nessuna selezione",
                                         message="Seleziona una voce dalla tabella!")

        self.aggiornaCasse()

    def inviaIncasso(self):
        if self.entryIncassoTot.get() != "":
            corrispettivo = round(float(self.corrispettivo.get()), 2)
            fatturato = round(float(self.fatturato.get()), 2)
            contanti = round(float(self.contanti.get()), 2)
            pos = round(float(self.pos.get()), 2)
            finanziamenti = round(float(self.finanziamenti.get()), 2)
            bonifici = round(float(self.bonifici.get()), 2)
            assegni = round(float(self.assegni.get()), 2)
            acconti = round(float(self.acconti.get()), 2)
            preincassato = round(float(self.preincassato.get()), 2)
            incassoTotale = round(float(self.incassoTotale.get()), 2)
            incassoTotale = incassoTotale
            data = self.entryData.get()

            if incassoTotale > 0:
                databaseOperations.Cassa(0, incassoTotale=incassoTotale, corrispettivo=corrispettivo,
                                         fatturato=fatturato, contanti=contanti, pos=pos, finanziamenti=finanziamenti,
                                         bonifici=bonifici, assegni=assegni, acconti=acconti, preincassato=preincassato,
                                         data=data, puntoVendita=puntoVendita)
            elif incassoTotale < 0:
                tkinter.messagebox.showerror(parent=self.frame8, title='Incasso negativo',
                                             message='Impossibile inserire un incasso negativo!')

            elif incassoTotale == 0:
                incasso0 = tkinter.messagebox.askyesno(parent=self.frame8, title='Incasso zero',
                                                       message='Sei sicuro di voler inserire un incasso pari a €0.00')
                if incasso0:
                    databaseOperations.Cassa(0, incassoTotale=incassoTotale, corrispettivo=corrispettivo,
                                             fatturato=fatturato, contanti=contanti, pos=pos,
                                             finanziamenti=finanziamenti, bonifici=bonifici, assegni=assegni,
                                             acconti=acconti, preincassato=preincassato, data=data,
                                             puntoVendita=puntoVendita)

            self.aggiornaCasse()
            self.entryIncassoTot.delete(0, END)
            self.entryCorrispettivo.delete(0, END)
            self.entryFatturato.delete(0, END)
            self.entryContanti.delete(0, END)
            self.entryPOS.delete(0, END)
            self.entryFinanziamenti.delete(0, END)
            self.entryAssegni.delete(0, END)
            self.entryBonifici.delete(0, END)
            self.entryAcconti.delete(0, END)
            self.entry.delete(0, END)
            ####
            self.entry.insert(0, self._default_)
            self.entryContanti.insert(0, self._default_)
            self.entryPOS.insert(0, self._default_)
            self.entryBonifici.insert(0, self._default_)
            self.entryAssegni.insert(0, self._default_)
            self.entryAcconti.insert(0, self._default_)
            self.entryFinanziamenti.insert(0, self._default_)
            self.entryFatturato.insert(0, self._default_)
            self.entryCorrispettivo.insert(0, self._default_)

        else:
            tkinter.messagebox.showerror(parent=self.frame8, title='Verificare quadratura',
                                         message="Assicurarsi di aver verificato la quadratura "
                                                 "prima di inserire l'incasso")

    def aggiornaCasse(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()

        if operatore != 'master':
            _SQLFetch = "SELECT * FROM cassa WHERE puntoVendita = %s ORDER BY data ASC"
            self.cursor.execute(_SQLFetch, (puntoVendita,))

        else:
            self.cursor.execute("SELECT * FROM cassa ORDER BY data ASC")

        giornate = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()

        self.tblStoricoGiornate.delete(*self.tblStoricoGiornate.get_children())

        for giornata in giornate:
            giornata = giornata[1:]
            self.tblStoricoGiornate.insert("", END, values=giornata)

        self.tblStoricoGiornate.yview_moveto(1)


# FINESTRA CHAT#########################################################################################################
class ChatWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM chat")
        self.chat = self.cursor.fetchall()

        self.recuperaUtenti()

        iconaChat = tk.PhotoImage(file='images/chat.png')

        super(ChatWidget, self).__init__(master, **kw)
        self.lfChat = ttk.Labelframe(self)
        self.lbChat = ttk.Treeview(self.lfChat)

        self.lbChat_cols = ['autore', 'messaggio']
        self.lbChat_dcols = ['autore', 'messaggio']

        self.lbChat.configure(columns=self.lbChat_cols, show='headings')

        self.lbChat.column('autore', anchor='w', stretch=False, width=100, minwidth=80)
        self.lbChat.column('messaggio', anchor='w', stretch=True, width=100, minwidth=80)

        self.lbChat.heading('autore', anchor='w', text='Autore')
        self.lbChat.heading('messaggio', anchor='w', text='Messaggio')

        self.lbChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lbChat.yview_moveto(1)
        #self.lbChat.bind('<Double-1>', self.rispondi, add='')
        self.lfChat.configure(height='200', text='Chat utenti', width='200')
        self.lfChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frmNuovoMessaggio = ttk.Frame(self)
        self.frmBoxTesto = ttk.Frame(self.frmNuovoMessaggio)
        '''self.frame5 = ttk.Frame(self.frmBoxTesto)
        self.comboDestinatario = ttk.Combobox(self.frame5)
        self.comboDestinatario.pack(fill='x', side='top')
        self.comboDestinatario.configure(values=self.utentiChat)
        self.frame5.configure(height='20', width='200')
        self.frame5.pack(fill='x', side='top')'''
        self.textMessaggio = tk.Entry(self.frmBoxTesto)
        self.textMessaggio.configure(width='50')
        self.textMessaggio.pack(expand='true', fill='both', side='top')
        self.textMessaggio.bind('<Return>', self.inviaMessaggio)
        self.frmBoxTesto.configure(height='100', width='200')
        self.frmBoxTesto.pack(expand='true', fill='both', pady='5', side='left')
        self.frmButton = ttk.Frame(self.frmNuovoMessaggio)
        self.btnInviaMessaggio = ttk.Button(self.frmButton)
        self.img_send = tk.PhotoImage(file='images/send.png')
        self.btnInviaMessaggio.configure(image=self.img_send, text='Invia')
        self.btnInviaMessaggio.pack(expand='true', fill='y', pady='5', side='top')
        self.btnInviaMessaggio.configure(command=self.inviaMessaggio)
        self.frmButton.configure(height='100', width='100')
        self.frmButton.pack(expand='true', fill='y', side='top')
        self.frmNuovoMessaggio.configure(height='100', width='200')
        self.frmNuovoMessaggio.pack(fill='x', padx='5', side='top')
        self.lbChat.insert("", END, 'Caricamento chat...')
        self.configure(height='200', width='200')
        self.geometry('800x600')
        self.iconphoto(False, iconaChat)
        self.title('Chat postazioni | AB Informatica - StockIt Manager')
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.aggiornamentoChat()
        self.autoAggiornamentoDaemon()

    def onClosing(self):
        self.destroy()

    def recuperaUtenti(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM users")
        self.users = self.cursor.fetchall()
        self.utentiChat = (
            ''
        )
        self.cursor.close()
        self.mydb.close()

        for user in self.users:
            utenteChat = str(user[1]).replace(" ", "_") + " "
            self.utentiChat = self.utentiChat + utenteChat

    def inviaMessaggio(self, event=None):
        autore = nomeUtente
        messaggio = self.textMessaggio.get()
        self.textMessaggio.delete(0, END)
        #destinatario = self.comboDestinatario.get().replace("_", " ")

        if messaggio != "":
            databaseOperations.Chat(autore, messaggio)

            #self.comboDestinatario.delete(0, END)

        self.textMessaggio.delete(0, END)

    def riceviMessaggio(self):
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC LIMIT 1) sub ORDER BY idx ASC")
        messaggio = cursor.fetchone()
        messaggio = messaggio[1:]
        cursor.close()
        mydb.close()
        try:
            self.lbChat.insert("", END, values=messaggio)
            self.lbChat.yview_moveto(1)
        except _tkinter.TclError:
            pass
        text = str(messaggio[0]+": "+str(messaggio[1]))
        '''if messaggio[0] != nomeUtente:
            try:
                notify(
                    BodyText=text,
                    AppName='StockIt Manager',
                    TitleText='Nuovo messaggio',
                    ImagePath='images/chat.png'
                )
            except AttributeError:
                pass'''

    def aggiornamentoChat(self):
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC) sub ORDER BY idx ASC")
        messaggi = cursor.fetchall()
        cursor.close()
        mydb.close()

        self.lbChat.delete(*self.lbChat.get_children())

        for messaggio in messaggi:
            messaggio = messaggio[1:]
            '''y = "  -  ".join([str(value) for value in messaggio])
            y.replace("{", "")
            y.replace("}", "")'''
            self.lbChat.insert("", END, values=messaggio)
            self.lbChat.yview_moveto(1)
            self.textMessaggio.delete(0, END)

    def ricercaAggiornamenti(self):
        while 1:
            # try:
            time.sleep(1)
            mydb = mysql.connector.connect(option_files='connector.cnf')
            cursor = mydb.cursor()
            file1changed = False
            cursor.execute("SELECT * FROM chat")
            NEWChat = cursor.fetchall()
            cursor.close()
            mydb.close()
            if NEWChat != self.chat:
                file1changed = True
                time.sleep(1)
            else:
                file1changed = False

            if file1changed:
                self.chat = NEWChat

                self.riceviMessaggio()

            else:
                pass

    def autoAggiornamentoDaemon(self):
        newthread = threading.Thread(target=self.ricercaAggiornamenti)
        newthread.daemon = True
        newthread.start()
        print("Chat Daemon STARTED\n")


# FINESTRA UTENTI#######################################################################################################
class UtentiWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        iconaUser = tk.PhotoImage(file='images/user.png')

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
        self.comboRuolo.insert(0, 'operatore')
        self.entryPuntoVendita = ttk.Combobox(self.frmEntry)
        self.entryPuntoVendita.configure(values='PV0 PV1 PV2 PV3 PV4')
        self.entryPuntoVendita.insert(0, 'PV0')
        self.entryPuntoVendita.pack(fill='x', side='top')
        self.frmEntry.configure(height='200', width='200')
        self.frmEntry.pack(fill='both', padx='5', pady='5', side='top')
        self.lfInserisciUtente.configure(height='200', text='Inserisci o modifica utente', width='200')
        self.lfInserisciUtente.pack(anchor='n', expand='false', fill='x', padx='5', pady='5', side='top')
        self.lfUtenti = ttk.Labelframe(self)
        self.tblUtenti_cols = ['idx', 'nomeUtente', 'password', 'ruolo', 'puntoVendita']
        self.tblUtenti_dcols = ['idx', 'nomeUtente', 'password', 'ruolo', 'puntoVendita']
        self.tblUtenti = ttk.Treeview(self.lfUtenti, columns=self.tblUtenti_cols, show='headings')
        self.tblUtenti.column('idx', anchor='w', stretch='false', width='67', minwidth='20')
        self.tblUtenti.column('nomeUtente', anchor='w', stretch='true', width='200', minwidth='20')
        self.tblUtenti.column('password', anchor='w', stretch='true', width='200', minwidth='20')
        self.tblUtenti.column('ruolo', anchor='w', stretch='false', width='100', minwidth='20')
        self.tblUtenti.column('puntoVendita', anchor='w', stretch='false', width='200', minwidth='20')
        self.tblUtenti.heading('idx', anchor='w', text='Prog.')
        self.tblUtenti.heading('nomeUtente', anchor='w', text='Nome utente')
        self.tblUtenti.heading('password', anchor='w', text='Password')
        self.tblUtenti.heading('ruolo', anchor='w', text='Ruolo')
        self.tblUtenti.heading('puntoVendita', anchor='w', text='Punto Vendita')
        self.tblUtenti.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.tblUtenti.bind('<Double-1>', self.OnClickTbl, add='')
        self.tblUtenti.yview_moveto(1)
        self.lfUtenti.configure(height='200', text='Utenti', width='200')
        self.lfUtenti.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame7 = ttk.Frame(self)
        self.button1 = ttk.Button(self.frame7)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.button1.configure(image=self.img_plus, text='button1', command=self.inserisciUtente)
        self.button1.pack(padx='5', pady='5', side='right')
        self.button3 = ttk.Button(self.frame7)
        self.img_clean = tk.PhotoImage(file='images/clean.png')
        self.button3.configure(image=self.img_clean, text='button1', command=self.svuotaCampi)
        self.button3.pack(padx='5', pady='5', side='right')
        self.button4 = ttk.Button(self.frame7)
        self.img_delete = tk.PhotoImage(file='images/delete.png')
        self.button4.configure(image=self.img_delete, text='button1', command=self.eliminaUtente)
        self.button4.pack(padx='5', pady='5', side='right')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(fill='x', side='top')
        self.configure(height='200', width='200')
        self.geometry('800x600')
        self.iconphoto(False, iconaUser)
        self.title('Gestione Utenti | AB Informatica - StockIt Manager')

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
        self.cursor.close()
        self.mydb.close()

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
        self.cursor.close()
        self.mydb.close()

        self.tblUtenti.delete(*self.tblUtenti.get_children())

        for utente in utenti:
            self.tblUtenti.insert("", END, values=utente)


# FINESTRA NUOVA COMUNICAZIONE##########################################################################################
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
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.btnComInserisciComunicazione.configure(image=self.img_plus, text='Inserisci comunicazione')
        self.btnComInserisciComunicazione.pack(padx='5', pady='5', side='right')
        self.btnComInserisciComunicazione.configure(command=self.inserisciComunicazione)
        self.btnComSvuotaCampi = ttk.Button(self.frmPulsanti)
        self.img_clean = tk.PhotoImage(file='images/clean.png')
        self.btnComSvuotaCampi.configure(image=self.img_clean, text='Svuota campi')
        self.btnComSvuotaCampi.pack(padx='5', pady='5', side='right')
        self.btnComSvuotaCampi.configure(command=self.svuotaCampi)
        self.frmPulsanti.configure(height='70', width='200')
        self.frmPulsanti.pack(expand='false', fill='x', side='top')
        self.configure(height='200', takefocus=True, width='200')
        self.geometry('800x600')
        self.iconbitmap("chat.ico")
        self.title('Inserisci comunicazione | AB Informatica - StockIt Manager')

    def inserisciComunicazione(self):
        messaggio = self.text1.get(1.0, END)
        data = str(date.today())
        databaseOperations.Comunicazioni(0, 0, nomeUtente, messaggio, data)
        self.svuotaCampi()
        self.destroy()

    def svuotaCampi(self):
        self.text1.delete(1.0, END)


# FINESTRA ASSISTENZA###################################################################################################
class AssistenzaWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):

        iconaAssistenza = tk.PhotoImage(file='images/call-center.png')

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
        self.img_plus = tk.PhotoImage(file='images/plus.png')
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
        self.treeview1.yview_moveto(1)
        self.treeview1.bind('<Double-1>', self.visualizzaPratica)
        #TODO:::ASSISTENZA:::Aggiungi binding e menu contestuale
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
        self.iconphoto(False, iconaAssistenza)
        self.title('Gestione Assistenza | AB Informatica - StockIt Manager')

        self.aggiornamentoOrdini()

    def visualizzaPratica(self, event):
        indice = self.treeview1.focus()
        idx = self.treeview1.item(indice)
        codiceProdotto = str(idx['values'][0])
        window = PraticaAssistenzaWidget(idx=codiceProdotto)
        window.grab_set()

    def nuovaAssistenza(self):
        self.nomeCliente = self.entryAssNomeCliente.get()
        self.nomeCliente = self.nomeCliente + " - P. vendita: " + puntoVendita
        self.contattoCliente = self.entryAssContattoCliente.get()
        self.prodotto = self.entryAssProdotto.get()
        self.difettoProdotto = self.entryAssDifetto.get()
        self.note = self.textAssNote.get(1.0, END)
        self.data = date.today()
        self.nomeCliente = self.nomeCliente.upper()
        self.prodotto = self.prodotto.upper()
        self.difettoProdotto = self.difettoProdotto.upper()
        self.note = self.note.upper()

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

        try:
            notify(
                    BodyText='La pratica è stata inserita correttamente',
                    AppName='StockIt Manager',
                    TitleText='Pratica inserita',
                    ImagePath='icon.ico'
                    )
        except AttributeError:
            pass

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
        self.cursor.close()
        self.mydb.close()

        # PULISCE TABELLA
        self.treeview1.delete(*self.treeview1.get_children())

        for ordine in ordini:
            self.treeview1.insert("", END, values=ordine)


# FINESTRA PRATICA ASSISTENZA###########################################################################################
class PraticaAssistenzaWidget(tk.Toplevel):
    def __init__(self, idx='', master=None, **kw):
        super(PraticaAssistenzaWidget, self).__init__(master, **kw)

        pratica = databaseOperations.GestioneAssistenza().selezionaPratica(idx=idx)

        self.index = idx

        self.labelframe10 = ttk.Labelframe(self)
        self.frame39 = ttk.Frame(self.labelframe10)
        self.label57 = ttk.Label(self.frame39)
        self.label57.configure(text='Progressivo:')
        self.label57.pack(anchor='e', pady='5', side='top')
        self.label51 = ttk.Label(self.frame39)
        self.label51.configure(text='Nome cliente:')
        self.label51.pack(anchor='e', pady='5', side='top')
        self.label54 = ttk.Label(self.frame39)
        self.label54.configure(text='Contatto cliente:')
        self.label54.pack(anchor='e', pady='5', side='top')
        self.label55 = ttk.Label(self.frame39)
        self.label55.configure(text='Prodotto:')
        self.label55.pack(anchor='e', pady='5', side='top')
        self.label56 = ttk.Label(self.frame39)
        self.label56.configure(text='Difetto riscontrato:')
        self.label56.pack(anchor='e', pady='5', side='top')
        self.frame39.configure(height='120', width='120')
        self.frame39.pack(padx='5', side='left')
        self.frame42 = ttk.Frame(self.labelframe10)
        self.entryProgressivo = ttk.Entry(self.frame42)
        self.entryProgressivo.pack(expand='true', fill='x', pady='4', side='top')
        self.entryProgressivo.insert(0, str(pratica[0]))
        self.entryProgressivo.configure(state='disabled')
        self.entryNomeCl = ttk.Entry(self.frame42)
        self.entryNomeCl.pack(expand='true', fill='x', pady='4', side='top')
        self.entryNomeCl.insert(0, str(pratica[1]))
        self.entryContattoCli = ttk.Entry(self.frame42)
        self.entryContattoCli.pack(expand='true', fill='x', pady='4', side='top')
        self.entryContattoCli.insert(0, str(pratica[2]))
        self.entryProdGuasto = ttk.Entry(self.frame42)
        self.entryProdGuasto.pack(expand='true', fill='x', pady='4', side='top')
        self.entryProdGuasto.insert(0, str(pratica[3]))
        self.entryDifetto = ttk.Entry(self.frame42)
        self.entryDifetto.pack(expand='true', fill='x', pady='4', side='top')
        self.entryDifetto.insert(0, str(pratica[4]))
        self.frame42.configure(height='100', width='200')
        self.frame42.pack(expand='true', fill='both', padx='5', side='top')
        self.labelframe10.configure(height='120', text='Dati prodotto', width='200')
        self.labelframe10.pack(fill='x', padx='5', pady='5', side='top')
        self.labelframe11 = ttk.Labelframe(self)
        self.textNote = tk.Text(self.labelframe11)
        self.textNote.configure(height='10', width='50')
        self.textNote.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.textNote.insert(1.0, pratica[6])
        self.labelframe11.configure(height='200', text='Note', width='200')
        self.labelframe11.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame43 = ttk.Frame(self)
        self.btnAggiornaPratica = ttk.Button(self.frame43)
        self.btnAggiornaPratica.configure(text='Aggiorna pratica', command=self.aggiornaPratica)
        self.btnAggiornaPratica.pack(anchor='e', padx='5', pady='5', side='right')
        self.btnLavorazione = ttk.Button(self.frame43)
        self.btnLavorazione.configure(text='In lavorazione', command=self.praticaLavorazione)
        self.btnLavorazione.pack(anchor='e', padx='5', pady='5', side='left')
        self.btnLavorata = ttk.Button(self.frame43)
        self.btnLavorata.configure(text='Lavorata', command=self.praticaLavorata)
        self.btnLavorata.pack(anchor='e', padx='5', pady='5', side='left')
        self.btnRestituita = ttk.Button(self.frame43)
        self.btnRestituita.configure(text='Restituita', command=self.praticaRestituita)
        self.btnRestituita.pack(anchor='e', padx='5', pady='5', side='left')
        self.frame43.configure(height='200', width='200')
        self.frame43.pack(fill='x', side='top')
        self.configure(height='200', width='200')
        self.geometry('600x600')
        self.minsize(600, 600)
        iconaAssistenza = tk.PhotoImage(file='images/call-center.png')
        self.iconphoto(False, iconaAssistenza)
        self.title('Pratica assistenza | AB Informatica - StockIt Manager')
        self.focus_force()

    def aggiornaPratica(self):
        idx = self.entryProgressivo.get()
        nomeCliente = self.entryNomeCl.get()
        contattoCliente = self.entryContattoCli.get()
        prodotto = self.entryProdGuasto.get()
        difettoProdotto = self.entryDifetto.get()
        note = self.textNote.get(1.0, END)

        databaseOperations.GestioneAssistenza().aggiornaPratica(idx, nomeCliente, contattoCliente, prodotto,
                                                                difettoProdotto, note)

        try:
            notify(
                BodyText='La pratica è stata aggiornata correttamente',
                AppName='StockIt Manager',
                TitleText='Pratica aggiornata',
                ImagePath='icon.ico'
            )
        except AttributeError:
            pass

        self.destroy()

    def praticaLavorazione(self):
        valore = self.index
        databaseOperations.GestioneAssistenza(1, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.destroy()

    def praticaLavorata(self):
        valore = self.index
        databaseOperations.GestioneAssistenza(2, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.destroy()

    def praticaRestituita(self):
        valore = self.index
        databaseOperations.GestioneAssistenza(3, valore, nomeCliente="", contattoCliente="", prodotto="",
                                              difettoProdotto="", note="", dataConsegna="")

        self.destroy()


# FINESTRA ORDINI#######################################################################################################
class OrdiniWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        iconaOrdini = tk.PhotoImage(file='images/box1.png')

        super(OrdiniWidget, self).__init__(master, **kw)  # INIZIO BUILD INTERFACCIA ORDINI
        self.lfNuovoOrdine = ttk.Labelframe(self)
        self.frameLabelOrdine = ttk.Frame(self.lfNuovoOrdine)
        self.lblOrdNomeProdotto = ttk.Label(self.frameLabelOrdine)
        self.lblOrdNomeProdotto.configure(text='Nome prodotto:')
        self.lblOrdNomeProdotto.pack(anchor='e', expand=True, side='top')
        self.lblOrdQuantita = ttk.Label(self.frameLabelOrdine)
        self.lblOrdQuantita.configure(text='Quantità:')
        self.lblOrdQuantita.pack(anchor='e', expand=True, side='top')
        self.lblOrdNote = ttk.Label(self.frameLabelOrdine)
        self.lblOrdNote.configure(text='Note:')
        self.lblOrdNote.pack(anchor='e', expand=True, side='top')
        self.lblNomeCliente = ttk.Label(self.frameLabelOrdine)
        self.lblNomeCliente.configure(text='Nome cliente:')
        self.lblNomeCliente.pack(anchor='e', expand=True, side='top')
        self.frameLabelOrdine.configure(width='200')
        self.frameLabelOrdine.pack(expand=False, fill='y', padx='5', pady='5', side='left')
        self.frameEntryOrdine = ttk.Frame(self.lfNuovoOrdine)
        self.entryNomeProdotto = ttk.Entry(self.frameEntryOrdine)
        self.entryNomeProdotto.configure(width=60)
        self.entryNomeProdotto.focus_force()
        self.entryNomeProdotto.pack(expand='true', fill='x', side='top')
        self.entryQuantita = ttk.Entry(self.frameEntryOrdine)
        self.entryQuantita.configure(width='60')
        self.entryQuantita.pack(expand='true', fill='x', side='top')
        self.entryQuantita.insert(0, "0")
        self.entryNoteProdotto = ttk.Entry(self.frameEntryOrdine)
        self.entryNoteProdotto.configure(width='60')
        self.entryNoteProdotto.pack(expand='true', fill='x', side='top')
        self.entryNomeCliente = ttk.Entry(self.frameEntryOrdine)
        self.entryNomeCliente.configure(width='60')
        self.entryNomeCliente.pack(expand='true', fill='x', side='top')
        self.frameEntryOrdine.configure(height='200', width='200')
        self.frameEntryOrdine.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.btnNuovoOrdine = ttk.Button(self.lfNuovoOrdine)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
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

        self.tblOrdiniDaEvadere.bind("d", lambda event: self.eliminaOrdine())
        self.tblOrdiniDaEvadere.bind("e", lambda event: self.evadiOrdine())
        self.tblOrdiniDaEvadere.yview_moveto(1)
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

        self.tblOrdiniEvasi.bind("r", lambda event: self.ordineConsegnato())
        self.tblOrdiniEvasi.yview_moveto(1)
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
        self.iconphoto(False, iconaOrdini)
        self.title('Gestione Ordini | AB Informatica - StockIt Manager')

        self.aggiornamentoOrdini()

    def nuovoOrdine(self):
        self.nomeProdotto = self.entryNomeProdotto.get()
        self.quantita = self.entryQuantita.get()
        self.note = self.entryNoteProdotto.get()
        self.nomeCliente = self.entryNomeCliente.get()

        self.nomeProdotto = self.nomeProdotto.upper()
        self.note = self.note.upper()
        self.nomeCliente = self.nomeCliente.upper()

        if self.nomeProdotto != '' and self.quantita != "0":
            # INSERISCE I DATI NEL DATABASE
            try:
                databaseOperations.GestioneOrdini(0, 0, self.nomeProdotto, self.quantita, self.note, self.nomeCliente,
                                                  puntoVendita)
            except mysql.connector.errors.DatabaseError:
                tkinter.messagebox.showerror(parent=self, title='Valore incorretto', message='Il campo quantità accetta'
                                                                                             ' solo numeri')

            # AGGIORNA LA TABELLA ORDINI
            self.aggiornamentoOrdini()

            # AZZERA I CAMPI
            self.entryNomeProdotto.delete(0, END)
            self.entryQuantita.delete(0, END)
            self.entryNoteProdotto.delete(0, END)
            self.entryNomeCliente.delete(0, END)

        else:
            ErroreOrdine = tkinter.messagebox.showerror(parent=self, title="Compilare i campi",
                                                        message="Assicurati di aver compilato almeno i campi richiesti")

    def eliminaOrdine(self):
        try:
            indice = self.tblOrdiniDaEvadere.focus()
            idx = self.tblOrdiniDaEvadere.item(indice)
            valore = idx['values'][0]

            databaseOperations.GestioneOrdini(3, valore, nomeCliente='', nomeProdotto='', note='', quantity='',
                                              puntoVendita='')

            self.aggiornamentoOrdini()

        except IndexError:
            ErroreSelezioneOrdine = tkinter.messagebox.showerror(parent=self, title="Seleziona ordine da eliminare",
                                                                 message="Seleziona l'ordine da eliminare.\n"
                                                                         "È possibile eliminare solo gli "
                                                                         "ordini inevasi")

    def evadiOrdine(self):
        curItems = self.tblOrdiniDaEvadere.selection()
        for idx in curItems:
            index = self.tblOrdiniDaEvadere.item(idx)
            valore = index['values'][0]
            databaseOperations.GestioneOrdini(1, valore, nomeCliente='', nomeProdotto='', note='', quantity='',
                                              puntoVendita='')

        self.aggiornamentoOrdini()

    def ordineConsegnato(self):
        curItems = self.tblOrdiniEvasi.selection()
        for idx in curItems:
            index = self.tblOrdiniEvasi.item(idx)
            valore = index['values'][0]
            databaseOperations.GestioneOrdini(2, valore, nomeCliente='', nomeProdotto='', note='', quantity='',
                                              puntoVendita='')

            nomeProdotto = index['values'][1]
            qty = int(index['values'][2])

            if nomeProdotto.startswith('*'):
                nomeProdotto = nomeProdotto.replace('*', '')
                prodotto = nomeProdotto.split(',')
                cod = str(prodotto[0])
                mag = str(prodotto[1]).split(' - ')
                mag = int(mag[0])
                switch1 = mag + 7
                magDest = int(puntoVendita.replace('PV', ''))
                switch2 = magDest + 7

                prodotto = databaseOperations.GestioneMagazzino().ricercaMagazzino(ricerca='codice', codice=cod)
                prodotto = prodotto[0]
                qtyprov = int(prodotto[switch1])
                qtydest = int(prodotto[switch2])

                n1 = qtyprov-qty
                n2 = qtydest+qty

                databaseOperations.GestioneMagazzino().trasferisciProdotto(codice=cod, provenienza=mag,
                                                                           destinazione=magDest, qprov=n1, qdest=n2)


                #print('Prodotto cod. ' + cod + ' trasferito da magazzino ' + mag + ' a magazzino ' + magDest)

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
        self.cursor.close()
        self.mydb.close()

        # PULISCE TABELLA
        self.tblOrdiniEvasi.delete(*self.tblOrdiniEvasi.get_children())

        for ordine in ordini:
            self.tblOrdiniEvasi.insert("", END, values=ordine)


# FINESTRA NUOVO ORDINE#################################################################################################
class InserisciOrdineWidget(tk.Toplevel):
    def __init__(self, master=None, nome='', **kw):
        super(InserisciOrdineWidget, self).__init__(master, **kw)

        iconaOrdini = tk.PhotoImage(file='images/box1.png')

        self.labelframe5 = ttk.Labelframe(self)
        self.frame18 = ttk.Frame(self.labelframe5)
        self.label14 = ttk.Label(self.frame18)
        self.label14.configure(text='Nome prodotto:')
        self.label14.pack(anchor='e', expand='true', side='top')
        self.label16 = ttk.Label(self.frame18)
        self.label16.configure(text='Quantità:')
        self.label16.pack(anchor='e', expand='true', side='top')
        self.label18 = ttk.Label(self.frame18)
        self.label18.configure(text='Note:')
        self.label18.pack(anchor='e', expand='true', side='top')
        self.label19 = ttk.Label(self.frame18)
        self.label19.configure(text='Nome cliente:')
        self.label19.pack(anchor='e', expand='true', side='top')
        self.frame18.configure(width='200')
        self.frame18.pack(expand='false', fill='y', padx='5', pady='5', side='left')
        self.frame19 = ttk.Frame(self.labelframe5)
        self.entryNomeProdotto1 = ttk.Entry(self.frame19)
        self.entryNomeProdotto1.configure(width='60')
        self.entryNomeProdotto1.insert(0, nome)
        self.entryNomeProdotto1.focus_force()
        self.nomeTip = Hovertip(self.entryNomeProdotto1, "Inserisci il nome prodotto")
        self.entryNomeProdotto1.pack(expand='true', fill='x', side='top')
        self.entryQuantita1 = ttk.Entry(self.frame19)
        self.entryQuantita1.configure(width='60')
        self.entryQuantita1.insert(END, '0')
        self.entryQuantita1.pack(expand='true', fill='x', side='top')
        self.entryNote1 = ttk.Entry(self.frame19)
        self.entryNote1.configure(width='60')
        self.entryNote1.pack(expand='true', fill='x', side='top')
        self.entryNomeCliente1 = ttk.Entry(self.frame19)
        self.entryNomeCliente1.configure(width='60')
        self.entryNomeCliente1.pack(expand='true', fill='x', side='top')
        self.frame19.configure(height='200', width='200')
        self.frame19.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.button7 = ttk.Button(self.labelframe5)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.button7.configure(image=self.img_plus, text='Inserisci')
        self.button7.pack(expand='true', fill='y', padx='5', pady='5', side='top')
        self.button7.configure(command=self.nuovoOrdine)
        self.labelframe5.configure(height='200', text='Nuovo Ordine', width='200')
        self.labelframe5.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.configure(height='200', width='200')
        self.geometry('640x200')
        self.resizable(False, False)
        self.iconphoto(False, iconaOrdini)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.title('Inserisci ordine | AB Informatica - StockIt Manager')

    def nuovoOrdine(self):
        self.nomeProdotto = self.entryNomeProdotto1.get()
        self.quantita = self.entryQuantita1.get()
        self.note = self.entryNote1.get()
        self.nomeCliente = self.entryNomeCliente1.get()

        self.nomeProdotto = self.nomeProdotto.upper()
        self.note = self.note.upper()
        self.nomeCliente = self.nomeCliente.upper()

        if self.nomeProdotto != '' and self.quantita != "0":
            # INSERISCE I DATI NEL DATABASE
            databaseOperations.GestioneOrdini(0, 0, self.nomeProdotto, self.quantita, self.note, self.nomeCliente,
                                              puntoVendita)

            # AZZERA I CAMPI
            self.entryNomeProdotto1.delete(0, END)
            self.entryQuantita1.delete(0, END)
            self.entryNote1.delete(0, END)
            self.entryNomeCliente1.delete(0, END)
            tkinter.messagebox.showinfo(parent=self, title="Ordine inserito", message="L'ordine è stato inserito"
                                                                                      " correttamente!")
            self.destroy()
            OrdiniWidget()

        else:
            ErroreOrdine = tkinter.messagebox.showerror(parent=self, title="Compilare i campi",
                                                        message="Assicurati di aver compilato almeno i campi richiesti")

            self.destroy()

    def on_closing(self):
        self.destroy()


# FINESTRA LEGGI COMUNICAZIONE##########################################################################################
class LeggiComunicazioneWidget(tk.Toplevel):
    def __init__(self, master=None, text="", **kw):
        super(LeggiComunicazioneWidget, self).__init__(master, **kw)
        self.labelframe6 = ttk.Labelframe(self)
        self.focus_force()
        self.text = tk.Text(self.labelframe6)
        self.text.configure(height='10', state='normal', width='50')
        self.text.insert(1.0, text)
        self.text.configure(state='disabled')
        self.text.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.labelframe6.configure(height='200', text='Comunicazione', width='200')
        self.labelframe6.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.configure(height='200', width='200')
        self.iconbitmap('chat.ico')
        self.title('Leggi comunicazione | AB Informatica - StockIt Manager')
        self.geometry('800x600')


# FINESTRA STAMPE#######################################################################################################
class StampeWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        iconaStampe = tk.PhotoImage(file='images/printer.png')

        super(StampeWidget, self).__init__(master, **kw)
        self.focus_force()
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
        if operatore != 'operatore':
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

        #TODO: Inserire stampe buoni spesa e stampe magazzino
        '''self.lfStampeBuoniSpesa = ttk.Labelframe(self)
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
        self.lfStampeComunicazioni.pack(expand='true', fill='both', pady='5', side='top')'''
        self.configure(height='200', width='200')
        self.geometry('300x480')
        self.title("Stampe")
        self.iconphoto(False, iconaStampe)
        self.resizable(False, False)

    def stampaOrdini(self):
        PDFOperations.StampaOrdine(switch=0)
        self.destroy()

    def stampaEvasi(self):
        PDFOperations.StampaOrdine(switch=1)
        self.destroy()

    def stampaConsegnati(self):
        PDFOperations.StampaOrdine(switch=2)
        self.destroy()

    def stampaNuovePratiche(self):
        PDFOperations.StampaAssistenza(switch=0)
        self.destroy()

    def stampaPraticheLavorazione(self):
        PDFOperations.StampaAssistenza(switch=1)
        self.destroy()

    def stampaPraticheLavorate(self):
        PDFOperations.StampaAssistenza(switch=2)
        self.destroy()

    def stampaReportData(self):
        self.destroy()
        PDFOperations.InserisciDataWidget(root, switch=2, operatore=operatore, puntoVendita=puntoVendita)

    def stampaReportMese(self):
        self.destroy()
        PDFOperations.InserisciDataWidget(root, switch=1, operatore=operatore, puntoVendita=puntoVendita)

    def stampaReportAnno(self):
        self.destroy()
        PDFOperations.InserisciDataWidget(root, switch=0, operatore=operatore, puntoVendita=puntoVendita)

    def stampaReportBuoni(self):
        pass

    def stampaReportPerCarta(self):
        pass

    def stampaComunicazione(self):
        pass


# CREDITS################################################################################################################
class CreditsWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(CreditsWidget, self).__init__(master, **kw)
        self.focus_force()
        self.label20 = ttk.Label(self)
        self.label20.configure(font='{Consolas} 20 {bold}', text='AB Informatica')
        self.label20.pack(pady='10', side='top')
        self.label21 = ttk.Label(self)
        self.label21.configure(font='{Consolas} 24 {bold}', justify='center', text='StockIt Manager')
        self.label21.pack(expand='false', pady='10', side='top')
        self.label22 = ttk.Label(self)
        self.label22.configure(anchor='center', font='{Arial} 16 {}', justify='center', text='''Augusto Burzo
info@augustoburzo.com
+39 379 146 48 24

-------------------------------------------------------------

Icone:
Flaticon
Freepik''')
        self.label22.pack(expand='true', fill='both', side='top')
        self.configure(height='200', width='200')
        self.geometry('640x480')
        self.iconbitmap('icon.ico')
        self.resizable(False, False)
        self.title('Credits')


# FINESTRA INSERISCI DOCUMENTO##########################################################################################
class InserisciDocumentoWidget(tk.Toplevel):
    def __init__(self, master=None, viewonly=False, **kw):
        super(InserisciDocumentoWidget, self).__init__(master, **kw)

        aliquote = databaseOperations.Settings().aliquoteIva()

        self.labelframe4 = ttk.Labelframe(self)
        self.frame22 = ttk.Frame(self.labelframe4)
        self.label25 = ttk.Label(self.frame22)
        self.label25.configure(text='Fornitore:')
        self.label25.pack(anchor='e', side='top')
        self.label27 = ttk.Label(self.frame22)
        self.label27.configure(text='N° documento:')
        self.label27.pack(anchor='e', side='top')
        self.label28 = ttk.Label(self.frame22)
        self.label28.configure(text='Tot. documento:')
        self.label28.pack(anchor='e', side='top')
        self.label29 = ttk.Label(self.frame22)
        self.label29.configure(text='Data documento:')
        self.label29.pack(anchor='e', side='top')
        self.label30 = ttk.Label(self.frame22)
        self.label30.configure(text='Tipo documento:')
        self.label30.pack(anchor='e', side='top')
        self.frame22.configure(height='200', width='200')
        self.frame22.pack(anchor='center', padx='5', side='left')
        self.frame24 = ttk.Frame(self.labelframe4)
        self.entryFornitore = ttk.Entry(self.frame24)
        self.entryFornitore.configure(width='80')
        self.entryFornitore.pack(fill='x', side='top')
        self.entryFornitore.focus_force()
        self.entryNumDoc = ttk.Entry(self.frame24)
        self.entryNumDoc.pack(fill='x', side='top')
        self.entryTotDoc = ttk.Entry(self.frame24)
        self.entryTotDoc.pack(fill='x', side='top')
        self.entryDataDoc = ttk.Entry(self.frame24)
        self.entryDataDoc.pack(fill='x', side='top')
        self.entryDataDoc.insert(0, date.today())
        self.comboTipoDoc = ttk.Combobox(self.frame24)
        self.comboTipoDoc.pack(fill='x', side='top')
        self.frame24.configure(height='200', width='200')
        self.frame24.pack(anchor='center', expand='true', fill='x', padx='5', side='left')
        self.labelframe4.configure(height='200', text='Inserisci documento', width='800')
        self.labelframe4.pack(fill='x', padx='5', pady='5', side='top')
        self.labelframe8 = ttk.Labelframe(self)
        self.frame23 = ttk.Frame(self.labelframe8)
        self.label23 = ttk.Label(self.frame23)
        self.label23.configure(text='Codice prodotto:')
        self.label23.pack(anchor='e', pady='1', side='top')
        self.label38 = ttk.Label(self.frame23)
        self.label38.configure(text='Nome prodotto:')
        self.label38.pack(anchor='e', pady='1', side='top')
        self.label24 = ttk.Label(self.frame23)
        self.label24.configure(text='EAN:')
        self.label24.pack(anchor='e', pady='1', side='top')
        self.label26 = ttk.Label(self.frame23)
        self.label26.configure(text='Quantità:')
        self.label26.pack(anchor='e', pady='1', side='top')
        self.label31 = ttk.Label(self.frame23)
        self.label31.configure(text='Regime IVA:')
        self.label31.pack(anchor='e', pady='1', side='top')
        self.label32 = ttk.Label(self.frame23)
        self.label32.configure(text='Cat. prodotto:')
        self.label32.pack(anchor='e', pady='1', side='top')
        self.label36 = ttk.Label(self.frame23)
        self.label36.configure(text='Costo:')
        self.label36.pack(anchor='e', pady='1', side='top')
        self.label37 = ttk.Label(self.frame23)
        self.label37.configure(text='Prezzo vendita:')
        self.label37.pack(anchor='e', pady='1', side='top')
        self.frame23.configure(height='200', width='200')
        self.frame23.pack(padx='5', side='left')
        self.frame25 = ttk.Frame(self.labelframe8)
        self.frame26 = ttk.Frame(self.frame25)
        self.entryCodProdDoc = ttk.Entry(self.frame26)
        self.entryCodProdDoc.configure(width='80')
        self.entryCodProdDoc.pack(fill='x', side='left', expand=True)
        self.cercaProdottoBtn = ttk.Button(self.frame26)
        self.cercaProdottoBtn.configure(text='Cerca...', command=self.onReturn)
        self.cercaProdottoBtn.pack(fill='x', side='right')
        self.frame26.pack(fill='x', side='top')
        self.entryNomeProdDoc = ttk.Entry(self.frame25)
        self.entryNomeProdDoc.configure(width='50')
        self.entryNomeProdDoc.pack(fill='x', side='top')
        self.entryEANProdDoc = ttk.Entry(self.frame25)
        self.entryEANProdDoc.pack(fill='x', side='top')
        self.entryQtyProdDoc = ttk.Entry(self.frame25)
        self.entryQtyProdDoc.pack(fill='x', side='top')
        self.comboIVAProdDoc = ttk.Combobox(self.frame25)
        self.comboIVAProdDoc.configure(values=aliquote)
        self.comboIVAProdDoc.current(END)
        self.comboIVAProdDoc.pack(fill='x', side='top')
        self.comboCatProdDoc = ttk.Combobox(self.frame25)
        self.comboCatProdDoc.pack(fill='x', side='top')
        self.entryCostoProdDoc = ttk.Entry(self.frame25)
        self.entryCostoProdDoc.pack(fill='x', side='top')
        self.entryPrezzoProdDoc = ttk.Entry(self.frame25)
        self.entryPrezzoProdDoc.pack(fill='x', side='top')
        self.frame25.configure(height='200', width='200')
        self.frame25.pack(expand='true', fill='x', padx='5', side='left')
        self.labelframe8.configure(height='200', text='Inserisci prodotti', width='200')
        self.labelframe8.pack(expand='false', fill='x', padx='5', pady='5', side='top')
        self.frame29 = ttk.Frame(self)
        self.btnInserisciProdDoc = ttk.Button(self.frame29)
        self.btnInserisciProdDoc.configure(text='Inserisci prodotto')
        self.btnInserisciProdDoc.pack(padx='5', pady='5', side='right')
        self.btnInserisciProdDoc.configure(command=self.inserisciProdottoDoc)
        self.frame29.configure(height='200', width='200')
        self.frame29.pack(fill='x', side='top')
        self.frame31 = ttk.Frame(self)
        self.treeview3 = ttk.Treeview(self.frame31)
        self.treeview3_cols = ['codice', 'nomeProdotto', 'ean', 'quantity', 'iva', 'categoria', 'costo', 'prezzo']
        self.treeview3_dcols = ['codice', 'nomeProdotto', 'ean', 'quantity', 'iva', 'categoria', 'costo', 'prezzo']
        self.treeview3.configure(columns=self.treeview3_cols, show='headings', height=5)
        self.treeview3.column('codice', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview3.column('nomeProdotto', anchor='w',stretch='true',width='200',minwidth='20')
        self.treeview3.column('ean', anchor='w',stretch='true',width='30',minwidth='20')
        self.treeview3.column('quantity', anchor='w',stretch='true',width='10',minwidth='20')
        self.treeview3.column('iva', anchor='w',stretch='true',width='10',minwidth='20')
        self.treeview3.column('categoria', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview3.column('costo', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview3.column('prezzo', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview3.heading('codice', anchor='w',text='Cod.')
        self.treeview3.heading('nomeProdotto', anchor='w',text='Nome prodotto')
        self.treeview3.heading('ean', anchor='w',text='EAN')
        self.treeview3.heading('quantity', anchor='w',text='Qnt.')
        self.treeview3.heading('iva', anchor='w',text='IVA')
        self.treeview3.heading('categoria', anchor='w',text='Categoria')
        self.treeview3.heading('costo', anchor='w',text='Costo')
        self.treeview3.heading('prezzo', anchor='w',text='Prezzo di vendita')
        self.treeview3.pack(expand='true', fill='both', padx='5', side='top')
        self.frame31.configure(height='200', width='200')
        self.frame31.pack(anchor='center', expand='true', fill='both', side='top')
        self.frame32 = ttk.Frame(self)
        self.btnInserisciDocumento = ttk.Button(self.frame32)
        self.img_plus = tk.PhotoImage(file='images/plus.png')
        self.btnInserisciDocumento.configure(image=self.img_plus, text='button13')
        self.btnInserisciDocumento.pack(anchor='e', expand='false', fill='y', padx='5', pady='5', side='right')
        self.btnInserisciDocumento.configure(command=self.inserisciDocumento)
        '''self.btnNuovoDocumento = ttk.Button(self.frame32)
        #TODO: Definisci funzione "Nuovo documento"
        self.img_contract = tk.PhotoImage(file='images/contract.png')
        self.btnNuovoDocumento.configure(image=self.img_contract, text='button13')
        self.btnNuovoDocumento.pack(anchor='e', expand='false', fill='y', pady='5', side='right')
        self.btnNuovoDocumento.configure(command=self.nuovoDocumento)'''
        self.frame32.configure(height='200', width='200')
        self.frame32.pack(expand='false', fill='x', side='top')
        self.geometry('1024x600')
        self.img_contract = tk.PhotoImage(file='images/contract.png')
        self.iconphoto(True, self.img_contract)
        self.title('Inserimento documento | AB Informatica StockIt Manager')

    def inserisciProdottoDoc(self):
        codice = self.entryCodProdDoc.get()
        nome = self.entryNomeProdDoc.get()
        ean = self.entryEANProdDoc.get()
        quantita = self.entryQtyProdDoc.get()
        iva = self.comboIVAProdDoc.get()
        categoria = self.comboCatProdDoc.get()
        costo = self.entryCostoProdDoc.get()
        prezzo = self.entryPrezzoProdDoc.get()

        prodottoEsistente = databaseOperations.GestioneMagazzino().prodottoEsistente(ean=ean, codice=codice)

        if prodottoEsistente:
            #tkinter.messagebox.showerror(parent=self, title='Prodotto esistente', message='Il prodotto esiste già:')
            prodottoInMagazzino = databaseOperations.GestioneMagazzino().leggiProdottoEsistente(ean=ean, codice=codice)
            codice = prodottoInMagazzino[0]
            nome = prodottoInMagazzino[1]
            ean = prodottoInMagazzino[2]
            quantitaOLD = prodottoInMagazzino[7]
            iva = prodottoInMagazzino[3]
            categoria = prodottoInMagazzino[4]
            costoOLD = prodottoInMagazzino[5]
            prezzo = prodottoInMagazzino[6]
            self.aggiornaProdotto(codice=codice, nome=nome, ean=ean, regime=iva, categoria=categoria, prezzo=prezzo)

        if not prodottoEsistente:
            riga = (
                codice, nome, ean, quantita, iva, categoria, costo, prezzo
            )
            self.treeview3.insert("", END, values=riga)

            self.entryCodProdDoc.delete(0, END)
            self.entryNomeProdDoc.delete(0, END)
            self.entryEANProdDoc.delete(0, END)
            self.entryQtyProdDoc.delete(0, END)
            self.comboIVAProdDoc.delete(0, END)
            self.comboCatProdDoc.delete(0, END)
            self.entryCostoProdDoc.delete(0, END)
            self.entryPrezzoProdDoc.delete(0, END)

    def aggiornaProdotto(self, codice, nome, ean, regime, categoria, prezzo):
        self.finestra = tk.Toplevel(self)
        self.labelframe7 = ttk.Labelframe(self.finestra)
        self.frame33 = ttk.Frame(self.labelframe7)
        self.label39 = ttk.Label(self.frame33)
        self.label39.configure(text='Codice prodotto:')
        self.label39.pack(anchor='e', pady='1', side='top')
        self.label40 = ttk.Label(self.frame33)
        self.label40.configure(text='Nome prodotto:')
        self.label40.pack(anchor='e', pady='1', side='top')
        self.label41 = ttk.Label(self.frame33)
        self.label41.configure(text='EAN:')
        self.label41.pack(anchor='e', pady='1', side='top')
        self.label42 = ttk.Label(self.frame33)
        self.label42.configure(text='Quantità in documento:')
        self.label42.pack(anchor='e', pady='1', side='top')
        self.label43 = ttk.Label(self.frame33)
        self.label43.configure(text='Regime IVA:')
        self.label43.pack(anchor='e', pady='1', side='top')
        self.label44 = ttk.Label(self.frame33)
        self.label44.configure(text='Cat. prodotto:')
        self.label44.pack(anchor='e', pady='1', side='top')
        self.label45 = ttk.Label(self.frame33)
        self.label45.configure(text='Costo:')
        self.label45.pack(anchor='e', pady='1', side='top')
        self.label46 = ttk.Label(self.frame33)
        self.label46.configure(text='Prezzo vendita:')
        self.label46.pack(anchor='e', pady='1', side='top')
        self.frame33.configure(height='200', width='200')
        self.frame33.pack(padx='5', side='left')
        self.frame34 = ttk.Frame(self.labelframe7)
        self.entry4 = ttk.Entry(self.frame34)
        self.entry4.configure(width='80')
        self.entry4.pack(fill='x', side='top')
        self.entry5 = ttk.Entry(self.frame34)
        self.entry5.configure(width='50')
        self.entry5.pack(fill='x', side='top')
        self.entry6 = ttk.Entry(self.frame34)
        self.entry6.pack(fill='x', side='top')
        self.entry8 = ttk.Entry(self.frame34)
        self.entry8.pack(fill='x', side='top')
        self.combobox3 = ttk.Combobox(self.frame34)
        self.combobox3.pack(fill='x', side='top')
        self.combobox4 = ttk.Combobox(self.frame34)
        self.combobox4.pack(fill='x', side='top')
        self.entry9 = ttk.Entry(self.frame34)
        self.entry9.pack(fill='x', side='top')
        self.entry10 = ttk.Entry(self.frame34)
        self.entry10.pack(fill='x', side='top')
        self.frame34.configure(height='200', width='200')
        self.frame34.pack(expand='true', fill='x', padx='5', side='left')
        self.labelframe7.configure(height='200', text='Aggiorna prodotti', width='200')
        self.labelframe7.pack(expand='false', fill='x', padx='5', pady='5', side='top')
        self.frame35 = ttk.Frame(self.finestra)
        self.button6 = ttk.Button(self.frame35)
        self.button6.configure(text='Inserisci prodotto')
        self.button6.pack(padx='5', pady='5', side='right')
        self.button6.configure(command=self.aggiornaProdottoDoc)
        self.frame35.configure(height='200', width='200')
        self.frame35.pack(fill='x', side='top')
        self.finestra.configure(height='200', width='200')
        self.finestra.resizable(False, False)
        self.finestra.title('Aggiorna prodotto | AB Informatica StockIt Manager')

        self.entry4.insert(0, codice)
        self.entry5.insert(0, nome)
        self.entry6.insert(0, ean)
        self.combobox3.insert(0, regime)
        self.combobox4.insert(0, categoria)
        self.entry10.insert(0, prezzo)

    def aggiornaProdottoDoc(self):
        codice = self.entry4.get()
        nome = self.entry5.get()
        ean = self.entry6.get()
        quantita = self.entry8.get()
        iva = self.combobox3.get()
        categoria = self.combobox4.get()
        costo = self.entry9.get()
        prezzo = self.entry10.get()
        riga = (
            codice, nome, ean, quantita, iva, categoria, costo, prezzo
        )
        self.treeview3.insert("", END, values=riga)

        self.finestra.destroy()

    def onReturn(self):
        codice = self.entryCodProdDoc.get()
        listaProdotti = databaseOperations.GestioneMagazzino().ricercaMagazzino(ricerca='codice', codice=codice)
        if listaProdotti != 1:
            prodottoInMagazzino = databaseOperations.GestioneMagazzino().leggiProdottoEsistente(codice=codice)
            codice = prodottoInMagazzino[0]
            nome = prodottoInMagazzino[1]
            ean = prodottoInMagazzino[2]
            quantitaOLD = prodottoInMagazzino[7]
            iva = prodottoInMagazzino[3]
            categoria = prodottoInMagazzino[4]
            costoOLD = prodottoInMagazzino[5]
            prezzo = prodottoInMagazzino[6]
            self.aggiornaProdotto(codice=codice, nome=nome, ean=ean, regime=iva, categoria=categoria, prezzo=prezzo)
        if listaProdotti == 1:
            tkinter.messagebox.showinfo(parent=self, title='Prodotto non presente',
                                        message='Il codice inserito non corrisponde a nessun prodotto in magazzino!')

    def inserisciDocumento(self):
        listaProdotti = ''
        fornitoreReale = self.entryFornitore.get()
        numeroDocumento = self.entryNumDoc.get()
        dataDocumento = self.entryDataDoc.get()
        tipoDocumento = self.comboCatProdDoc.get()
        totaleDocumento = self.entryTotDoc.get()
        for child in self.treeview3.get_children():
            prodotto = self.treeview3.item(child)["values"]

            codice = prodotto[0]
            nome = prodotto[1]
            ean = prodotto[2]
            quantita = prodotto[3]
            iva = prodotto[4]
            categoria = prodotto[5]
            costo = prodotto[6]
            prezzo = prodotto[7]
            singoloProdotto = str(prodotto)
            singoloProdotto = singoloProdotto.replace("[","")
            singoloProdotto = singoloProdotto.replace("]","")
            singoloProdotto = singoloProdotto.replace("'","")
            listaProdotti = listaProdotti + singoloProdotto + ';\n'

            fornitore = str(fornitoreReale) + " - " + str(numeroDocumento) + " - " + str(dataDocumento) + " - " + \
                        str(costo) + ";\n"
            esiste = False

            try:
                databaseOperations.GestioneMagazzino().inserisciProdotto(codice, nome, ean, iva, quantita, categoria,
                                                                         costo, prezzo, fornitore)
            except mysql.connector.errors.IntegrityError:
                esiste = True

            if esiste:
                prodottoInMagazzino = databaseOperations.GestioneMagazzino().leggiProdottoEsistente(ean=ean,
                                                                                                    codice=codice)
                quantitaOLD = prodottoInMagazzino[7]
                fornitoreOLD = prodottoInMagazzino[12]
                fornitoreNEW = fornitore + fornitoreOLD
                newQty = int(quantitaOLD)+int(quantita)
                databaseOperations.GestioneMagazzino().aggiornaProdotto(
                    codice=codice, nome=nome, ean=ean, iva=iva, categoria=categoria, costo=costo, prezzo=prezzo,
                quantita=newQty, fornitore=fornitoreNEW)

        try:
            databaseOperations.GestioneMagazzino().inserisciDocumento(numero=numeroDocumento, fornitore=fornitoreReale,
                                                                      data=dataDocumento, tipo=tipoDocumento,
                                                                      importo=totaleDocumento, prodotti=listaProdotti)
            try:
                notify(
                    BodyText='Il documento è stato inserita correttamente',
                    AppName='StockIt Manager',
                    TitleText='Documento inserito',
                    ImagePath='icon.ico'
                )
            except AttributeError:
                pass

        except mysql.connector.errors.IntegrityError:
            tkinter.messagebox.showerror(parent=self, title='Documento già presente', message='Il numero documento '
                                                                                              'indicato è già presente'
                                                                                              ' nel database!')


# FINESTRA RICERCA PRODOTTI#############################################################################################
class RicercaProdottiWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(RicercaProdottiWidget, self).__init__(master, **kw)
        self.lfRicercaProdMag = ttk.Labelframe(self)
        self.frame27 = ttk.Frame(self.lfRicercaProdMag)
        self.label33 = ttk.Label(self.frame27)
        self.label33.configure(text='Nome prodotto:')
        self.label33.pack(anchor='e', side='top')
        self.label34 = ttk.Label(self.frame27)
        self.label34.configure(text='Cod. prodotto:')
        self.label34.pack(anchor='e', side='top')
        self.label35 = ttk.Label(self.frame27)
        self.label35.configure(text='EAN:')
        self.label35.pack(anchor='e', side='top')
        self.frame27.configure(height='200', width='200')
        self.frame27.pack(padx='5', side='left')
        self.frame28 = ttk.Frame(self.lfRicercaProdMag)
        self.entryRicNomeProdotto = ttk.Entry(self.frame28)
        self.entryRicNomeProdotto.pack(fill='x', side='top')
        self.entryRicNomeProdotto.bind('<FocusIn>', self.nomeFocus)
        self.entryRicCodProd = ttk.Entry(self.frame28)
        self.entryRicCodProd.pack(fill='x', side='top')
        self.entryRicCodProd.bind('<FocusIn>', self.codFocus)
        self.entryRicEANProd = ttk.Entry(self.frame28)
        self.entryRicEANProd.pack(fill='x', side='top')
        self.entryRicEANProd.bind('<FocusIn>', self.eanFocus)
        self.frame28.configure(height='100', width='200')
        self.frame28.pack(expand='true', fill='x', side='left')
        self.btnSearch = ttk.Button(self.lfRicercaProdMag)
        self.img_magnifyingglass = tk.PhotoImage(file='images/magnifying-glass.png')
        self.btnSearch.configure(image=self.img_magnifyingglass, text='button6', command=self.ricercaProdotto)
        self.btnSearch.pack(padx='5', pady='5', side='bottom')
        self.lfRicercaProdMag.configure(height='100', text='Ricerca prodotto', width='200')
        self.lfRicercaProdMag.pack(fill='x', padx='5', pady='5', side='top')
        self.frame30 = ttk.Frame(self)
        self.tblProdotti = ttk.Treeview(self.frame30)
        self.tblProdotti_cols = ['codiceProdotto', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9', 'column18']
        self.tblProdotti_dcols = ['codiceProdotto', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9', 'column18']
        self.tblProdotti.configure(columns=self.tblProdotti_cols, show='headings')
        self.tblProdotti.column('codiceProdotto', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column2', anchor='w',stretch='true',width='200',minwidth='20')
        self.tblProdotti.column('column3', anchor='w',stretch='true',width='35',minwidth='20')
        self.tblProdotti.column('column4', anchor='w',stretch='true',width='200',minwidth='20')
        self.tblProdotti.column('column5', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column6', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column7', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column8', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column9', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.column('column18', anchor='w',stretch='true',width='20',minwidth='20')
        self.tblProdotti.heading('codiceProdotto', anchor='w',text='Cod.')
        self.tblProdotti.heading('column2', anchor='w',text='Nome prodotto')
        self.tblProdotti.heading('column3', anchor='w',text='EAN')
        self.tblProdotti.heading('column4', anchor='w',text='Fornitore')
        self.tblProdotti.heading('column5', anchor='w',text='Mag. 0')
        self.tblProdotti.heading('column6', anchor='w',text='Mag. 1')
        self.tblProdotti.heading('column7', anchor='w',text='Mag. 2')
        self.tblProdotti.heading('column8', anchor='w',text='Mag. 3')
        self.tblProdotti.heading('column9', anchor='w',text='Mag. 4')
        self.tblProdotti.heading('column18', anchor='w',text='Prezzo')
        self.tblProdotti.pack(expand='true', fill='both', side='top')
        self.tblProdotti.bind('<Double-1>', self.callback, add='')
        self.tblProdotti.bind('<Button-3>', self.popup)

        self.frame30.configure(height='200', width='200')
        self.frame30.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frmButtons = ttk.Frame(self)
        self.btnVendi = ttk.Button(self.frmButtons)
        self.btnVendi.configure(text="Scarica prodotto", command=self.vendita)
        self.btnVendi.pack(anchor='w')
        self.frmButtons.pack(fill='x', expand=False, padx=5, pady=5)
        self.img_warehouse = tk.PhotoImage(file='images/warehouse.png')
        self.configure(height='200', width='200')
        self.geometry('1024x600')
        self.iconphoto(True, self.img_warehouse)
        self.title('Visualizza magazzino | AB Informatica StockIt Manager')
        self.focus_force()

        self.gestioneMagazzino = databaseOperations.GestioneMagazzino()
        self.listaMagazzino()

    def vendita(self):
        indice = self.tblProdotti.focus()
        idx = self.tblProdotti.item(indice)
        cod = str(idx['values'][0])
        magazzino = puntoVendita
        vendi = inserisciVenditaWidget(codeProdotto=cod, magazzino=magazzino)
        self.destroy()
    def nomeFocus(self, event):
        self.entryRicEANProd.delete(0, END)
        self.entryRicCodProd.delete(0, END)

    def eanFocus(self, event):
        self.entryRicCodProd.delete(0, END)
        self.entryRicNomeProdotto.delete(0, END)

    def codFocus(self, event):
        self.entryRicEANProd.delete(0, END)
        self.entryRicNomeProdotto.delete(0, END)

    def popup(self, event):
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Ordina prodotto", command=self.ordinaProdotto)
        m.add_separator()
        m.add_command(label="Visualizza prodotto", command=self.visualizzaProdotto)
        m.add_command(label="Elimina prodotto", command=self.eliminaProdotto)

        iid = self.tblProdotti.identify_row(event.y)
        if iid:
            self.tblProdotti.selection_set(iid)
            self.tblProdotti.focus(iid)
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        else:
            pass

    def ordinaProdotto(self):
        magazzinoP = tkinter.simpledialog.askstring(parent=self, title='Selezione Magazzino',
                                                   prompt='Inserisci il numero magazzino:')
        indice = self.tblProdotti.focus()
        idx = self.tblProdotti.item(indice)
        cod = str(idx['values'][0])
        nome = str(idx['values'][1])
        magazzinoD = puntoVendita.replace('PV', '')
        if magazzinoP == magazzinoD:
            tkinter.messagebox.showerror(parent=self, title='Errore selezione',
                                         message='Non puoi ordinare dal tuo magazzino!')
            magazzinoP = tkinter.simpledialog.askstring(parent=self, title='Selezione Magazzino',
                                                        prompt='Inserisci il numero magazzino:')
        nome = "*" + cod + "," + magazzinoP + " - " + nome
        InserisciOrdineWidget(nome=nome)

    def eliminaProdotto(self):
        indice = self.tblProdotti.focus()
        idx = self.tblProdotti.item(indice)
        cod = str(idx['values'][0])
        nome = str(idx['values'][1])
        elimina = tkinter.messagebox.askyesno(parent=self, title='Eliminare prodotto?',
                                              message="Sei sicuro di voler eliminare il prodotto?")
        elimina1 = tkinter.messagebox.askyesno(parent=self, title='Conferma eliminazione',
                                               message="L'eliminazione del prodotto è definitiva, procedere?")
        if elimina and elimina1:
            databaseOperations.GestioneMagazzino().eliminaProdotto(codice=cod)
            _Message = "Il prodotto " + nome + " è stato correttamente eliminato!"
            tkinter.messagebox.showinfo(parent=self, title="Prodotto eliminato",
                                        message=_Message)
            self.listaMagazzino()
        else:
            tkinter.messagebox.showinfo(parent=self, title='Operazione annullata',
                                        message="Nessuna modifica è stata apportata al database")

    def visualizzaProdotto(self):
        indice = self.tblProdotti.focus()
        idx = self.tblProdotti.item(indice)
        codiceProdotto = str(idx['values'][0])
        VisualizzaProdottoWidget(codiceProdotto=codiceProdotto)
        self.destroy()

    def callback(self, event):
        indice = self.tblProdotti.focus()
        idx = self.tblProdotti.item(indice)
        codiceProdotto = str(idx['values'][0])
        VisualizzaProdottoWidget(codiceProdotto=codiceProdotto)
        self.destroy()

    def ricercaProdotto(self):
        codice = self.entryRicCodProd.get()
        nome = self.entryRicNomeProdotto.get()
        ean = self.entryRicEANProd.get()

        if codice == '' and nome == '' and ean == '':
            tkinter.messagebox.showerror(parent=self, title='Campi non compilati',
                                         message='Compila almeno un campo per procedere alla ricerca!')
            self.listaMagazzino()

        elif codice == '' and ean == '':
            prodotti = databaseOperations.GestioneMagazzino().ricercaMagazzino(ricerca='nome', nome=nome)
            self.entryRicNomeProdotto.delete(0, END)
            if prodotti == 1:
                tkinter.messagebox.showerror(parent=self, title='Nessun prodotto',
                                             message="Non è stato trovato nessun prodotto!")
            else:
                self.tblProdotti.delete(*self.tblProdotti.get_children())
                for prodotto in prodotti:
                    codice = prodotto[0]
                    nome = prodotto[1]
                    ean = prodotto[2]
                    fornitore = str(prodotto[12]).replace("\n", "")
                    mag0 = prodotto[7]
                    mag1 = prodotto[8]
                    mag2 = prodotto[9]
                    mag3 = prodotto[10]
                    mag4 = prodotto[11]
                    prezzo = prodotto[6]
                    riga = (
                        codice, nome, ean, fornitore, mag0, mag1, mag2, mag3, mag4, prezzo
                    )
                    self.tblProdotti.insert("", END, values=riga)

        elif nome == '' and ean == '':
            prodotti = databaseOperations.GestioneMagazzino().ricercaMagazzino(ricerca='codice', codice=codice)
            self.entryRicCodProd.delete(0, END)
            if prodotti == 1:
                tkinter.messagebox.showerror(parent=self, title='Nessun prodotto',
                                             message="Non è stato trovato nessun prodotto!")
            else:
                self.tblProdotti.delete(*self.tblProdotti.get_children())
                for prodotto in prodotti:
                    codice = prodotto[0]
                    nome = prodotto[1]
                    ean = prodotto[2]
                    fornitore = str(prodotto[12]).replace("\n", "")
                    mag0 = prodotto[7]
                    mag1 = prodotto[8]
                    mag2 = prodotto[9]
                    mag3 = prodotto[10]
                    mag4 = prodotto[11]
                    prezzo = prodotto[6]
                    riga = (
                        codice, nome, ean, fornitore, mag0, mag1, mag2, mag3, mag4, prezzo
                    )
                    self.tblProdotti.insert("", END, values=riga)

        elif codice == '' and nome == '':
            prodotti = databaseOperations.GestioneMagazzino().ricercaMagazzino(ricerca='ean', ean=ean)
            self.entryRicEANProd.delete(0, END)
            if prodotti == 1:
                tkinter.messagebox.showerror(parent=self, title='Nessun prodotto',
                                             message="Non è stato trovato nessun prodotto!")
            else:
                self.tblProdotti.delete(*self.tblProdotti.get_children())
                for prodotto in prodotti:
                    codice = prodotto[0]
                    nome = prodotto[1]
                    ean = prodotto[2]
                    fornitore = str(prodotto[12]).replace("\n", "")
                    mag0 = prodotto[7]
                    mag1 = prodotto[8]
                    mag2 = prodotto[9]
                    mag3 = prodotto[10]
                    mag4 = prodotto[11]
                    prezzo = prodotto[6]
                    riga = (
                        codice, nome, ean, fornitore, mag0, mag1, mag2, mag3, mag4, prezzo
                    )
                    self.tblProdotti.insert("", END, values=riga)




    def listaMagazzino(self):
        self.tblProdotti.delete(*self.tblProdotti.get_children())
        magazzino = databaseOperations.GestioneMagazzino().listaMagazzino()

        for prodotto in magazzino:
            codice = prodotto[0]
            nome = prodotto[1]
            ean = prodotto[2]
            fornitore = str(prodotto[12]).replace("\n","")
            mag0 = prodotto[7]
            mag1 = prodotto[8]
            mag2 = prodotto[9]
            mag3 = prodotto[10]
            mag4 = prodotto[11]
            prezzo = prodotto[6]
            riga = (
                codice, nome, ean, fornitore, mag0, mag1, mag2, mag3, mag4, prezzo
            )
            self.tblProdotti.insert("", END, values=riga)


# FINESTRA VISUALIZZA PRODOTTO##########################################################################################
class VisualizzaProdottoWidget(tk.Toplevel):
    def __init__(self, master=None, codiceProdotto='', **kw):
        self.codiceProdotto = codiceProdotto
        super(VisualizzaProdottoWidget, self).__init__(master, **kw)

        aliquote = databaseOperations.Settings().aliquoteIva()

        self.frame38 = ttk.Frame(self)
        self.frame36 = ttk.Frame(self.frame38)
        self.label42 = ttk.Label(self.frame36)
        self.label42.configure(text='Codice prodotto:')
        self.label42.pack(anchor='e', padx='5', pady='5', side='top')
        self.label43 = ttk.Label(self.frame36)
        self.label43.configure(text='Nome prodotto:')
        self.label43.pack(anchor='e', padx='5', pady='5', side='top')
        self.label44 = ttk.Label(self.frame36)
        self.label44.configure(text='EAN:')
        self.label44.pack(anchor='e', padx='5', pady='5', side='top')
        self.label45 = ttk.Label(self.frame36)
        self.label45.configure(text='Quantità tot. magazzino:')
        self.label45.pack(anchor='e', padx='5', pady='5', side='top')
        self.label46 = ttk.Label(self.frame36)
        self.label46.configure(text='Regime IVA:')
        self.label46.pack(anchor='e', padx='5', pady='5', side='top')
        self.label47 = ttk.Label(self.frame36)
        self.label47.configure(text='Categoria merceologica:')
        self.label47.pack(anchor='e', padx='5', pady='5', side='top')
        self.label48 = ttk.Label(self.frame36)
        self.label48.configure(text='Costo:')
        self.label48.pack(anchor='e', padx='5', pady='5', side='top')
        self.label49 = ttk.Label(self.frame36)
        self.label49.configure(text='Prezzo di vendita:')
        self.label49.pack(anchor='e', padx='5', pady='5', side='top')
        self.frame36.configure(height='150', width='200')
        self.frame36.pack(anchor='w', expand='false', fill='both', padx='5', pady='5', side='left')
        self.frame37 = ttk.Frame(self.frame38)
        self.entryCodProd = ttk.Entry(self.frame37)
        self.entryCodProd.pack(fill='x', pady='4', side='top')
        self.entryNomeProd = ttk.Entry(self.frame37)
        self.entryNomeProd.configure(width='40')
        self.entryNomeProd.pack(fill='x', pady='4', side='top')
        self.entryEanProd = ttk.Entry(self.frame37)
        self.entryEanProd.pack(fill='x', pady='4', side='top')
        self.entryQuant = ttk.Entry(self.frame37)
        self.entryQuant.pack(fill='x', pady='4', side='top')
        self.comboIVA = ttk.Combobox(self.frame37)
        self.comboIVA.configure(values=aliquote)
        self.comboIVA.pack(fill='x', pady='4', side='top')
        self.comboCategoria = ttk.Combobox(self.frame37)
        self.comboCategoria.pack(fill='x', pady='4', side='top')
        self.entry15 = ttk.Entry(self.frame37)
        self.entry15.pack(fill='x', pady='4', side='top')
        self.entry16 = ttk.Entry(self.frame37)
        self.entry16.pack(fill='x', pady='4', side='top')
        self.frame37.configure(height='200', width='200')
        self.frame37.pack(anchor='e', expand='true', fill='both', padx='5', pady='5', side='left')
        self.frame38.configure(height='200', width='200')
        self.frame38.pack(expand='false', fill='both', side='top')
        self.labelframe9 = ttk.Labelframe(self)
        self.treeview5 = ttk.Treeview(self.labelframe9)
        self.treeview5_cols = ['column26', 'column27', 'column28', 'column29']
        self.treeview5_dcols = ['column26', 'column27', 'column28', 'column29']
        self.treeview5.configure(columns=self.treeview5_cols, show='headings')
        self.treeview5.column('column26', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview5.column('column27', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview5.column('column28', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview5.column('column29', anchor='w',stretch='true',width='20',minwidth='20')
        self.treeview5.heading('column26', anchor='w',text='Fornitore')
        self.treeview5.heading('column27', anchor='w',text='Numero documento')
        self.treeview5.heading('column28', anchor='w',text='Data di acquisto')
        self.treeview5.heading('column29', anchor='w',text='Costo di acquisto')
        self.treeview5.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.labelframe9.configure(height='200', text='Fornitori: ', width='200')
        self.labelframe9.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame40 = ttk.Frame(self)
        self.button8 = ttk.Button(self.frame40)
        self.button8.configure(text='Aggiorna prodotto')
        self.button8.pack(anchor='e', padx='5', pady='5', side='right')
        self.button9 = ttk.Button(self.frame40)
        self.button9.configure(text='Ordina prodotto', command=self.ordina)
        self.button9.pack(anchor='e', padx='5', pady='5', side='left')
        self.button10 = ttk.Button(self.frame40)
        self.button10.configure(text='Scarica prodotto', command=self.vendi)
        self.button10.pack(anchor='e', padx='5', pady='5', side='left')
        self.frame40.configure(height='200', width='200')
        self.frame40.pack(fill='x', side='top')
        self.configure(height='200', width='200')
        self.geometry('600x600')
        self.minsize(600, 600)
        title = 'Visualizza prodotto: ' + codiceProdotto
        self.title(title)
        self.focus_force()

        self.caricaInterfaccia()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        RicercaProdottiWidget(root)
        self.destroy()

    def vendi(self):
        codice = self.entryCodProd.get()
        magazzino = puntoVendita
        vendi = inserisciVenditaWidget(codeProdotto=codice, magazzino=magazzino)

    def ordina(self):
        cod = self.entryCodProd.get()
        nome = self.entryNomeProd.get()

        magazzinoP = tkinter.simpledialog.askstring(parent=self, title='Selezione Magazzino',
                                                    prompt='Inserisci il numero magazzino:')
        magazzinoD = puntoVendita.replace('PV', '')
        if magazzinoP == magazzinoD:
            tkinter.messagebox.showerror(parent=self, title='Errore selezione',
                                         message='Non puoi ordinare dal tuo magazzino!')
            magazzinoP = tkinter.simpledialog.askstring(parent=self, title='Selezione Magazzino',
                                                        prompt='Inserisci il numero magazzino:')
        nome = "*" + cod + "," + magazzinoP + " - " + nome
        InserisciOrdineWidget(nome=nome)

    def caricaInterfaccia(self):
        ricerca = databaseOperations.GestioneMagazzino()
        prodotti = ricerca.ricercaMagazzino(ricerca='codice', codice=self.codiceProdotto)
        prodotto = prodotti[0]
        codice = prodotto[0]
        nome = prodotto[1]
        ean = prodotto[2]
        iva = prodotto[3]
        categoria = prodotto[4]
        costo = prodotto[5]
        prezzo = prodotto[6]
        quantità = int(prodotto[7])+int(prodotto[8])+int(prodotto[9])+int(prodotto[10])+int(prodotto[11])
        documentoFornitore = str(prodotto[12])

        #Inserisce i dati nelle entry:
        self.entryCodProd.insert(0, codice)
        self.entryCodProd.configure(state="disabled")
        self.entryNomeProd.insert(0, nome)
        self.entryEanProd.insert(0, ean)
        self.entryQuant.insert(0, str(quantità))
        self.comboIVA.insert(0, iva)
        self.comboCategoria.insert(0, categoria)
        self.entry15.insert(0, costo)
        self.entry16.insert(0, prezzo)

        datiTabella = tuple(map(str, documentoFornitore.splitlines(False)))
        for riga in datiTabella:
            riga = riga[:-1]
            riga = tuple(map(str, riga.split(' - ')))
            self.treeview5.insert("", END, values=riga)

# FINESTRA INSERMENTO VENDITA###########################################################################################
class inserisciVenditaWidget(tk.Toplevel):
    def __init__(self, codeProdotto, magazzino, master=None, **kw):
        super(inserisciVenditaWidget, self).__init__(master, **kw)
        self.frame47 = ttk.Frame(self)
        self.frame47.configure(height=200, width=200)
        self.lblNomeProdotto = ttk.Label(self.frame47)
        self.lblNomeProdotto.configure(text='Codice prodotto:')
        self.lblNomeProdotto.pack(anchor="e", side="top")
        self.label60 = ttk.Label(self.frame47)
        self.label60.configure(text='Magazzino:')
        self.label60.pack(anchor="e", side="top")
        self.label61 = ttk.Label(self.frame47)
        self.label61.configure(text='Quantità:')
        self.label61.pack(anchor="e", side="top")
        self.frame47.pack(expand="false", padx=5, pady=5, side="left")
        self.frame46 = ttk.Frame(self)
        self.frame46.configure(height=200, width=200)
        self.entryCodeProdotto = ttk.Entry(self.frame46)
        self.entryCodeProdotto.pack(side="top")
        self.entryCodeProdotto.insert(0, codeProdotto)
        self.entryMagazzino = ttk.Entry(self.frame46)
        self.entryMagazzino.pack(side="top")
        self.entryMagazzino.insert(0, magazzino)
        self.entryQty = ttk.Entry(self.frame46)
        self._text_ = '1'
        self.entryQty.delete("0", "end")
        self.entryQty.insert("0", self._text_)
        self.entryQty.pack(side="top")
        self.frame46.pack(padx=5, pady=5, side="left")
        self.btnScarica = ttk.Button(self)
        self.btnScarica.configure(text='Scarica')
        self.btnScarica.pack(fill="both", padx=5, pady=5, side="left")
        self.btnScarica.configure(command=self.scaricaProdotto)
        self.img_sell = tk.PhotoImage(file="images/sell.png")
        self.configure(height=200, width=200)
        self.iconphoto(True, self.img_sell)
        self.title("Seleziona quantità")

    def scaricaProdotto(self):
        codicePrd = self.entryCodeProdotto.get()
        mag = self.entryMagazzino.get()
        mag=mag.replace("PV","")
        qty = self.entryQty.get()

        databaseOperations.GestioneMagazzino().vendiProdotto(codice=codicePrd, magazzino=mag, qntVenduta=qty)
        #TODO: Completare inserimento funzione vendita
        self.destroy()

# FINESTRA PRINCIPALE###################################################################################################
class StockItApp:
    def __init__(self, master=None):
        # build ui

        self.style = ttk.Style(root)
        self.style.configure('TButton', background='#ff0000')

        self.normal = ttk.Style(root)
        self.normal.configure('TButton', background='#eee')

        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM orders_to_ship")
        self.orders_to_ship = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM comunicazioni")
        self.comunicazioni = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC LIMIT 1) sub ORDER BY "
                                           "idx ASC")
        self.chatList = str(self.cursor.fetchone())

        self.cursor.close()
        self.mydb.close()

        self.masterFrame = ttk.Frame(master)
        self.style = ttk.Style(master)

        self.frmPulsantiSup = ttk.Frame(self.masterFrame)
        self.btnStampa = ttk.Button(self.frmPulsantiSup)
        self.img_printer = tk.PhotoImage(file='images/printer.png')
        self.btnStampa.configure(image=self.img_printer, text='Cassa')
        self.btnStampa.pack(expand='false', padx='5', pady='5', side='right')
        self.btnStampa.configure(command=self.finestraStampe)
        self.btnVendi = ttk.Button(self.frmPulsantiSup)
        self.img_sell = tk.PhotoImage(file='images/sell.png')
        self.btnVendi.configure(image=self.img_sell, text='Vendita')
        self.btnVendi.pack(expand=False, padx=5, pady=5, side='right')
        self.stampeTip = Hovertip(self.btnStampa, "Apri la finestra Stampe")
        self.img_warehouse = tk.PhotoImage(file='images/warehouse.png')
        self.btnMagazzino = ttk.Button(self.frmPulsantiSup)
        self.btnMagazzino.configure(image=self.img_warehouse, text='Magazzino')
        self.btnMagazzino.pack(expand=False, padx=5, side='left')
        self.btnMagazzino.configure(command=RicercaProdottiWidget)
        self.btnOrdini = ttk.Button(self.frmPulsantiSup)
        self.img_box1 = tk.PhotoImage(file='images/box1.png')
        self.btnOrdini.configure(image=self.img_box1, text='Ordini')
        self.btnOrdini.pack(expand='false', padx='5', side='left')
        self.btnOrdini.configure(command=self.finestraOrdini)
        self.ordiniTip = Hovertip(self.btnOrdini, "Apri la finestra Gestione Ordini")
        self.btnAssistenza = ttk.Button(self.frmPulsantiSup)
        self.img_callcenter = tk.PhotoImage(file='images/call-center.png')
        self.btnAssistenza.configure(image=self.img_callcenter, text='Cassa')
        self.btnAssistenza.pack(expand='false', padx='5', side='left')
        self.btnAssistenza.configure(command=self.finestraAssistenza)
        self.assistenzaTip = Hovertip(self.btnAssistenza, "Apri la finestra Gestione Pratiche Assistenza")
        if operatore != 'operatore':
            self.btnCassa = ttk.Button(self.frmPulsantiSup)
            self.img_money = tk.PhotoImage(file='images/money.png')
            self.btnCassa.configure(image=self.img_money, text='Cassa')
            self.btnCassa.pack(expand='false', padx='5', side='left')
            self.btnCassa.configure(command=self.finestraCassa)
            self.cassaTip = Hovertip(self.btnCassa, "Apri la finestra Gestione Cassa")
        self.btnChat = ttk.Button(self.frmPulsantiSup)
        self.img_chat = tk.PhotoImage(file='images/chat.png')
        self.img_chatNotif = tk.PhotoImage(file='images/chatPlus.png')
        self.btnChat.configure(image=self.img_chat, text='Cassa', style='')
        self.style.configure('Die.TButton', background='#f00')
        self.btnChat.pack(expand='false', padx='5', side='left')
        self.btnChat.configure(command=self.finestraChat)
        self.chatTip = Hovertip(self.btnChat, "Apri la finestra Chat")
        self.btnBuoni = ttk.Button(self.frmPulsantiSup)
        self.img_creditcard = tk.PhotoImage(file='images/credit-card.png')
        self.btnBuoni.configure(image=self.img_creditcard, text='Cassa')
        self.btnBuoni.pack(expand='false', padx='5', side='left')
        self.btnBuoni.configure(command=self.finestraFidelity)
        self.buoniTip = Hovertip(self.btnBuoni, "Apri la finestra Fidelity Card")
        '''if operatore == 'manager' or 'master':
            self.btnSettings = ttk.Button(self.frmPulsantiSup)
            self.img_settings = tk.PhotoImage(file='settings.png')
            self.btnSettings.configure(image=self.img_settings, text='Cassa')
            self.btnSettings.pack(expand='false', padx='5', side='left')
            self.btnSettings.configure(command=self.finestraFidelity)'''
        if operatore == 'master':
            self.btnUsers = ttk.Button(self.frmPulsantiSup)
            self.img_users = tk.PhotoImage(file='images/user.png')
            self.btnUsers.configure(image=self.img_users, text='Cassa')
            self.btnUsers.pack(expand='false', padx='5', side='left')
            self.btnUsers.configure(command=self.finestraUtenti)
            self.utentiTip = Hovertip(self.btnUsers, "Apri la finestra Gestione Utenti")
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
        self.tblComunicazioni.yview_moveto(1)

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

        self.tblOrdiniDaEvadere.bind("<Double-1>", lambda event: self.ordineEvaso())
        self.tblOrdiniDaEvadere.yview_moveto(1)
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
        self.btnInserisciOrdine.configure(command=self.widgetInserisciOrdine)
        self.btnOrdineEvaso = ttk.Button(self.frmPulsantiInf)
        self.btnOrdineEvaso.configure(text='Ordine evaso')
        self.btnOrdineEvaso.pack(expand='false', ipadx='10', ipady='6', side='left')
        self.btnOrdineEvaso.configure(command=self.ordineEvaso)
        self.btnAggiornaOrdini = ttk.Button(self.frmPulsantiInf)
        # self.btnAggiornaOrdini.configure(text='Invia & Ricevi')
        # self.btnAggiornaOrdini.pack(expand='false', ipadx='10', ipady='6', side='left')
        # self.btnAggiornaOrdini.configure(command=self.aggiornamentoOrdini)
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
    def widgetInserisciOrdine():
        inserisci = InserisciOrdineWidget(root)
        inserisci.grab_set()

    @staticmethod
    def finestraStampe():
        stampe = StampeWidget(root)
        #stampe.grab_set()

    def finestraOrdini(self):
        ordini = OrdiniWidget(self.masterFrame)
        #ordini.grab_set()

    @staticmethod
    def finestraAssistenza():
        AssistenzaWidget(root)

    @staticmethod
    def finestraUtenti():
        UtentiWidget(root)

    def finestraCassa(self):
        CassaWidget(root)

    def finestraChat(self):
        self.btnChat.configure(image=self.img_chat, text='Cassa', style='')
        self.chat()

    @staticmethod
    def chat():
        ChatWidget(root)

    def finestraFidelity(self):
        RicercaFidClienteWidget(root)

    def stampaOrdini(self):
        PDFOperations.StampaOrdine(switch=0)

    @staticmethod
    def finestraInserisciOrdine():
        OrdiniWidget(root)

    def ordineEvaso(self):
        curItems = self.tblOrdiniDaEvadere.selection()
        for idx in curItems:
            index = self.tblOrdiniDaEvadere.item(idx)
            valore = index['values'][0]
            databaseOperations.GestioneOrdini(1, valore, nomeCliente='', nomeProdotto='', note='', quantity='',
                                              puntoVendita='')

        self.aggiornamentoOrdini()

    def OnDoubleClickComunicazioni(self, event):
        try:
            item = self.tblComunicazioni.identify('item', event.x, event.y)
            indice = self.tblComunicazioni.focus()
            idx = self.tblComunicazioni.item(indice)
            valore = idx['values'][0]
            autore = idx['values'][1]
            messaggio = idx['values'][2]
            title = str(valore) + " - " + str(autore)
            # tkinter.messagebox.showinfo(title="Comunicazione n." + title, message=messaggio + "\nAutore: " + autore)
            LeggiComunicazioneWidget(root, text=messaggio)
        except IndexError:
            pass

    def inserisciComunicazione(self):
        NuovaComunicazioneWidget()

    def eliminaComunicazione(self):
        indice = self.tblComunicazioni.focus()
        idx = self.tblComunicazioni.item(indice)
        valore = idx['values'][0]
        autore = idx['values'][1]

        if autore == nomeUtente or operatore == 'manager' or 'master':
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
        self.cursor.close()
        self.mydb.close()

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
            # try:
            time.sleep(1)
            mydb = mysql.connector.connect(option_files='connector.cnf')
            cursor = mydb.cursor()
            file1changed = False
            file2changed = False
            file3changed = False
            cursor.execute("SELECT * FROM orders_to_ship")
            NEWorders_to_ship = cursor.fetchall()
            cursor.execute("SELECT * FROM comunicazioni")
            NEWcomunicazioni = cursor.fetchall()
            cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC LIMIT 1) sub ORDER BY idx ASC")
            NEWChat = str(cursor.fetchone())
            cursor.close()
            mydb.close()
            if NEWorders_to_ship != self.orders_to_ship:
                file1changed = True
                time.sleep(1)
            elif NEWcomunicazioni != self.comunicazioni:
                file2changed = True
                time.sleep(1)
            elif NEWChat != self.chatList:
                file3changed = True
                time.sleep(1)

            else:
                file1changed = False
                file2changed = False
                file3changed = False

            if file1changed or file2changed:
                self.orders_to_ship = NEWorders_to_ship
                self.comunicazioni = NEWcomunicazioni
                self.aggiornamentoOrdini()

                try:
                    notify(
                        BodyText='Una nuova comunicazione o un nuovo ordine è stato ricevuto!',
                        AppName='StockIt Manager',
                        TitleText='Aggiornamento ricevuto',
                        ImagePath='icon.ico'
                    )
                except AttributeError:
                    pass

            if file3changed:
                self.chatList = NEWChat

                mydb = mysql.connector.connect(option_files='connector.cnf')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC LIMIT 1) sub ORDER BY idx ASC")
                messaggio = cursor.fetchone()
                messaggio = messaggio[1:]
                cursor.close()
                mydb.close()
                text = str(messaggio[0] + ": " + str(messaggio[1]))
                if messaggio[0] != nomeUtente:
                    self.btnChat.configure(image=self.img_chatNotif, style='Die.TButton')
                    try:
                        notify(
                            BodyText=text,
                            AppName='StockIt Manager',
                            TitleText='Nuovo messaggio',
                            ImagePath='images/chat.png'
                        )
                    except AttributeError:
                        pass
                file3changed = False

            else:
                pass

    def aggiornamentoInterfacce(self):
        UtentiWidget.aggiornaUtenti(self)
        AssistenzaWidget.aggiornamentoOrdini(self)
        OrdiniWidget.aggiornamentoOrdini(self)

    def eliminaNotificaChat(self):
        self.btnChat.configure(style='')

    def autoAggiornamentoDaemon(self):
        newthread = threading.Thread(target=self.ricercaAggiornamenti)
        newthread.daemon = True
        newthread.start()
        print("Daemon STARTED\n")


# STRING DIALOG PERSONALIZZATA##########################################################################################
class StringDialog(tkinter.simpledialog._QueryString):
    def body(self, master):
        super().body(master)
        self.iconbitmap('icon.ico')
        self.resizable(False, False)
        #self.overrideredirect(True)

    def ask_string(title, prompt, **kargs):
        d = StringDialog(title, prompt, **kargs)
        return d.result

operatore = 0
winchat = 'c'
wincassa = 'c'

if __name__ == '__main__':

    root = tk.Tk()
    root.minsize(width=700, height=650)
    root.geometry('1024x650')
    root.state('zoomed')
    root.title('AB Informatica - StockIt Manager')
    root.iconbitmap('icon.ico')
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    splashTiny = Image.open("images/icon.png")
    splashResized = splashTiny.resize((height, height), Image.ANTIALIAS)
    splash = ImageTk.PhotoImage(splashResized)
    splashImage = tk.Label(root, image=splash)
    splashImage.configure(background='#124282')
    splashImage.pack(expand=True, fill='both')
    nomeUtente = "TestUser"
    puntoVendita = "TestStore"
    loop = 0
    accesso = False
    while not accesso:
        if loop < 3:
            try:
                password = StringDialog.ask_string('Password Utente', 'Inserisci password:\t\t\t\t\t\t\n\n\n', show='*')
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
                splashImage.destroy()
                accesso = True
            except IndexError:
                tkinter.messagebox.showerror(title='Accesso errato', message="Impossibile effettuare l'accesso.\n"
                                                                             "Password errata o database "
                                                                             "irraggiungibile")
            loop = loop + 1
        else:
            try:
                root.destroy()
            except _tkinter.TclError:
                sys.exit()

    header = "AB Informatica - StockIt Manager | Operatore: " + nomeUtente + " - Punto vendita: " + puntoVendita
    try:
        root.title(header)
        app = StockItApp(root)
        ordini = OrdiniWidget
        assistenza = AssistenzaWidget
        cassa = CassaWidget
        inserisciOrdine = InserisciOrdineWidget
        inserisciDocumento = InserisciDocumentoWidget
        ricercaProdotti = RicercaProdottiWidget
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=False)
        filemenu.add_command(label='Invia/Ricevi', command=app.aggiornamentoOrdini)
        filemenu.add_command(label='Stampa...', command=StampeWidget)
        filemenu.add_separator()
        filemenu.add_command(label='Esci', command=root.destroy)

        magazzinomenu = tk.Menu(menubar, tearoff=False)
        magazzinomenu.add_command(label='Inserisci nuovo documento', command=inserisciDocumento)
        magazzinomenu.add_command(label='Ricerca prodotti magazzino', command=ricercaProdotti)
        #TODO: Aggiungi voce menu per aggiunta singolo prodotto

        ordinimenu = tk.Menu(menubar, tearoff=False)
        ordinimenu.add_command(label='Inserisci ordine', command=inserisciOrdine)
        ordinimenu.add_command(label='Apri finestra ordini', command=ordini)

        assistenzamenu = tk.Menu(menubar, tearoff=False)
        assistenzamenu.add_command(label='Apri finestra assistenza', command=assistenza)

        cassamenu = tk.Menu(menubar, tearoff=False)
        cassamenu.add_command(label='Apri finestra cassa', command=cassa)

        infomenu = tk.Menu(menubar, tearoff=False)
        infomenu.add_command(label='Credits', command=CreditsWidget, underline=0)

        menubar.add(tk.CASCADE, menu=filemenu, label='File', underline=0)
        menubar.add(tk.CASCADE, menu=ordinimenu, label='Ordini', underline=0)
        menubar.add(tk.CASCADE, menu=assistenzamenu, label='Assistenza', underline=0)
        menubar.add(tk.CASCADE, menu=cassamenu, label='Cassa', underline=0)
        menubar.add(tk.CASCADE, menu=magazzinomenu, label='Magazzino', underline=0)
        menubar.add(tk.CASCADE, menu=infomenu, label='Info', underline=0)
        root.configure(menu=menubar)

        app.run()
    except _tkinter.TclError:
        pass
