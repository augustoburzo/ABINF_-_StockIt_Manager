import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

import guiMagazzino
import guiOrdini

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "StockItManager.ui"


class StockitmanagerApp:
    def __init__(self, master=None):
        # build ui
        self.mainWindow = tk.Toplevel(master, container='false')
        self.label1 = ttk.Label(self.mainWindow)
        self.img_Splash = tk.PhotoImage(file='Splash.png')
        self.label1.configure(borderwidth='0', image=self.img_Splash)
        self.label1.grid(column='0', columnspan='8', row='0', rowspan='6')
        self.frmComandi = tk.Frame(self.mainWindow)
        self.btnMagazzino = tk.Button(self.frmComandi)
        self.btnMagazzino.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                    font='{Bahnschrift} 14 {bold}')
        self.btnMagazzino.configure(foreground='#01509e', highlightbackground='#01509e', padx='20', pady='20')
        self.btnMagazzino.configure(relief='flat', text='Magazzino')
        self.btnMagazzino.pack(ipadx='16', side='top')
        self.btnMagazzino.configure(command=self.GestioneMagazzino)
        self.btnOrdini = tk.Button(self.frmComandi)
        self.btnOrdini.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                 font='{Bahnschrift} 14 {bold}')
        self.btnOrdini.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnOrdini.configure(text='Ordini P.V.')
        self.btnOrdini.pack(ipadx='17', side='top')
        self.btnOrdini.configure(command=self.GestioneOrdini)
        self.btnAssistenza = tk.Button(self.frmComandi)
        self.btnAssistenza.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                     font='{Bahnschrift} 14 {bold}')
        self.btnAssistenza.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnAssistenza.configure(text='Assistenza')
        self.btnAssistenza.pack(ipadx='14', side='top')
        self.btnAssistenza.configure(command=self.GestioneAssistenza)
        self.btnCassa = tk.Button(self.frmComandi)
        self.btnCassa.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                font='{Bahnschrift} 14 {bold}')
        self.btnCassa.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnCassa.configure(text='Cassa')
        self.btnCassa.pack(ipadx='33', side='top')
        self.btnCassa.configure(command=self.GestioneAssistenza)
        self.btnBacheca = tk.Button(self.frmComandi)
        self.btnBacheca.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                  font='{Bahnschrift} 14 {bold}')
        self.btnBacheca.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnBacheca.configure(text='Bacheca\ncomunicazioni')
        self.btnBacheca.pack(side='top')
        self.btnBacheca.configure(command=self.BackecaComunicazioni)
        self.btnChat = tk.Button(self.frmComandi)
        self.btnChat.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                               font='{Bahnschrift} 14 {bold}')
        self.btnChat.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnChat.configure(text='Chat P.V.')
        self.btnChat.pack(ipadx='23', side='top')
        self.btnChat.configure(command=self.ChatStaff)
        self.btnStampe = tk.Button(self.frmComandi)
        self.btnStampe.configure(activebackground='#fff', activeforeground='#0a76fa', background='#fff',
                                 font='{Bahnschrift} 14 {bold}')
        self.btnStampe.configure(foreground='#01509e', padx='20', pady='20', relief='flat')
        self.btnStampe.configure(text='Stampe')
        self.btnStampe.pack(ipadx='29', side='top')
        self.btnStampe.configure(command=self.StampaReport)
        self.frmComandi.configure(background='#fff', height='600', width='200')
        self.frmComandi.grid(column='8', row='0', rowspan='6', sticky='e')
        self.topMenu = tk.Menu(self.mainWindow)
        self.fileMenu = tk.Menu(self.topMenu, tearoff='false')
        self.topMenu.add(tk.CASCADE, menu=self.fileMenu, label='File', underline='0')
        self.mi_btnExit = 0
        self.fileMenu.add('command', label='Exit')
        self.magazzinoMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.magazzinoMenu, label='Magazzino', underline='0')
        self.ordiniMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.ordiniMenu, label='Ordini', underline='0')
        self.assistenzaMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.assistenzaMenu, label='Assistenza', underline='0')
        self.cassaMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.cassaMenu, label='Cassa', underline='0')
        self.bachecaMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.bachecaMenu, label='Bacheca', underline='0')
        self.chatMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.chatMenu, label='Chat', underline='1')
        self.stampeMenu = tk.Menu(self.topMenu)
        self.topMenu.add(tk.CASCADE, menu=self.stampeMenu, label='Stampe', underline='4')
        self.mainWindow.configure(menu=self.topMenu)
        self.btnClose = tk.Button(self.mainWindow)
        self.btnClose.configure(activebackground='#97cbff', activeforeground='#f00', background='#97cbff',
                                font='{Bahnschrift} 12 {}')
        self.btnClose.configure(foreground='#ffffff', height='3', relief='flat', text='Chiudi sessione')
        self.btnClose.grid(column='0', row='5', sticky='sw')
        self.btnClose.configure(command=self.stop)
        self.mainWindow.configure(background='#fff', height='200', width='200')
        self.mainWindow.iconbitmap('barcode.ico')
        self.mainWindow.minsize(800, 600)
        self.mainWindow.resizable(False, False)
        self.mainWindow.title('AB Informatica - StockIt Manager')
        self.mainWindow.grid_anchor('center')

        # Main widget
        self.mainwindow = self.mainWindow

    def stop(self):
        root.destroy()

    def run(self):
        self.mainwindow.mainloop()

    def GestioneMagazzino(self):
        guiMagazzino.RicercaProdottoWidget()

    def GestioneOrdini(self):
        guiOrdini.OrdiniWidget()

    def GestioneAssistenza(self):
        pass

    def BackecaComunicazioni(self):
        pass

    def ChatStaff(self):
        pass

    def StampaReport(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = StockitmanagerApp(root)
    app.run()

