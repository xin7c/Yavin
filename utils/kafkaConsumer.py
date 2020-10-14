#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaConsumer.py
@time:2020/10/12
"""
import time

from kafka import KafkaConsumer, TopicPartition
from json import loads

topic = 'xx5'


def consumerAction():
    consumer = KafkaConsumer(
        topic,  # topic
        group_id="xuchu",
        bootstrap_servers=['10.61.153.83:9092',
                           '10.61.153.83:9093',
                           '10.61.153.83:9094'],  # bootstrap server
        # api_version=(0, 11, 3),
        auto_offset_reset='earliest',
        # enable_auto_commit=True,
        # value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    consumer.partitions_for_topic(topic)
    print(consumer.topics())
    # print(consumer.position(TopicPartition(topic=u'xx5', partition=0)))
    consumer.subscribe(topics=['xx5'])
    print('Receiving message...')
    # 手动拉取消息
    # while True:
    #     msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
    #     print(msg)
    #     time.sleep(1)
    for message in consumer:
        recv = "%s:%d:%d: key=%s value=%s" % (
            message.topic, message.partition, message.offset, message.key, message.value)
        print(recv)
        print('Message: ' + str(message.value))


if __name__ == '__main__':
    consumerAction()
