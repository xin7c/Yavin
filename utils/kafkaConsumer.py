#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaConsumer.py
@time:2020/10/12
"""

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer('test', bootstrap_servers=['10.61.153.83:9092'])

    print(consumer)
    for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
        print(recv)
