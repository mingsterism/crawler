import pika 
import configparser 
import common
import json

RABBIT_CONTAINER='rabbitContainer2'
PROFILES='profiles.ini'


config = configparser.ConfigParser()
config.read(PROFILES)

def sendRabbitMessage(x):
        q = common.Connector(config[RABBIT_CONTAINER])
        message = json.dumps({'url':x})
        channel1 = common.create_channel(config[PROFILES])
        channel1.basic_publish(exchange='logs', routing_key='', body=message)
        return channel1    

def main(x):
    try:
        a1 = sendRabbitMessage(x)
    except KeyboardInterupt:
        a1.close()
    

