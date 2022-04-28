from datetime import date
import mysql.connector


class VerificaDatabase:
    def __init__(self):
        self.mydb = mysql.connector.connect(option_files='VerifyConnector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS StockitManager;')
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


class GestioneAssistenza:
    def __init__(self, switch, idx, nomeCliente, contattoCliente, prodotto, difettoProdotto, dataConsegna, note):
        if switch == 0:
            #PRODOTTO RITIRATO
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            sql = ("""INSERT
                        INTO
                        `assistenzaProdotti`(`nomeCliente`, `contattoCliente`, `prodotto`, `difettoProdotto`, 
                        `dataConsegna`, `note`, `statoPratica`)
                        VALUES(%s, %s, %s, %s, %s, %s, %s)""")
            val = (nomeCliente, contattoCliente, prodotto, difettoProdotto, dataConsegna, note, 'inserita')
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1:  #PRATICA IN LAVORAZIONE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "UPDATE assistenzaProdotti SET statoPratica = 'in lavorazione' WHERE " \
                       "idx = '%s';"

            self.cursor.execute(_SQLMove, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 2:  #PRATICA LAVORATA
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "UPDATE assistenzaProdotti SET statoPratica = 'lavorata' WHERE " \
                       "idx = '%s';"

            self.cursor.execute(_SQLMove, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 3:  #PRATICA RESTITUITA
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "UPDATE assistenzaProdotti SET statoPratica = %s WHERE " \
                       "idx = '%s';"
            oggi = str(date.today())
            oggi = "Restituita il " + oggi
            self.cursor.execute(_SQLMove, (oggi, idx))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 4:  #ELIMINA ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM assistenzaProdotti WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()


class GestioneOrdini:
    def __init__(self, switch, idx, nomeProdotto, quantity, note, nomeCliente, puntoVendita):
        if switch == 0:  #INSERIMENTO ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            sql = ("""INSERT
                        INTO
                        `orders_to_ship`(`nomeProdotto`, `quantity`, `note`, nomeCliente, `puntoVendita`)
                        VALUES(%s, %s, %s, %s, %s)""")
            val = (nomeProdotto, quantity, note, nomeCliente, puntoVendita)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1:  #ORDINE IN CONSEGNA
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

        elif switch == 2:  #ORDINE IN CONSEGNA
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

        elif switch == 3:  #ELIMINA ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM orders_to_ship WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()

class Comunicazioni:
    def __init__(self, switch, idx, autore, messaggio, data):
        if switch == 0:
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            sql = ("""INSERT
                                    INTO
                                    `comunicazioni`(`autore`, `messaggio`, `data`)
                                    VALUES(%s, %s, %s)""")
            val = (autore, messaggio, data)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1:  #ELIMINA COMUNICAZIONE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM comunicazioni WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()


class Utenti:
    def __init__(self, switch, idx, nomeUtente, password, ruolo, puntoVendita):
        if switch == 0:
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            sql = ("""INSERT
                                    INTO
                                    `users`(`nomeUtente`, `password`, `manager`, `puntoVendita`)
                                    VALUES(%s, %s, %s, %s)""")
            val = (nomeUtente, password, ruolo, puntoVendita)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1:  #ELIMINA COMUNICAZIONE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM users WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

class Chat:
    def __init__(self, autore, messaggio, destinatario):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()
        sql = ("""INSERT
                                            INTO
                                            `chat`(`autore`, `messaggio`, `destinatario`)
                                            VALUES(%s, %s, %s)""")
        val = (autore, messaggio, destinatario)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

class Cassa:
    def __init__(self, switch, incassoTotale, corrispettivo, fatturato, contanti, pos, finanziamenti,
                 bonifici, assegni, acconti, preincassato, data, puntoVendita):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
        self.cursor = self.mydb.cursor()

        if switch == 0:
            sql = ("""INSERT
                    INTO
                    `cassa`(`incassoTotale`, `corrispettivo`, `fatturato`, `contanti`,
                    `pos`, `finanziamenti`, `bonifici`, `assegni`, `acconti`, `preincassato`,
                    `data`, `puntoVendita`)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
            val = (incassoTotale, corrispettivo, fatturato, contanti, pos, finanziamenti, bonifici, assegni, acconti,
                   preincassato, data, puntoVendita)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 1:
            _SQLDel = "DELETE FROM cassa WHERE data = %s AND puntoVendita = %s;"
            self.cursor.execute(_SQLDel, (data, puntoVendita))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()


class Fidelity:
    def __init__(self, switch=0, numeroCarta = "", nomeUtente = "", indirizzoCliente = "", contattoCliente = "",
                 creditoCliente = 0):
        global utenti
        global utente
        utente = nomeUtente
        global carta
        carta = numeroCarta
        global indirizzo
        indirizzo = indirizzoCliente
        global contatto
        contatto = contattoCliente
        global credito
        credito = creditoCliente
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()

    def eliminaCliente(self):
        _SQLDel = "DELETE FROM fidelity WHERE numeroCarta = %s;"
        self.cursor.execute(_SQLDel, (carta,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def inserisciCliente(self):
        sql = ("""INSERT
                        INTO
                        `fidelity`(`numeroCarta`, `nomeCliente`, `indirizzoCliente`, `contattoCliente`,
                        `credito`)
                        VALUES(%s, %s, %s, %s, %s)""")
        val = (carta, utente, indirizzo, contatto, credito)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def ricercaCliente(self):
        if carta == '':
            _SQLDel = "SELECT * FROM fidelity WHERE nomeCliente = %s;"
            self.cursor.execute(_SQLDel, (utente,))
            utenti = self.cursor.fetchall()

        elif utente == '':
            _SQLDel = "SELECT * FROM fidelity WHERE numeroCarta = %s;"
            self.cursor.execute(_SQLDel, (carta,))
            utenti = self.cursor.fetchall()

        else:
            _SQLDel = "SELECT * FROM fidelity WHERE nomeCliente = %s or numeroCarta = %s;"
            self.cursor.execute(_SQLDel, (utente, carta))
            utenti = self.cursor.fetchall()

        return utenti


    def selezionaClienti(self):
        _SQLSel = "SELECT * FROM fidelity;"
        self.cursor.execute(_SQLSel)
        utenti = self.cursor.fetchall()
        return utenti

    def aggiornaCredito(self):
        _SQLMove = "UPDATE fidelity SET credito = %s WHERE numeroCarta = %s;"
        self.cursor.execute(_SQLMove, (credito, carta))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def verificaCredito(self):
        _SQLSel = "SELECT * FROM fidelity WHERE numeroCarta = %s;"
        self.cursor.execute(_SQLSel, (carta,))
        utenti = self.cursor.fetchall()
        print(utenti)
        for utente in utenti:
            nuovoCredito = utente[4]
        return nuovoCredito
