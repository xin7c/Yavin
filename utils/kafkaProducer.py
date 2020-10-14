#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaProducer.py
@time:2020/10/12
"""
import time
from json import dumps

from kafka import KafkaProducer

topic = "xx5"
def conn_kafka():
    producer = KafkaProducer(bootstrap_servers=['10.61.153.83:9092',
                                                '10.61.153.83:9093',
                                                '10.61.153.83:9094'])  # 连接kafka
    print(producer.bootstrap_connected())
    msg = f"{time.time()}".encode('utf-8')  # 发送内容,必须是bytes类型
    future = producer.send(topic=topic, value=msg, key=b"xuchu")  # 发送的topic为test
    result = future.get(timeout=60)
    print(result)
    print(future.is_done)

    producer.close()


if __name__ == '__main__':
    for i in range(1000):
        conn_kafka()
        time.sleep(2)

