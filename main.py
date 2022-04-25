import _tkinter
import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, NO, YES, ANCHOR
import mysql.connector
import tkinter.simpledialog
import tkinter.messagebox
from datetime import date
import time
import ctypes
from PIL import ImageTk, Image

import PDFOperations
import databaseOperations

columnsOrdini = ('numOrdine', 'nomeProdotto', 'quantita', 'note', 'nomeCliente', 'puntoVendita')
columnsComunicazioni = ('numComunicazione', 'autore', 'messaggio', 'data')
columnsAssistenza = ('numAssistenza', 'nomeCliente', 'contattoCliente', 'prodotto', 'difettoProdotto', 'dataConsegna',
                     'note', 'statoPratica')


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

        iconaCassa = tk.PhotoImage(file='money.png')

        super(CassaWidget, self).__init__(master, **kw)
        self.lfReportGiornata = ttk.Labelframe(self)
        self.lfTotali = ttk.Labelframe(self.lfReportGiornata)
        self.frame1 = ttk.Frame(self.lfTotali)
        self.lblIncassoTotale = ttk.Label(self.frame1)
        self.lblIncassoTotale.configure(text='Incasso totale:')
        self.lblIncassoTotale.pack(anchor='e', pady='5', side='top')
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text='Corrispettivo:')
        self.label3.pack(anchor='e', pady='5', side='top')
        self.label4 = ttk.Label(self.frame1)
        self.label4.configure(text='Fatturato:')
        self.label4.pack(anchor='e', pady='5', side='top')
        self.frame1.configure(height='200', width='150')
        self.frame1.pack(padx='5', side='left')
        self.frame4 = ttk.Frame(self.lfTotali)
        self.entryIncassoTot = ttk.Entry(self.frame4, textvariable=self.incassoTotale)
        self.entryIncassoTot.pack(expand='true', fill='x', pady='4', side='top')
        self.entryCorrispettivo = ttk.Entry(self.frame4, textvariable=self.corrispettivo)
        self.entryCorrispettivo.pack(expand='true', fill='x', pady='4', side='top')
        self.entryFatturato = ttk.Entry(self.frame4, textvariable=self.fatturato)
        self.entryFatturato.pack(expand=True, fill='x', pady='4', side='top')
        self.frame4.configure(height='80', width='200')
        self.frame4.pack(expand=True, fill='x', padx='5', side='left')
        self.lfTotali.configure(height='200', text='Totali Giornata', width='200')
        self.lfTotali.pack(expand='false', fill='x', padx='5', pady='5', side='top')
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
        self.frame6.configure(height='200', width='100')
        self.frame6.pack(expand='true', fill='both', side='left')
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
        self.btnQuadratura = ttk.Button(self.frame8)
        self.btnQuadratura.configure(text='Quadratura')
        self.btnQuadratura.pack(fill='x', padx='5', pady='10', side='top')
        self.btnQuadratura.configure(command=self.quadratura)
        self.lblQuadratura = ttk.Label(self.frame8, text='0,00')
        self.lblQuadratura.pack(side='top')

        self.btnInviaIncasso = ttk.Button(self.frame8)
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.btnInviaIncasso.configure(image=self.img_plus, text='button7')
        self.btnInviaIncasso.pack(expand='false', fill='both', padx='5', pady='5', side='bottom')
        self.btnInviaIncasso.configure(command=self.inviaIncasso)
        self.label14 = ttk.Label(self.frame8)
        self.label14.configure(text='Invia incassi:')
        self.label14.pack(pady='5', side='bottom')
        self.frame8.configure(height='200', width='100')
        self.frame8.pack(expand='true', fill='both', side='left')
        self.lfDettaglio.configure(height='200', text='Dettaglio Giornata', width='200')
        self.lfDettaglio.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lfReportGiornata.configure(height='200', text='Report Giornata', width='200')
        self.lfReportGiornata.pack(expand='false', fill='both', padx='5', pady='5', side='left')
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

        self.tblStoricoGiornate.column('incassoTotale', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('corrispettivo', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('fatturato', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('contanti', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('pos', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('finanziamenti', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('bonifici', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('assegni', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('acconti', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('preincassati', anchor='w', stretch='true', width='80', minwidth='20')
        self.tblStoricoGiornate.column('data', anchor='w', stretch='true', width='100', minwidth='20')
        self.tblStoricoGiornate.column('cassaPuntoVendita', anchor='w', stretch='true', width='80', minwidth='20')

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

        _default_ = 0.00

        self.entry.insert(0, _default_)
        self.entryContanti.insert(0, _default_)
        self.entryPOS.insert(0, _default_)
        self.entryBonifici.insert(0, _default_)
        self.entryAssegni.insert(0, _default_)
        self.entryAcconti.insert(0, _default_)
        self.entryFinanziamenti.insert(0, _default_)
        self.entryFatturato.insert(0, _default_)
        self.entryCorrispettivo.insert(0, _default_)

        self.aggiornaCasse()

    def quadratura(self):
        self.entryIncassoTot.delete(0, END)
        # incassoTotale = float(self.incassoTotale.get())
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
        totale = contanti + pos + finanziamenti + bonifici + assegni - acconti + preincassato
        quadratura = totale - incassoTotale
        quadratura = round(quadratura, 2)
        # self.entryQuadratura.insert(0, str(quadratura))
        self.lblQuadratura.configure(text=quadratura)

        if quadratura != 0:
            tkinter.messagebox.showerror(parent=self.frame1, title="Squadratura negativa",
                                         message="È stata riscontrata una squadratura di €" + str(quadratura))

        print(incassoTotale)
        print(corrispettivo)
        print(fatturato)
        print(contanti)
        print(pos)
        print(finanziamenti)
        print(bonifici)
        print(quadratura)
        print(totale)

    def eliminaRecord(self):
        indice = self.tblStoricoGiornate.focus()
        selezione = self.tblStoricoGiornate.item(indice)
        oggi = str(date.today())

        try:
            data = selezione['values'][10]
            negozio = selezione['values'][11]
            if negozio == puntoVendita:
                databaseOperations.Cassa(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, data=data, puntoVendita=puntoVendita)

            else:
                ErrorePV = tkinter.messagebox.showerror(parent=self, title="Errore Punto Vendita",
                                                        message="Non puoi eliminare i record degli altri Punti Vendita")

        except IndexError:
            ErroreIDX = tkinter.messagebox.showerror(parent=self, title="Nessuna selezione",
                                                     message="Seleziona una voce dalla tabella!")

        self.aggiornaCasse()

    def inviaIncasso(self):
        if self.entryIncassoTot.get() != "":
            corrispettivo = float(self.corrispettivo.get())
            fatturato = float(self.fatturato.get())
            contanti = float(self.contanti.get())
            pos = float(self.pos.get())
            finanziamenti = float(self.finanziamenti.get())
            bonifici = float(self.bonifici.get())
            assegni = float(self.assegni.get())
            acconti = float(self.acconti.get())
            preincassato = float(self.preincassato.get())
            incassoTotale = float(self.incassoTotale.get())
            data = str(date.today())

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
        else:
            erroreQuadratura = tkinter.messagebox.showerror(parent=self.frame8, title='Verificare quadratura',
                                                            message="Assicurarsi di aver verificato la quadratura "
                                                                    "prima di inserire l'incasso")

    def aggiornaCasse(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()

        if operatore != 'master':
            _SQLFetch = "SELECT * FROM cassa WHERE puntoVendita = %s"
            self.cursor.execute(_SQLFetch, (puntoVendita,))

        else:
            self.cursor.execute("SELECT * FROM cassa")

        giornate = self.cursor.fetchall()

        self.tblStoricoGiornate.delete(*self.tblStoricoGiornate.get_children())

        for giornata in giornate:
            giornata = giornata[1:]
            self.tblStoricoGiornate.insert("", END, values=giornata)


# FINESTRA CHAT#########################################################################################################

class ChatWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM chat")
        self.chat = self.cursor.fetchall()

        self.recuperaUtenti()

        iconaChat = tk.PhotoImage(file='chat.png')

        super(ChatWidget, self).__init__(master, **kw)
        self.lfChat = ttk.Labelframe(self)
        self.lbChat = tk.Listbox(self.lfChat)
        self.lbChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.lbChat.bind('<Double-1>', self.rispondi, add='')
        self.lfChat.configure(height='200', text='Chat utenti', width='200')
        self.lfChat.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frmNuovoMessaggio = ttk.Frame(self)
        self.frmBoxTesto = ttk.Frame(self.frmNuovoMessaggio)
        self.frame5 = ttk.Frame(self.frmBoxTesto)
        self.comboDestinatario = ttk.Combobox(self.frame5)
        self.comboDestinatario.pack(fill='x', side='top')
        self.comboDestinatario.configure(values=self.utentiChat)
        self.frame5.configure(height='20', width='200')
        self.frame5.pack(fill='x', side='top')
        self.textMessaggio = tk.Text(self.frmBoxTesto)
        self.textMessaggio.configure(height='6', width='50')
        self.textMessaggio.pack(expand='true', fill='x', side='top')
        self.textMessaggio.bind('<Return>', self.inviaMessaggio, add='')
        self.frmBoxTesto.configure(height='100', width='200')
        self.frmBoxTesto.pack(expand='true', fill='x', pady='5', side='left')
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
        self.lbChat.insert(0, 'Caricamento chat...')
        self.configure(height='200', width='200')
        self.geometry('800x600')
        self.iconphoto(False, iconaChat)
        self.title('Chat postazioni | AB Informatica - StockIt Manager')

        self.aggiornamentoChat()
        self.autoAggiornamentoDaemon()

    def recuperaUtenti(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM users")
        self.users = self.cursor.fetchall()

        self.utentiChat = ""

        for user in self.users:
            utenteChat = str(user[1]) + " "
            self.utentiChat = self.utentiChat + utenteChat

        print(self.utentiChat)

    def rispondi(self, event=None):
        destinatario = self.lbChat.get(ANCHOR)
        left_text = destinatario.partition(" ")[0]
        self.comboDestinatario.delete(0, END)
        self.comboDestinatario.insert(0, left_text)
        print("fatto")

    def inviaMessaggio(self, event=None):
        autore = nomeUtente
        messaggio = self.textMessaggio.get(1.0, END)
        destinatario = self.comboDestinatario.get()

        if messaggio != "" or messaggio != "\n":
            databaseOperations.Chat(autore, messaggio, destinatario)
            self.textMessaggio.delete(1.0, END)
            self.comboDestinatario.delete(0, END)

    def aggiornamentoChat(self):
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM (SELECT * FROM chat ORDER BY idx DESC LIMIT 30) sub ORDER BY idx ASC")
        messaggi = cursor.fetchall()

        self.lbChat.delete(0, END)

        for messaggio in messaggi:
            messaggio = messaggio[1:]
            y = "  -  ".join([str(value) for value in messaggio])
            y.replace("{", "")
            y.replace("}", "")
            self.lbChat.insert(END, y)
            self.lbChat.update()
            self.lbChat.yview(END)
            self.textMessaggio.delete(1.0, END)

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

            if file1changed == True:
                self.chat = NEWChat

                self.aggiornamentoChat()

            else:
                pass
            # except:
            #   print("error")

    # def aggiornamentoInterfacce():
    #    UtentiWidget.aggiornaUtenti()
    #    AssistenzaWidget.aggiornamentoOrdini()
    #    OrdiniWidget.aggiornamentoOrdini()

    def autoAggiornamentoDaemon(self):
        newthread = threading.Thread(target=self.ricercaAggiornamenti)
        newthread.daemon = True
        newthread.start()
        print("Chat Daemon STARTED\n")


# FINESTRA UTENTI#######################################################################################################

class UtentiWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        iconaUser = tk.PhotoImage(file='user.png')

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

        iconaAssistenza = tk.PhotoImage(file='call-center.png')

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
        self.iconphoto(False, iconaAssistenza)
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
        iconaOrdini = tk.PhotoImage(file='box1.png')

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

        self.tblOrdiniDaEvadere.bind("d", lambda event: self.eliminaOrdine())
        self.tblOrdiniDaEvadere.bind("e", lambda event: self.evadiOrdine())
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
            databaseOperations.GestioneOrdini(0, 0, self.nomeProdotto, self.quantita, self.note, self.nomeCliente,
                                              puntoVendita)

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


# FINESTRA NUOVO ORDINE##################################################################################################
class InserisciOrdineWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(InserisciOrdineWidget, self).__init__(master, **kw)

        iconaOrdini = tk.PhotoImage(file='box1.png')

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
        self.entryNomeProdotto1.pack(expand='true', fill='x', side='top')
        self.entryQuantita1 = ttk.Entry(self.frame19)
        self.entryQuantita1.configure(width='60')
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
        self.img_plus = tk.PhotoImage(file='plus.png')
        self.button7.configure(image=self.img_plus, text='Inserisci')
        self.button7.pack(expand='true', fill='y', padx='5', pady='5', side='top')
        self.button7.configure(command=self.nuovoOrdine)
        self.labelframe5.configure(height='200', text='Nuovo Ordine', width='200')
        self.labelframe5.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.configure(height='200', width='200')
        self.geometry('640x200')
        self.resizable(False, False)
        self.iconphoto(False, iconaOrdini)
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

        else:
            ErroreOrdine = tkinter.messagebox.showerror(parent=self, title="Compilare i campi",
                                                        message="Assicurati di aver compilato almeno i campi richiesti")

            self.destroy()


# FINESTRA LEGGI COMUNICAZIONE###########################################################################################
class LeggiComunicazioneWidget(tk.Toplevel):
    def __init__(self, master=None, text="", **kw):
        super(LeggiComunicazioneWidget, self).__init__(master, **kw)
        self.labelframe6 = ttk.Labelframe(self)
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


# FINESTRA STAMPE########################################################################################################

class StampeWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        iconaStampe = tk.PhotoImage(file='printer.png')

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

#CREDITS################################################################################################################
class CreditsWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(CreditsWidget, self).__init__(master, **kw)
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
Vecteezy''')
        self.label22.pack(expand='true', fill='both', side='top')
        self.configure(height='200', width='200')
        self.geometry('640x480')
        self.iconbitmap('icon.ico')
        self.resizable(False, False)
        self.title('Credits')

# FINESTRA PRINCIPALE###################################################################################################

class StockItApp:
    def __init__(self, master=None):
        # build ui
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT * FROM orders_to_ship")
        self.orders_to_ship = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM comunicazioni")
        self.comunicazioni = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM chat")
        self.chatList = self.cursor.fetchall()

        self.masterFrame = ttk.Frame(master)
        self.style = ttk.Style(master)

        self.frmPulsantiSup = ttk.Frame(self.masterFrame)
        self.btnStampa = ttk.Button(self.frmPulsantiSup)
        self.img_printer = tk.PhotoImage(file='printer.png')
        self.btnStampa.configure(image=self.img_printer, text='Cassa')
        self.btnStampa.pack(expand='false', padx='5', pady='5', side='right')
        self.btnStampa.configure(command=self.finestraStampe)
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
        if operatore != 'operatore':
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
        '''self.btnBuoni = ttk.Button(self.frmPulsantiSup)
        self.img_creditcard = tk.PhotoImage(file='credit-card.png')
        self.btnBuoni.configure(image=self.img_creditcard, text='Cassa')
        self.btnBuoni.pack(expand='false', padx='5', side='left')
        self.btnBuoni.configure(command=self.finestraFidelity)'''
        '''if operatore == 'manager' or 'master':
            self.btnSettings = ttk.Button(self.frmPulsantiSup)
            self.img_settings = tk.PhotoImage(file='settings.png')
            self.btnSettings.configure(image=self.img_settings, text='Cassa')
            self.btnSettings.pack(expand='false', padx='5', side='left')
            self.btnSettings.configure(command=self.finestraFidelity)'''
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

        self.tblOrdiniDaEvadere.bind("<Double-1>", lambda event: self.ordineEvaso())
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

    def widgetInserisciOrdine(self):
        InserisciOrdineWidget(root)

    @staticmethod
    def finestraStampe():
        StampeWidget(root)

    @staticmethod
    def finestraOrdini():
        OrdiniWidget(root)

    @staticmethod
    def finestraAssistenza():
        AssistenzaWidget(root)

    @staticmethod
    def finestraUtenti():
        UtentiWidget(root)

    @staticmethod
    def finestraCassa():
        CassaWidget(root)

    def finestraChat(self):
        self.btnChat.configure(style='')
        self.chat()

    @staticmethod
    def chat():
        ChatWidget(root)

    def finestraFidelity(self):
        pass

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
            #tkinter.messagebox.showinfo(title="Comunicazione n." + title, message=messaggio + "\nAutore: " + autore)
            LeggiComunicazioneWidget(root, text=messaggio)
        except IndexError:
            pass
            # tkinter.messagebox.showwarning(title="Nessuna selezione", message="Selezionare una voce per visualizzarla")

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
            cursor.execute("SELECT * FROM chat")
            self.NEWChat = cursor.fetchall()
            cursor.close()
            mydb.close()
            if NEWorders_to_ship != self.orders_to_ship:
                file1changed = True
                time.sleep(1)
            elif NEWcomunicazioni != self.comunicazioni:
                file2changed = True
                time.sleep(1)
            elif self.NEWChat != self.chatList:
                file3changed = True
            else:
                file1changed = False
                file2changed = False
                file3changed = False

            if (file1changed or file2changed) == True:
                self.orders_to_ship = NEWorders_to_ship
                self.comunicazioni = NEWcomunicazioni
                self.aggiornamentoOrdini()

            if file3changed == True:
                pass



            else:
                pass
            # except:
            #   print("error")

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


operatore = 0


class StringDialog(tkinter.simpledialog._QueryString):
    def body(self, master):
        super().body(master)
        self.iconbitmap('icon.ico')

    def ask_string(title, prompt, **kargs):
        d = StringDialog(title, prompt, **kargs)
        return d.result


if __name__ == '__main__':

    databaseOperations.VerificaDatabase()

    root = tk.Tk()
    root.minsize(width=700, height=650)
    root.geometry('1024x650')
    root.state('zoomed')
    root.title('AB Informatica - StockIt Manager')
    root.iconbitmap('icon.ico')
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    splashTiny = Image.open("StockIt.png")
    splashResized = splashTiny.resize((width, height), Image.ANTIALIAS)
    splash = ImageTk.PhotoImage(splashResized)
    splashImage = tk.Label(root, image=splash)
    splashImage.pack(expand=True, fill='both')
    nomeUtente = "TestUser"
    puntoVendita = "TestStore"

    try:
        password = StringDialog.ask_string('Password Utente', 'Inserisci password:\t\t\t\t\n\n\n', show='*')
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
    except IndexError:
        tkinter.messagebox.showerror(title='Accesso errato', message="Impossibile effettuare l'accesso.\n"
                                                                     "Password errata o database irraggiungibile")
        root.destroy()

    header = "AB Informatica - StockIt Manager | Operatore: " + nomeUtente + " - Punto vendita: " + puntoVendita
    try:
        root.title(header)
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=False)
        filemenu.add_command(label='Stampa...', command=StampeWidget)
        filemenu.add_separator()
        filemenu.add_command(label='Esci', command=root.destroy)

        infomenu = tk.Menu(menubar, tearoff=False)
        infomenu.add_command(label='Credits', command=CreditsWidget, underline=0)

        menubar.add(tk.CASCADE, menu=filemenu, label='File', underline=0)
        menubar.add(tk.CASCADE, menu=infomenu, label='Info', underline=0)
        root.configure(menu=menubar)
        app = StockItApp(root)
        app.run()
    except _tkinter.TclError:
        pass
