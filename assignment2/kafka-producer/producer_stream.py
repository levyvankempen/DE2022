import logging
import time
from threading import Thread
from kafka import KafkaProducer

vm_ip = '34.29.4.111'

def write_to_topic(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    print("Sending " + msg)
    producer.flush(timeout=60)

def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)

class KafkaMessageProducer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.producer = KafkaProducer(bootstrap_servers=f'{vm_ip}:9092')
        self.start()

    def run(self):
        while True:
            try:
                with open('D:/Documents/YEAR6_JADS_M1/1_Data_Engineering/Assignment2/Data/olist_orders_dataset.csv') as f0:
                    order_lines = f0.readlines()
                with open('D:/Documents/YEAR6_JADS_M1/1_Data_Engineering/Assignment2/Data/olist_order_items_dataset.csv') as f1:
                    order_items_lines = f1.readlines()


                for line0 in order_lines:
                    print(line0)
                    write_to_topic(self.producer, line0, 'orders')
                for line1 in order_items_lines:
                    print(line1)
                    write_to_topic(self.producer, line1, 'order_items')


                f0.close()            
                f1.close()
                time.sleep(60)
            except Exception as err:
                logging.info(f"Unexpected {err=}, {type(err)=}")
                time.sleep(60)


KafkaMessageProducer()