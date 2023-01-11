import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from fpdf import FPDF
import mysql.connector


class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', '', 10)
        # Title
        self.cell(95, 10, 'AB Informatica - StockIt Manager', 0, 0, 'L')
        #self.cell(95,10, head, 0, 0, 'R')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(95, 10, 'AB Informatica - Augusto Burzo | StockIt Manager')
        self.set_x(-105)
        self.cell(95, 10, 'Pagina ' + str(self.page_no()), 0, 0, 'R')


class StampaOrdine():
    def __init__(self, switch):
        filename = "Prodotti"
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        if switch == 0:
            cursor.execute("SELECT * FROM orders_to_ship")
        elif switch == 1:
            cursor.execute("SELECT * FROM orders_shipped")
        elif switch == 2:
            cursor.execute("SELECT * FROM orders_received")

        ordiniDaStampare = cursor.fetchall()
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('', 'B', 14)
        if switch == 0:
            pdf.cell(190, 10, 'PRODOTTI IN ORDINE', align='C', ln=2)
            filename = "Prodotti in ordine"
        elif switch == 1:
            pdf.cell(190, 10, 'PRODOTTI IN CONSEGNA', align='C', ln=2)
            filename = "Prodotti in consegna"
        elif switch == 2:
            pdf.cell(190, 10, 'PRODOTTI CONSEGNATI', align='C', ln=2)
            filename = "Prodotti consegnati"
        pdf.set_font('', '', 10)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(7, 6, "Nr.", 1, align='L')
        pdf.cell(80, 6, "Nome prodotto", 1, align='l')
        pdf.cell(10, 6, "Qnt.", 1, align='l')
        pdf.cell(33, 6, "Note", 1, align='l')
        pdf.cell(30, 6, "Nome cliente", 1, align='l')
        pdf.cell(30, 6, "Punto Vendita", 1, align='l')
        pdf.ln()
        for ordine in ordiniDaStampare:
            pdf.cell(7, 4, str(ordine[0]), 1, align='L')
            pdf.cell(80, 4, str(ordine[1][0:34]), 1, align='l')
            pdf.cell(10, 4, str(ordine[2]), 1, align='l')
            pdf.cell(33, 4, str(ordine[3]), 1, align='l')
            pdf.cell(30, 4, str(ordine[4][0:12]), 1, align='l')
            pdf.cell(30, 4, str(ordine[5]), 1, align='l')
            pdf.ln()

        try:
            files = [('PDF', '*.pdf')]
            outfile = tkinter.filedialog.asksaveasfilename(filetypes=files, defaultextension=files, title='Ordine',
                                                           initialfile=filename)
            pdf.output(outfile, 'F')
            tk.messagebox.showinfo(title="Ordine generato",
                               message="Ordine generato correttamente")
        except:
            tk.messagebox.showerror(title="Impossibile salvare", message='Impossibile salvare l\'ordine')

class StampaAssistenza():
    def __init__(self, switch):
        filename = "Prodotti"
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        if switch == 0:
            cursor.execute("SELECT * FROM assistenzaProdotti WHERE statoPratica = 'inserita'")
        elif switch == 1:
            cursor.execute("SELECT * FROM assistenzaProdotti WHERE statoPratica = 'in lavorazione'")
        elif switch == 2:
            cursor.execute("SELECT * FROM assistenzaProdotti WHERE statoPratica = 'lavorata'")

        ordiniDaStampare = cursor.fetchall()
        pdf = PDF()
        pdf.add_page(orientation='L')
        pdf.set_font('', 'B', 14)
        if switch == 0:
            pdf.cell(277, 10, 'NUOVE PRATICHE ASSISTENZA', align='C', ln=2)
            filename = "Nuove pratiche assistenza"
        elif switch == 1:
            pdf.cell(277, 10, 'PRATICHE ASSISTENZA IN LAVORAZIONE', align='C', ln=2)
            filename = "Assistenze in lavorazione"
        elif switch == 2:
            pdf.cell(277, 10, 'PRATICHE ASSISTENZA LAVORATE', align='C', ln=2)
            filename = "Assistenze lavorate"
        pdf.set_font('', '', 10)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(10, 6, "Nr.", 1, align='L')
        pdf.cell(77.5, 6, "Nome cliente", 1, align='l')
        pdf.cell(22.5, 6, "Contatto", 1, align='l')
        pdf.cell(44.5, 6, "Prodotto", 1, align='l')
        pdf.cell(44.5, 6, "Difetto", 1, align='l')
        pdf.cell(22.5, 6, "Data", 1, align='l')
        pdf.cell(55.5, 6, "Note", 1, align='l')
        pdf.ln()
        for ordine in ordiniDaStampare:
            pdf.cell(10, 4, str(ordine[0]), 1, align='L')
            pdf.cell(77.5, 4, str(ordine[1][0:33]), 1, align='l')
            pdf.cell(22.5, 4, str(ordine[2]), 1, align='l')
            pdf.cell(44.5, 4, str(ordine[3][0:25]), 1, align='l')
            pdf.cell(44.5, 4, str(ordine[4][0:25]), 1, align='l')
            pdf.cell(22.5, 4, str(ordine[5]), 1, align='l')
            pdf.cell(55.5, 4, str(ordine[6][0:28]), 1, align='l')
            pdf.ln()

        try:
            files = [('PDF', '*.pdf')]
            outfile = tkinter.filedialog.asksaveasfilename(filetypes=files, defaultextension=files, title='Ordine',
                                                           initialfile=filename)
            pdf.output(outfile, 'F')
            tk.messagebox.showinfo(title="Ordine generato",
                               message="Ordine generato correttamente")
        except:
            tk.messagebox.showerror(title="Impossibile salvare", message='Impossibile salvare l\'ordine')

class InserisciDataWidget(tk.Toplevel):
    def __init__(self, master=None, switch=0, operatore="", puntoVendita="", **kw):
        super(InserisciDataWidget, self).__init__(master, **kw)
        self.frame1 = ttk.Frame(self)
        self.label1 = ttk.Label(self.frame1)
        self.label1.configure(text='Giorno:')
        self.label1.pack(expand='true', pady='20', side='top')
        self.label2 = ttk.Label(self.frame1)
        self.label2.configure(text='Mese:')
        self.label2.pack(expand='true', pady='20', side='top')
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text='Anno:')
        self.label3.pack(expand='true', pady='20', side='top')
        self.frame1.configure(height='200', width='100')
        self.frame1.pack(fill='y', padx='5', pady='5', side='left')
        self.frame2 = ttk.Frame(self)
        self.combobox1 = ttk.Combobox(self.frame2)
        iconaStampe = tk.PhotoImage(file='images/printer.png')
        self.iconphoto(False, iconaStampe)

        self.operatore = operatore
        self.puntoVendita = puntoVendita

        if switch == 0:
            self.switch1 = 0
            self.combobox1.configure(state='disabled',
                                     values='01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31')
        elif switch == 1:
            self.switch1 = 1
            self.combobox1.configure(state='disabled',
                                     values='01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31')
        elif switch == 2:
            self.switch1 = 2
            self.combobox1.configure(state='enabled',
                                     values='01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31')
        self.combobox1.pack(expand='true', fill='x', pady='18', side='top')
        self.combobox2 = ttk.Combobox(self.frame2)
        if switch == 0:
            self.combobox2.configure(state='disabled', values='01 02 03 04 05 06 07 08 09 10 11 12')
        elif switch == 1:
            self.combobox2.configure(state='enabled', values='01 02 03 04 05 06 07 08 09 10 11 12')
        elif switch == 2:
            self.combobox2.configure(state='enabled', values='01 02 03 04 05 06 07 08 09 10 11 12')
        self.combobox2.pack(expand='true', fill='x', pady='18', side='top')
        self.entry1 = ttk.Entry(self.frame2)
        self.entry1.pack(expand='true', fill='x', pady='19', side='top')
        self.frame2.configure(height='200', width='160')
        self.frame2.pack(expand='true', fill='both', padx='5', pady='5', side='left')
        self.frame4 = ttk.Frame(self)
        self.button5 = ttk.Button(self.frame4)
        self.img_printer = tk.PhotoImage(file='images/printer.png')
        self.button5.configure(image=self.img_printer, text='Stampa', command=self.stampa)
        self.button5.pack(expand='true', fill='y', side='bottom')
        self.frame4.configure(height='200', width='60')
        self.frame4.pack(expand='true', fill='y', padx='5', pady='5', side='top')
        self.configure(height='200', width='200')
        self.geometry('320x200')
        self.resizable(False, False)
        self.title('Inserisci data')

    def stampa(self):
        if self.switch1 == 0:
            anno = self.entry1.get()
            query = anno + "-"

        elif self.switch1 == 1:
            anno = self.entry1.get()
            mese = self.combobox2.get()
            query = anno+"-"+mese+"-"

        elif self.switch1 == 2:
            anno = self.entry1.get()
            mese = self.combobox2.get()
            giorno = self.combobox1.get()
            query = anno+"-"+mese+"-"+giorno

        filename = "Prodotti"
        mydb = mysql.connector.connect(option_files='connector.cnf')
        cursor = mydb.cursor()
        if self.operatore == "master":
            _SQLSearch = "SELECT * FROM cassa WHERE data LIKE %s"
            args = [query + "%"]
            cursor.execute(_SQLSearch, args)
        else:
            _SQLSearch = "SELECT * FROM cassa WHERE data LIKE %s AND puntoVendita = %s"
            args = [query + "%", self.puntoVendita]
            cursor.execute(_SQLSearch, args)

        ordiniDaStampare = cursor.fetchall()
        pdf = PDF()
        pdf.add_page(orientation='L')
        pdf.set_font('', 'B', 14)
        if self.switch1 == 0:
            pdf.cell(277, 10, 'REPORT PER ANNO', align='C', ln=2)
            filename = "Report cassa per anno"
        elif self.switch1 == 1:
            pdf.cell(277, 10, 'REPORT PER MESE', align='C', ln=2)
            filename = "Report cassa per mese"
        elif self.switch1 == 2:
            pdf.cell(277, 10, 'REPORT PER GIORNO', align='C', ln=2)
            filename = "Report cassa per giorno"
        pdf.set_font('', '', 10)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(23, 6, "Incasso tot.", 1, align='L')
        pdf.cell(23, 6, "Corrispettivo", 1, align='l')
        pdf.cell(23, 6, "Fatturato", 1, align='l')
        pdf.cell(23, 6, "Contanti", 1, align='l')
        pdf.cell(23, 6, "POS", 1, align='l')
        pdf.cell(23, 6, "Finanziamen.", 1, align='l')
        pdf.cell(23, 6, "Bonifici", 1, align='l')
        pdf.cell(23, 6, "Assegni", 1, align='l')
        pdf.cell(23, 6, "Acconti", 1, align='l')
        pdf.cell(23, 6, "Preincassato", 1, align='l')
        pdf.cell(23, 6, "Data", 1, align='l')
        pdf.cell(23, 6, "P.Vendita", 1, align='l')
        pdf.ln()
        sommaIncassi = 0
        sommaCorrispettivi = 0
        sommaFatturati = 0
        sommaContanti = 0
        sommaPos = 0
        sommaFinanziamenti = 0
        sommaBonifici = 0
        sommaAssegni = 0
        sommaAcconti = 0
        sommaPreinc = 0
        for ordine in ordiniDaStampare:
            pdf.cell(23, 4, str(ordine[1]), 1, align='L')
            sommaIncassi = sommaIncassi + float(ordine[1])
            pdf.cell(23, 4, str(ordine[2]), 1, align='L')
            sommaCorrispettivi = sommaCorrispettivi + float(ordine[2])
            pdf.cell(23, 4, str(ordine[3]), 1, align='L')
            sommaFatturati = sommaFatturati + float(ordine[3])
            pdf.cell(23, 4, str(ordine[4]), 1, align='L')
            sommaContanti = sommaContanti + float(ordine[4])
            pdf.cell(23, 4, str(ordine[5]), 1, align='L')
            sommaPos = sommaPos + float(ordine[5])
            pdf.cell(23, 4, str(ordine[6]), 1, align='L')
            sommaFinanziamenti = sommaFinanziamenti + float(ordine[6])
            pdf.cell(23, 4, str(ordine[7]), 1, align='L')
            sommaBonifici = sommaBonifici + float(ordine[7])
            pdf.cell(23, 4, str(ordine[8]), 1, align='L')
            sommaAssegni = sommaAssegni + float(ordine[8])
            pdf.cell(23, 4, str(ordine[9]), 1, align='L')
            sommaAcconti = sommaAcconti + float(ordine[9])
            pdf.cell(23, 4, str(ordine[10]), 1, align='L')
            sommaPreinc = sommaPreinc + float(ordine[10])
            pdf.cell(23, 4, str(ordine[11]), 1, align='L')
            pdf.cell(23, 4, str(ordine[12]), 1, align='L')
            pdf.ln()
            
        pdf.set_fill_color(230, 230, 230)
        pdf.cell(23, 4, str(round(sommaIncassi, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaCorrispettivi, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaFatturati, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaContanti, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaPos, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaFinanziamenti, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaBonifici, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaAssegni, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaAcconti, 2)), 1, align='L', fill=True)
        pdf.cell(23, 4, str(round(sommaPreinc, 2)), 1, align='L', fill=True)
        pdf.ln()

        try:
            files = [('PDF', '*.pdf')]
            outfile = tkinter.filedialog.asksaveasfilename(filetypes=files, defaultextension=files, title='Ordine',
                                                           initialfile=filename)
            pdf.output(outfile, 'F')
            tk.messagebox.showinfo(title="Report generato",
                               message="Report generato correttamente")
        except:
            tk.messagebox.showerror(title="Impossibile salvare", message='Impossibile salvare il report')

        self.destroy()
