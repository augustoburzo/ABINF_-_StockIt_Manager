import pathlib
from tkinter import END

import mysql.connector
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Database Config.ui"


class DatabaseConfigApp:
    def __init__(self, master=None):
        # build ui
        self.frame15 = ttk.Frame(master)
        self.frame1 = ttk.Frame(self.frame15)
        self.labelframe1 = ttk.Labelframe(self.frame1)
        self.frame2 = ttk.Frame(self.labelframe1)
        self.frame3 = ttk.Frame(self.frame2)
        self.label1 = ttk.Label(self.frame3)
        self.label1.configure(text='Indirizzo DB:')
        self.label1.pack(anchor='e', expand='true', fill='both', side='top')
        self.label2 = ttk.Label(self.frame3)
        self.label2.configure(justify='right', text='Username:')
        self.label2.pack(anchor='e', expand='true', fill='y', side='top')
        self.label3 = ttk.Label(self.frame3)
        self.label3.configure(text='Password:')
        self.label3.pack(anchor='e', expand='true', fill='y', side='top')
        self.label4 = ttk.Label(self.frame3)
        self.label4.configure(text='Database:')
        self.label4.pack(anchor='e', expand='true', fill='y', side='top')
        self.label5 = ttk.Label(self.frame3)
        self.label5.configure(text='Porta:')
        self.label5.pack(anchor='e', expand='true', fill='y', side='top')
        self.frame3.configure(height='200', width='200')
        self.frame3.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.frame4 = ttk.Frame(self.frame2)
        self.entryIndirizzo = ttk.Entry(self.frame4)
        self.entryIndirizzo.configure(takefocus=True, width='50')
        self.entryIndirizzo.delete('0', 'end')
        self.entryIndirizzo.pack(expand='true', fill='x', side='top')
        self.entryUsername = ttk.Entry(self.frame4)
        self.entryUsername.configure(width='50')
        self.entryUsername.delete('0', 'end')
        self.entryUsername.pack(expand='true', fill='x', side='top')
        self.entryPassword = ttk.Entry(self.frame4)
        self.entryPassword.configure(show='•', width='50')
        self.entryPassword.delete('0', 'end')
        self.entryPassword.pack(expand='true', fill='x', side='top')
        self.entryDatabase = ttk.Entry(self.frame4)
        self.entryDatabase.configure(width='50')
        self.entryDatabase.delete('0', 'end')
        self.entryDatabase.pack(expand='true', fill='x', side='top')
        self.entryPorta = ttk.Entry(self.frame4)
        self.entryPorta.configure(width='50')
        self.entryPorta.delete('0', 'end')
        self.entryPorta.pack(expand='true', fill='x', side='top')
        self.frame4.configure(height='200', width='200')
        self.frame4.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.labelframe1.configure(height='200', text='Definizioni Database', width='200')
        self.labelframe1.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame6 = ttk.Frame(self.frame1)
        self.btnAggiornaImp = ttk.Button(self.frame6)
        self.btnAggiornaImp.configure(text='Aggiorna impostazioni DB')
        self.btnAggiornaImp.pack(fill='x', padx='5', pady='5', side='top')
        self.btnAggiornaImp.configure(command=self.aggiornaImpostazioni)
        self.frame6.configure(height='200', width='200')
        self.frame6.pack(expand='true', fill='x', side='top')
        self.separator2 = ttk.Separator(self.frame1)
        self.separator2.configure(orient='horizontal')
        self.separator2.pack(expand='true', fill='x', ipadx='120', padx='5', pady='5', side='top')
        self.checkAzzeraDB = ttk.Checkbutton(self.frame1)
        self.checkAzzeraDB.configure(state='normal', text='Azzera Database')
        self.checkAzzeraDB.pack(side='top')
        self.separator3 = ttk.Separator(self.frame1)
        self.separator3.configure(orient='horizontal')
        self.separator3.pack(expand='true', fill='x', ipadx='120', padx='5', pady='5', side='top')
        self.labelframe2 = ttk.Labelframe(self.frame1)
        self.frame12 = ttk.Frame(self.labelframe2)
        self.checkTabNuoviOrdini = ttk.Checkbutton(self.frame12)
        self.checkTabNuoviOrdini.configure(text='Tabella Nuovi Ordini')
        self.checkTabNuoviOrdini.pack(anchor='w', side='top')
        self.checkTabOrdiniEvasi = ttk.Checkbutton(self.frame12)
        self.checkTabOrdiniEvasi.configure(text='Tabella Ordini Evasi')
        self.checkTabOrdiniEvasi.pack(anchor='w', side='top')
        self.checkTabOrdiniCons = ttk.Checkbutton(self.frame12)
        self.checkTabOrdiniCons.configure(text='Tabella Ordini Cons.')
        self.checkTabOrdiniCons.pack(anchor='w', side='top')
        self.checkTabCategorieProd = ttk.Checkbutton(self.frame12)
        self.checkTabCategorieProd.configure(text='Tabella Categorie Prod.')
        self.checkTabCategorieProd.pack(anchor='w', side='top')
        self.checkTabTipiDoc = ttk.Checkbutton(self.frame12)
        self.checkTabTipiDoc.configure(text='Tabella Tipi Documento')
        self.checkTabTipiDoc.pack(anchor='w', side='top')
        self.checkTabAliquote = ttk.Checkbutton(self.frame12)
        self.checkTabAliquote.configure(text='Tabella Aliquote IVA')
        self.checkTabAliquote.pack(anchor='w', side='top')
        self.checkTabProdotti = ttk.Checkbutton(self.frame12)
        self.checkTabProdotti.configure(text='Tabella Prodotti Mag.')
        self.checkTabProdotti.pack(anchor='w', side='top')
        self.frame12.configure(height='200', width='200')
        self.frame12.pack(expand='true', side='left')
        self.frame13 = ttk.Frame(self.labelframe2)
        self.checkTabDocumenti = ttk.Checkbutton(self.frame13)
        self.checkTabDocumenti.configure(text='Tabella Documenti Mag.')
        self.checkTabDocumenti.pack(anchor='w', side='top')
        self.checkTabAssistenza = ttk.Checkbutton(self.frame13)
        self.checkTabAssistenza.configure(text='Tabella Assistenza Prod.')
        self.checkTabAssistenza.pack(anchor='w', side='top')
        self.checkTabUtenti = ttk.Checkbutton(self.frame13)
        self.checkTabUtenti.configure(text='Tabella Utenti')
        self.checkTabUtenti.pack(anchor='w', side='top')
        self.checkTabComunicazioni = ttk.Checkbutton(self.frame13)
        self.checkTabComunicazioni.configure(text='Tabella Comunicazioni')
        self.checkTabComunicazioni.pack(anchor='w', side='top')
        self.checkTabChat = ttk.Checkbutton(self.frame13)
        self.checkTabChat.configure(text='Tabella Chat')
        self.checkTabChat.pack(anchor='w', side='top')
        self.checkTabCassa = ttk.Checkbutton(self.frame13)
        self.checkTabCassa.configure(text='Tabella Cassa')
        self.checkTabCassa.pack(anchor='w', side='top')
        self.checkTabFidelity = ttk.Checkbutton(self.frame13)
        self.checkTabFidelity.configure(text='Tabella Fidelity Card')
        self.checkTabFidelity.pack(anchor='w', side='top')
        self.frame13.configure(height='200', width='200')
        self.frame13.pack(expand='true', side='left')
        self.labelframe2.configure(height='200', text='Azzera tabelle', width='200')
        self.labelframe2.pack(fill='both', padx='5', pady='5', side='top')
        self.frame14 = ttk.Frame(self.frame1)
        self.button2 = ttk.Button(self.frame14)
        self.button2.configure(text='Consolida Database')
        self.button2.pack(side='top')
        self.button2.configure(command=self.consolidaDB)
        self.frame14.configure(height='200', width='200')
        self.frame14.pack(fill='x', pady='5', side='top')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(side='left')
        self.frame17 = ttk.Frame(self.frame15)
        self.textLogger = tk.Text(self.frame17)
        self.textLogger.configure(height='10', width='50')
        self.textLogger.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame17.configure(height='200', width='200')
        self.frame17.pack(expand='true', fill='both', side='top')
        self.frame15.configure(height='200', width='200')
        self.frame15.pack(side='top')
        self.leggiConfig()

        # Main widget
        self.mainwindow = self.frame15

    def run(self):
        self.mainwindow.mainloop()

    def leggiConfig(self):
        with open('connector.cnf', 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for line in lines:
                if line.startswith('host='):
                    host = line.replace('host=', '')
                    self.entryIndirizzo.delete(0, END)
                    self.entryIndirizzo.insert(0, host)
                if line.startswith('user='):
                    user = line.replace('user=', '')
                    self.entryUsername.delete(0, END)
                    self.entryUsername.insert(0, user)
                if line.startswith('password='):
                    pwd = line.replace('password=', '')
                    self.entryPassword.delete(0, END)
                    self.entryPassword.insert(0, pwd)
                if line.startswith('database='):
                    db = line.replace('database=', '')
                    self.entryDatabase.delete(0, END)
                    self.entryDatabase.insert(0, db)
                if line.startswith('port='):
                    port = line.replace('port=', '')
                    self.entryPorta.delete(0, END)
                    self.entryPorta.insert(0, port)

        with open('connector.cnf', 'r') as f:
            lines = f.readlines()
            self.textLogger.insert(END, 'FILE CONNESSIONE===========================\n')
            for line in lines:
                self.textLogger.insert(END, line)

            self.textLogger.insert(END, '\n===========================================\n')

    def aggiornaImpostazioni(self):
        host = self.entryIndirizzo.get()
        user = self.entryUsername.get()
        pwd = self.entryPassword.get()
        db = self.entryDatabase.get()
        port = self.entryPorta.get()

        with open('connector.cnf', 'w', encoding='utf-8') as f:
            f.write('[client]\n')
            f.write('host='+host)
            f.write('user='+user)
            f.write('password='+pwd)
            f.write('database='+db)
            f.write('port='+port)
            f.write('socket=/tmp/mysql.sock\n\n')
            f.write('[mysqld]\n')
            f.write('port='+port)
            f.write('socket=/tmp/mysql.sock\n')
            f.write('key_buffer_size=16M\n')
            f.write('max_allowed_packet=128M\n\n')
            f.write('[mysqldump]\n')
            f.write('quick')

        with open('connector.cnf', 'r') as f:
            lines = f.readlines()
            self.textLogger.insert(END, 'FILE CONNESSIONE AGGIORNATO================\n')
            for line in lines:
                self.textLogger.insert(END, line)

            self.textLogger.insert(END, '\n===========================================\n')

        with open('VerifyConnector.cnf', 'w', encoding='utf-8') as f:
            f.write('[client]\n')
            f.write('host=' + host)
            f.write('user=' + user)
            f.write('password=' + pwd)
            f.write('port=' + port)
            f.write('socket=/tmp/mysql.sock\n\n')
            f.write('[mysqld]\n')
            f.write('port=' + port)
            f.write('socket=/tmp/mysql.sock\n')
            f.write('key_buffer_size=16M\n')
            f.write('max_allowed_packet=128M\n\n')
            f.write('[mysqldump]\n')
            f.write('quick')

    def consolidaDB(self):
        self.mydb = mysql.connector.connect(option_files='VerifyConnector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()
        azzeraDB = self.checkAzzeraDB.state()
        nuoviOrdini = self.checkTabNuoviOrdini.state()
        ordiniEvasi = self.checkTabOrdiniEvasi.state()
        ordiniConsegnati = self.checkTabOrdiniCons.state()
        categorie = self.checkTabCategorieProd.state()
        tipiDoc = self.checkTabTipiDoc.state()
        aliquote = self.checkTabAliquote.state()
        prodotti = self.checkTabProdotti.state()
        documenti = self.checkTabDocumenti.state()
        assistenza = self.checkTabAssistenza.state()
        utenti = self.checkTabUtenti.state()
        comunicazioni = self.checkTabComunicazioni.state()
        chat = self.checkTabChat.state()
        cassa = self.checkTabCassa.state()
        fidelity = self.checkTabFidelity.state()

        if azzeraDB[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione completa DataBase selezionata\n')
            self.textLogger.insert(END, "===========================================\n\n")
            self.cursor.execute('DROP DATABASE IF EXISTS stockit;')
            self.textLogger.insert(END, ">>>Database eliminato correttamente\n")
            self.textLogger.insert(END, "===========================================\n\n")

        self.cursor.execute('CREATE DATABASE IF NOT EXISTS stockit;')
        self.cursor.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()

        if nuoviOrdini[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Nuovi Ordini\n')
            self.cursor.execute('DROP TABLE IF EXISTS orders_to_ship')
            self.textLogger.insert(END, '>>>Tabella Nuovi Ordini eliminata correttamente\n')

        if ordiniEvasi[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Ordini Evasi\n')
            self.cursor.execute('DROP TABLE IF EXISTS orders_shipped')
            self.textLogger.insert(END, '>>>Tabella Ordini Evasi eliminata correttamente\n')

        if ordiniConsegnati[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Ordini Ricevuti\n')
            self.cursor.execute('DROP TABLE IF EXISTS orders_received')
            self.textLogger.insert(END, '>>>Tabella Ordini Ricevuti eliminata correttamente\n')

        if categorie[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Categorie Prodotto\n')
            self.cursor.execute('DROP TABLE IF EXISTS categorieProdotto')
            self.textLogger.insert(END, '>>>Tabella Categorie Prodotto eliminata correttamente\n')

        if tipiDoc[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Tipi Documento\n')
            self.cursor.execute('DROP TABLE IF EXISTS tipoDocumenti')
            self.textLogger.insert(END, '>>>Tabella Tipi Documento eliminata correttamente\n')

        if aliquote[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Aliquote IVA\n')
            self.cursor.execute('DROP TABLE IF EXISTS aliquote')
            self.textLogger.insert(END, '>>>Tabella Aliquote IVA eliminata correttamente\n')

        if prodotti[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Prodotti Magazzino\n')
            self.cursor.execute('DROP TABLE IF EXISTS prodottiMagazzino')
            self.textLogger.insert(END, '>>>Tabella Prodotti Magazzino eliminata correttamente\n')

        if documenti[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Documenti Magazzino\n')
            self.cursor.execute('DROP TABLE IF EXISTS documentiMagazzino')
            self.textLogger.insert(END, '>>>Tabella Documenti Magazzino eliminata correttamente\n')

        if assistenza[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Assistenza Prodotti\n')
            self.cursor.execute('DROP TABLE IF EXISTS assistenzaProdotti')
            self.textLogger.insert(END, '>>>Tabella Assistenza Prodotti eliminata correttamente\n')

        if utenti[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Utenti\n')
            self.cursor.execute('DROP TABLE IF EXISTS users')
            self.textLogger.insert(END, '>>>Tabella Utenti eliminata correttamente\n')

        if comunicazioni[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Comunicazioni\n')
            self.cursor.execute('DROP TABLE IF EXISTS comunicazioni')
            self.textLogger.insert(END, '>>>Tabella Comunicazioni eliminata correttamente\n')

        if chat[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Chat\n')
            self.cursor.execute('DROP TABLE IF EXISTS chat')
            self.textLogger.insert(END, '>>>Tabella Chat eliminata correttamente\n')

        if cassa[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Cassa\n')
            self.cursor.execute('DROP TABLE IF EXISTS cassa')
            self.textLogger.insert(END, '>>>Tabella Cassa eliminata correttamente\n')

        if fidelity[0] == 'selected':
            self.textLogger.insert(END, 'Eliminazione Tabella Fidelity Card\n')
            self.cursor.execute('DROP TABLE IF EXISTS fidelity')
            self.textLogger.insert(END, '>>>Tabella Fidelity eliminata correttamente\n')
            self.textLogger.insert(END, '===========================================\n\n')

        self.textLogger.yview_moveto(1)

        self.cursor.execute('CREATE TABLE IF NOT EXISTS categorieProdotto('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'categoria VARCHAR(40));')
        self.textLogger.insert(END, '>>>>Tabella Categorie Prodotto creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS tipoDocumenti('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'tipo VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Tipi Documento creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS aliquote('
                            'aliquota VARCHAR(40) PRIMARY KEY,'
                            'percentuale INT);')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Aliquote creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS prodottiMagazzino('
                            'codice VARCHAR(40) PRIMARY KEY,'
                            'nome VARCHAR(40),'
                            'ean VARCHAR(40),'
                            'iva VARCHAR(40),'
                            'categoria VARCHAR(80),'
                            'costo VARCHAR(40),'
                            'prezzo VARCHAR(40),'
                            'mag0 INT,'
                            'mag1 INT,'
                            'mag2 INT,'
                            'mag3 INT,'
                            'mag4 INT,'
                            'fornitore VARCHAR(1000));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Prodotti Magazzino creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS documentiMagazzino('
                            'numero VARCHAR(40) PRIMARY KEY,'
                            'importo VARCHAR(40),'
                            'data VARCHAR(40),'
                            'fornitore VARCHAR(40),'
                            'tipo VARCHAR(40),'
                            'prodotti VARCHAR(1000));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Documenti Magazzino creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_to_ship('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Nuovi Ordini creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_shipped('
                            'idx INT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Ordini Inviati creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_received('
                            'idx INT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Ordini Consegnati creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS assistenzaProdotti('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeCliente VARCHAR(40),'
                            'contattoCliente VARCHAR(40),'
                            'prodotto VARCHAR(60),'
                            'difettoProdotto VARCHAR(80),'
                            'dataConsegna VARCHAR(30),'
                            'note VARCHAR(120),'
                            'statoPratica VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Assistenza Prodotti creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS users('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeUtente VARCHAR(40),'
                            'password VARCHAR(40),'
                            'manager VARCHAR(60),'
                            'puntoVendita VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Utenti creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS comunicazioni('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'autore VARCHAR(40),'
                            'messaggio VARCHAR(10000),'
                            'data VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Comunicazioni creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS chat('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'autore VARCHAR(40),'
                            'messaggio VARCHAR(1000),'
                            'destinatario VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Chat creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS cassa('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'incassoTotale FLOAT(40),'
                            'corrispettivo FLOAT(40),'
                            'fatturato FLOAT(40),'
                            'contanti FLOAT(40),'
                            'pos FLOAT(40),'
                            'finanziamenti FLOAT(40),'
                            'bonifici FLOAT(40),'
                            'assegni FLOAT(40),'
                            'acconti FLOAT(40),'
                            'preincassato FLOAT(40),'
                            'data VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Cassa creata\n')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS fidelity('
                            'numeroCarta VARCHAR(40) PRIMARY KEY,'
                            'nomeCliente VARCHAR(40),'
                            'indirizzoCliente VARCHAR(40),'
                            'contattoCliente VARCHAR(40),'
                            'credito FLOAT(40));')
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>Tabella Fidelity Card creata\n')

        self.textLogger.insert(END, '===========================================\n\n')

        self.cursor.execute("""INSERT
                                INTO
                                `users`(`nomeUtente`, `password`, `manager`, `puntoVendita`)
                                VALUES ('MasterUser', 'mtsa6156', 'master', 'PV0')""")
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>>Master User registrato correttamente\n')

        self.cursor.execute("""INSERT
                                            INTO
                                            `users`(`nomeUtente`, `password`, `manager`, `puntoVendita`)
                                            VALUES ('Manager', 'manager', 'manager', 'PV0')""")
        self.mydb.commit()
        self.textLogger.insert(END,'>>>>>Manager User registrato correttamente\n')
        self.cursor.execute("""INSERT
                                                    INTO
                                                    `aliquote`(`aliquota`, `percentuale`)
                                                    VALUES ('22% Standard', '22');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT
                                                            INTO
                                                            `aliquote`(`aliquota`, `percentuale`)
                                                            VALUES ('10% Standard', '10');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT
                                                            INTO
                                                            `aliquote`(`aliquota`, `percentuale`)
                                                            VALUES ('Esente', '0');""")
        self.mydb.commit()
        self.textLogger.insert(END, '>>>>>Tabella Aliquote popolata correttamente\n')
        self.cursor.close()
        self.mydb.close()
        self.textLogger.insert(END, '===========================================\n\n')
        self.textLogger.insert(END, '====DATA BASE CONSOLIDATO CORRETTAMENTE====\n')
        self.textLogger.yview_moveto(1)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Consolidatore DataBase - StockIt')
    root.iconbitmap('icon.ico')
    app = DatabaseConfigApp(root)
    app.run()


