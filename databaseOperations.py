from datetime import date

import mysql.connector

class GestioneAssistenza:
    def __init__(self, switch, idx, nomeCliente, contattoCliente, prodotto, difettoProdotto, dataConsegna, note):
        if switch == 0:
            # PRODOTTO RITIRATO
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

        elif switch == 1:  # PRATICA IN LAVORAZIONE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "UPDATE assistenzaProdotti SET statoPratica = 'in lavorazione' WHERE " \
                       "idx = '%s';"

            self.cursor.execute(_SQLMove, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 2:  # PRATICA LAVORATA
            self.mydb = mysql.connector.connect(option_files='connector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            _SQLMove = "UPDATE assistenzaProdotti SET statoPratica = 'lavorata' WHERE " \
                       "idx = '%s';"

            self.cursor.execute(_SQLMove, (idx,))

            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif switch == 3:  # PRATICA RESTITUITA
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

        elif switch == 4:  # ELIMINA ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM assistenzaProdotti WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()


class GestioneOrdini:
    def __init__(self, switch, idx, nomeProdotto, quantity, note, nomeCliente, puntoVendita):
        if switch == 0:  # INSERIMENTO ORDINE
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

        elif switch == 1:  # ORDINE IN CONSEGNA
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

        elif switch == 2:  # ORDINE IN CONSEGNA
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

        elif switch == 3:  # ELIMINA ORDINE
            self.mydb = mysql.connector.connect(option_files='connector.cnf')
            self.cursor = self.mydb.cursor()
            _SQLDel = "DELETE FROM orders_to_ship WHERE idx = '%s';"
            self.cursor.execute(_SQLDel, (idx,))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()


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

        elif switch == 1:  # ELIMINA COMUNICAZIONE
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

        elif switch == 1:  # ELIMINA COMUNICAZIONE
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
    def __init__(self, switch, incassoTotale=0, corrispettivo=0, fatturato=0, contanti=0, pos=0, finanziamenti=0,
                 bonifici=0, assegni=0, acconti=0, preincassato=0, data=0, puntoVendita=''):
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
            _SQLDel = "DELETE FROM cassa WHERE incassoTotale =%s AND data = %s AND puntoVendita = %s;"
            self.cursor.execute(_SQLDel, (incassoTotale, data, puntoVendita))
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()


class Fidelity:
    def __init__(self, numeroCarta="", nomeUtente="", indirizzoCliente="", contattoCliente="",
                 creditoCliente=0):
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
            self.cursor.close()
            self.mydb.close()

        elif utente == '':
            _SQLDel = "SELECT * FROM fidelity WHERE numeroCarta = %s;"
            self.cursor.execute(_SQLDel, (carta,))
            utenti = self.cursor.fetchall()
            self.cursor.close()
            self.mydb.close()

        else:
            _SQLDel = "SELECT * FROM fidelity WHERE nomeCliente = %s or numeroCarta = %s;"
            self.cursor.execute(_SQLDel, (utente, carta))
            utenti = self.cursor.fetchall()
            self.cursor.close()
            self.mydb.close()

        return utenti

    def selezionaClienti(self):
        _SQLSel = "SELECT * FROM fidelity;"
        self.cursor.execute(_SQLSel)
        utenti = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()
        return utenti

    def aggiornaCredito(self):
        _SQLMove = "UPDATE fidelity SET credito = %s WHERE numeroCarta = %s;"
        self.cursor.execute(_SQLMove, (credito, carta))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def aggiornaCliente(self):
        _SQLUpdate = "UPDATE fidelity SET nomeCliente = %s, indirizzoCliente = %s, contattoCliente = %s " \
                     "WHERE numeroCarta = %s"
        self.cursor.execute(_SQLUpdate, (utente, indirizzo, contatto, carta))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def verificaCredito(self):
        global nuovoCredito
        _SQLSel = "SELECT * FROM fidelity WHERE numeroCarta = %s;"
        self.cursor.execute(_SQLSel, (carta,))
        utenti = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()
        for utente in utenti:
            nuovoCredito = utente[4]
        return nuovoCredito


class GestioneMagazzino:
    def __init__(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()

    def inserisciDocumento(self, numero='', importo=0, data='', fornitore='', tipo='', prodotti=''):
        _SQLInsert = "INSERT INTO `documentiMagazzino`(`numero`,`importo`,`data`,`fornitore`,`tipo`," \
                     "`prodotti`) VALUES (%s,%s,%s,%s,%s,%s);"
        self.cursor.execute(_SQLInsert, (numero, importo, data, fornitore, tipo, prodotti))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def eliminaDocumento(self, numero=''):
        _SQLDelete = "DELETE FROM documentiMagazzino WHERE numero = %s;"
        self.cursor.execute(_SQLDelete, (numero,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def eliminaProdotto(self, codice=''):
        _SQLDelete = "DELETE FROM prodottiMagazzino WHERE codice = %s"
        self.cursor.execute(_SQLDelete, (codice,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def ricercaDocumenti(self, ricerca=0, numero='', fornitore='', data=''):

        if ricerca == 0:
            _SQLSearch = "SELECT * FROM documentiMagazzino WHERE numeroDoc = %s;"
            self.cursor.execute(_SQLSearch, (numero,))

        elif ricerca == 1:
            _SQLSearch = "SELECT * FROM documentiMagazzino WHERE fornitoreDoc = %s;"
            self.cursor.execute(_SQLSearch, (fornitore,))

        elif ricerca == 2:
            _SQLSearch = "SELECT * FROM documentiMagazzino WHERE data = %s;"
            self.cursor.execute(_SQLSearch, (data,))

        documenti = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()

        return documenti

    def listaDocumenti(self):
        #Ricava la lista completa dei documenti in magazzino
        _SQLList = "SELECT * FROM documentiMagazzino"
        self.cursor.execute(_SQLList)
        documenti = self.cursor.fetchall()

        return documenti

    def inserisciProdotto(self, codice='', nome='', ean='', iva='', quantita='', categoria='', costo='', prezzo='',
                          fornitore=''):
        #Inserisce il prodotto a magazzino
        _SQLInsert = "INSERT INTO `prodottiMagazzino`(`codice`,`nome`,`ean`,`iva`," \
                     "`categoria`,`costo`,`prezzo`,`fornitore`,`mag0`,`mag1`,`mag2`,`mag3`,`mag4`) VALUES (%s,%s,%s," \
                     "%s,%s,%s,%s,%s,%s,0,0,0,0);"
        self.cursor.execute(_SQLInsert, (codice, nome, ean, iva, categoria, costo, prezzo, fornitore,
                                         quantita))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def aggiornaProdotto(self, codice='', nome='', ean='', iva='', quantita='', categoria='', costo='', prezzo='',
                          fornitore=''):
        _SQLUpdate = "UPDATE prodottiMagazzino SET nome = %s, ean = %s, iva = %s, categoria = %s, costo = %s, " \
                     "prezzo = %s, mag0 = %s, fornitore = %s WHERE codice = %s"
        self.cursor.execute(_SQLUpdate, (nome, ean, iva, categoria, costo, prezzo, quantita, fornitore, codice))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def prodottoEsistente(self, ean, codice):
        #Verifica se il prodotto è esistente e restituisce un Booleano
        _SQLSearch = "SELECT * FROM prodottiMagazzino WHERE ean = %s OR codice = %s"
        self.cursor.execute(_SQLSearch, (ean, codice))
        prodotto = self.cursor.fetchone()
        self.cursor.close()
        self.mydb.close()

        if self.is_empty(prodotto):
            return False
        else:
            return True

    def leggiProdottoEsistente(self, ean='', codice=''):
        _SQLSearch = "SELECT * FROM prodottiMagazzino WHERE ean = %s OR codice = %s"
        self.cursor.execute(_SQLSearch, (ean, codice))
        prodotto = self.cursor.fetchone()
        self.cursor.close()
        self.mydb.close()

        return prodotto

    def listaMagazzino(self):
        _SQLList = "SELECT * FROM prodottiMagazzino"
        self.cursor.execute(_SQLList)
        prodotti = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()

        return prodotti

    def ricercaMagazzino(self, ricerca='ean', nome='', codice='', ean=''):
        global prodotti
        if ricerca == 'ean':
            _SQLSearch = "SELECT * FROM prodottiMagazzino WHERE ean = %s"
            self.cursor.execute(_SQLSearch, (ean,))
            prodotti = self.cursor.fetchall()

        elif ricerca == 'nome':
            _SQLSearch = "SELECT * FROM prodottiMagazzino WHERE nome LIKE %%s%"
            self.cursor.execute(_SQLSearch, (nome,))
            prodotti = self.cursor.fetchall()

        elif ricerca == 'codice':
            _SQLSearch = "SELECT * FROM prodottiMagazzino WHERE codice = %s"
            self.cursor.execute(_SQLSearch, (codice,))
            prodotti = self.cursor.fetchall()

        else:
            pass

        self.cursor.close()
        self.mydb.close()

        check = self.is_empty(prodotti)

        if check:
            return 1
        else:
            return prodotti

    def is_empty(self, any_structure):
        if any_structure:
            return False
        else:
            return True

class Settings:
    def __init__(self):
        self.mydb = mysql.connector.connect(option_files='connector.cnf')
        self.cursor = self.mydb.cursor()

    def aliquoteIva(self, percentonly=False):
        _SQLSearch = "SELECT * FROM aliquote"
        self.cursor.execute(_SQLSearch)
        aliquote = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()
        percent = ''
        nomi = ''
        for aliquota in aliquote:
            aliquota = aliquota[1]
            aliquota = str(aliquota)
            aliquota = aliquota.replace('[', '')
            aliquota = aliquota.replace(']', '')
            percent = percent + aliquota + ' '

        for stringa in aliquote:
            stringa = stringa[0]
            stringa = str(stringa)
            stringa = stringa.replace('[', '')
            stringa = stringa.replace(']', '')
            stringa = stringa.replace(' ', '_')
            nomi = nomi + stringa + ' '

        if percentonly:
            return percent

        if not percentonly:
            return nomi

    def inserisciAliquota(self, nomeAliquota='', percentuale=0):
        _SQLInsert = "INSERT INTO `aliquote` (`aliquota`, `percentuale`) VALUES ('%', '%');"
        self.cursor.execute(_SQLInsert, (nomeAliquota, percentuale))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def inserisciTipoDocumento(self, tipoDocumento=''):
        _SQLInsert = "INSERT INTO `tipodocumenti` (`tipo`) VALUES ('%');"
        self.cursor.execute(_SQLInsert, (tipoDocumento,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def eliminaTipoDocumento(self, idx=0):
        _SQLDelete = "DELETE FROM tipoDocumenti WHERE idx = %s;"
        self.cursor.execute(_SQLDelete, (idx,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def tipiDocumento(self):
        _SQLSearch = "SELECT * FROM tipoDocumenti"
        self.cursor.execute(_SQLSearch)
        tipi = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()
        lista = ''
        for tipo in tipi:
            tipo = tipo[1]
            tipo = str(tipo)
            tipo = tipo.replace("[", "")
            tipo = tipo.replace("]", "")
            tipo = tipo.replace("'", "")
            lista = lista + tipo + ' '
        return lista

    def eliminaAliquota(self, aliquota=''):
        _SQLDelete = "DELETE FROM aliquote WHERE aliquota = %s;"
        self.cursor.execute(_SQLDelete, (aliquota,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def eliminaCategoria(self, categoria=''):
        _SQLDelete = "DELETE FROM categorieProdotto WHERE categoria = %s;"
        self.cursor.execute(_SQLDelete, (categoria,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    def categorieProdotto(self):
        _SQLSearch = "SELECT * FROM categorieProdotto"
        self.cursor.execute(_SQLSearch)
        categorie = self.cursor.fetchall()
        self.cursor.close()
        self.mydb.close()
        lista = ''
        for categoria in categorie:
            categoria = categoria[1]
            categoria = str(categoria)
            categoria = categoria.replace("[", "")
            categoria = categoria.replace("]", "")
            categoria = categoria.replace("'", "")
            lista = lista + categoria + ' '
        return lista

    def inserisciCategoriaProdotto(self, categoriaProdotto=''):
        _SQLInsert = "INSERT INTO `tipodocumenti` (`tipo`) VALUES ('%');"
        self.cursor.execute(_SQLInsert, (categoriaProdotto,))
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
