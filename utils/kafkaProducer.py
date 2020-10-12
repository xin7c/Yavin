#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaProducer.py
@time:2020/10/12
"""
from kafka import KafkaProducer


def conn_kafka():
    producer = KafkaProducer(bootstrap_servers=['10.61.153.83:9092'])  # 连接kafka

    msg = "Hello World".encode('utf-8')  # 发送内容,必须是bytes类型
    producer.send('xc_topic', msg)  # 发送的topic为test
    # result = future.get(timeout=10)
    # print(result)
    producer.close()


if __name__ == '__main__':
    conn_kafka()
