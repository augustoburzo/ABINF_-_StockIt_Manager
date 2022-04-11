import tkinter.messagebox

import mysql.connector


class VerificaDatabase():
    def __init__(self):
        self.mydb = mysql.connector.connect(option_files='VerifyConnector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS stockit;')
        self.cursor.close()
        self.mydb.close()
        self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_to_ship('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_shipped('
                            'idx INT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_received('
                            'idx INT PRIMARY KEY,'
                            'nomeProdotto VARCHAR(40),'
                            'quantity INT,'
                            'note VARCHAR(80),'
                            'nomeCliente VARCHAR(40),'
                            'puntoVendita VARCHAR(40));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS assistenzaProdotti('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeCliente VARCHAR(40),'
                            'contattoCliente VARCHAR(40),'
                            'prodotto VARCHAR(60),'
                            'difettoProdotto VARCHAR(80),'
                            'dataConsegna VARCHAR(30),'
                            'note VARCHAR(120),'
                            'statoPratica VARCHAR(40));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users('
                            'idx INT AUTO_INCREMENT PRIMARY KEY,'
                            'nomeUtente VARCHAR(40),'
                            'password VARCHAR(40),'
                            'manager VARCHAR(60),'
                            'puntoVendita VARCHAR(40));')

        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
        #except:
        #    tkinter.messagebox.showerror(title='Impossibile collegare', message='Impossibile collegarsi al database\n'
        #                                                                        'Controllare le impostazioni')

class GestioneOrdini():
    def __init__(self, switch, idx, nomeProdotto, quantity, note, nomeCliente):
        if switch == 0: #INSERIMENTO ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            sql = ("""INSERT
                        INTO
                        `orders_to_ship`(`nomeProdotto`, `quantity`, `note`, `nomeCliente`)
                        VALUES(%s, %s, %s, %s)""")
            val = (nomeProdotto, quantity, note, nomeCliente)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1: #ORDINE IN CONSEGNA
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "INSERT INTO orders_shipped SELECT * FROM orders_to_ship WHERE idx = '%s';"
            _SQLDel = "DELETE FROM orders_to_ship WHERE idx = '%s';"
            print(idx)

            self.cursor.execute(_SQLMove, (idx,))
            self.cursor.execute(_SQLDel, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 2: #ORDINE IN CONSEGNA
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "INSERT INTO orders_received SELECT * FROM orders_shipped WHERE idx = '%s';"
            _SQLDel = "DELETE FROM orders_shipped WHERE idx = '%s';"
            print(idx)

            self.cursor.execute(_SQLMove, (idx,))
            self.cursor.execute(_SQLDel, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 3: #ELIMINA ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM orders_to_ship WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()
