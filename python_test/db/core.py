import psycopg2

class core:
    def __init__(self):
        self.conn = psycopg2.connect(database="costumerBooking", user = "superuser", password = "YWxwZXJlbmV5bWVuMTIzLg==", host = "172.217.17.142", port = "5432")
        print("Connected to DB")
    def close(self):
        self.conn.close()
    def executeCommands(self, commands):
        cursr = self.conn.cursor()
        for command in commands:
           cursr.execute(command)
        self.conn.commit()
    def executeSelectCommand(self, command):
        cursr = self.conn.cursor()
        cursr.execute(command)
        rows = cursr.fetchall()
        return rows
    