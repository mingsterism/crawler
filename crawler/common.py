import pika
import configparser
import psycopg2

# def create_channel(user, exchange, type):
# 	credentials = pika.PlainCredentials(user.credentials, user.credentials)
# 	parameters = pika.ConnectionParameters(user.ip, user.port, '/', credentials)
# 	connection = pika.BlockingConnection(parameters)
# 	channel = connection.channel()
# 	channel.exchange_declare(exchange=exchange, type=type)
# 	return channel

def create_channel(p):
	credentials = pika.PlainCredentials(p['credentials'], p['credentials'])
	parameters = pika.ConnectionParameters(p['ip'], int(p['port']), '/', credentials)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.exchange_declare(exchange=p['exchange'], type=p['type'])
	return channel

# class Connector:
	# def __init__(self, credentials, ip, port):
	# 	self.credentials = credentials
	# 	self.ip = ip
	# 	self.port = port

class Connector:
	def __init__(self, profile):
		self.credentials = profile['credentials']
		self.ip = profile['ip']
		self.port = profile['port']

class MYSQL_DB:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host=db_settings.HOST,
            user=db_settings.USER, password=db_settings.PASSWORD,
            database=db_settings.DATABASE)

    def insert_url(self, url):
        cursor = self.cnx.cursor()
        cursor.execute(
            'INSERT INTO crawled_urls (url) VALUES (%s)', (url,))
        self.cnx.commit()
        cursor.close()

class PSQL_DB:
    def __init__(self, db):
        self.conn = psycopg2.connect("dbname=" + db['dbname'] + " user=" + db['user'] + " host=" + db['host'] + " port=" + \
            db['port'])
        self.cur = self.conn.cursor()

    def create_table(self, table):
        self.cur.execute("CREATE TABLE IF NOT EXISTS " + table + " (id serial PRIMARY KEY, url TEXT);") 

    def insert_data(self, url, table):
        self.cur.execute("INSERT INTO " + table + " (url) VALUES ('" + url + "')")

    def closeDB(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()




