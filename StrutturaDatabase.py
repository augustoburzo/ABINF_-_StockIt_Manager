import mysql.connector


class StrutturaDatabase:
    def __init__(self):
        print("La seguente procedura distruggerà completamente il database!\n"
              "Si intende continuare? (S o N)")
        risposta = input()
        if risposta == 'S' or risposta == 's':
            self.mydb = mysql.connector.connect(option_files='VerifyConnector.cnf')  # CONNESSIONE DATABASE
            self.cursor = self.mydb.cursor()
            self.cursor.execute('DROP DATABASE IF EXISTS stockit;')
            self.cursor.execute('CREATE DATABASE IF NOT EXISTS stockit;')
            print('Database creato')
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
            print('Tabella ordini da inviare creata')

            self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_shipped('
                                'idx INT PRIMARY KEY,'
                                'nomeProdotto VARCHAR(40),'
                                'quantity INT,'
                                'note VARCHAR(80),'
                                'nomeCliente VARCHAR(40),'
                                'puntoVendita VARCHAR(40));')
            print('Tabella ordini inviati creata')

            self.cursor.execute('CREATE TABLE IF NOT EXISTS orders_received('
                                'idx INT PRIMARY KEY,'
                                'nomeProdotto VARCHAR(40),'
                                'quantity INT,'
                                'note VARCHAR(80),'
                                'nomeCliente VARCHAR(40),'
                                'puntoVendita VARCHAR(40));')
            print('Tabella ordini ricevuti creata')

            self.cursor.execute('CREATE TABLE IF NOT EXISTS assistenzaProdotti('
                                'idx INT AUTO_INCREMENT PRIMARY KEY,'
                                'nomeCliente VARCHAR(40),'
                                'contattoCliente VARCHAR(40),'
                                'prodotto VARCHAR(60),'
                                'difettoProdotto VARCHAR(80),'
                                'dataConsegna VARCHAR(30),'
                                'note VARCHAR(120),'
                                'statoPratica VARCHAR(40));')
            print('Tabella assistenza creata')

            self.cursor.execute('CREATE TABLE IF NOT EXISTS users('
                                'idx INT AUTO_INCREMENT PRIMARY KEY,'
                                'nomeUtente VARCHAR(40),'
                                'password VARCHAR(40),'
                                'manager VARCHAR(60),'
                                'puntoVendita VARCHAR(40));')
            print('Tabella utenti creata')

            self.cursor.execute('CREATE TABLE IF NOT EXISTS comunicazioni('
                                'idx INT AUTO_INCREMENT PRIMARY KEY,'
                                'autore VARCHAR(40),'
                                'messaggio VARCHAR(1000),'
                                'data VARCHAR(40));')
            print('Tabella comunicazioni creata')
            self.mydb.commit()

            self.cursor.execute('CREATE TABLE IF NOT EXISTS chat('
                                'idx INT AUTO_INCREMENT PRIMARY KEY,'
                                'autore VARCHAR(40),'
                                'messaggio VARCHAR(1000),'
                                'destinatario VARCHAR(40));')
            print('Tabella chat creata')
            self.mydb.commit()

            self.cursor.execute("""INSERT
                        INTO
                        `users`(`nomeUtente`, `password`, `manager`, `puntoVendita`)
                        VALUES ('MasterUser', 'mtsa6156', 'master', 'all')""")
            print('Master User creato')
            self.mydb.commit()

            self.cursor.execute("""INSERT
                                    INTO
                                    `users`(`nomeUtente`, `password`, `manager`, `puntoVendita`)
                                    VALUES ('Manager', 'manager', 'manager', 'all')""")
            print('Manager User creato')
            self.mydb.commit()
            self.cursor.close()
            self.mydb.close()

        elif risposta == 'N' or risposta == 'n':
            print("Nessuna modifica verrà apportata al database.\n"
                  "Premere invio per continuare.")
            input()
            exit()
        else:
            print('Risposta non valida.')
            self.__init__()


if __name__ == '__main__':
    app = StrutturaDatabase()
