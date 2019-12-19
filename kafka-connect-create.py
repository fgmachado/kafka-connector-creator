#!/usr/bin/python

import os
import sys
import requests

CONNECTION_URL = '$(connection.url)'
CONNECTION_USER = '$(connection.user)'
CONNECTION_PASSWORD = '$(connection.password)'


def connectors_create(params):
    path = get_item(params, 1)
    kafka_api = get_item(params, 2)
    kafka_host = get_item(params, 3)
    conn_url = get_item(params, 4)
    conn_user = get_item(params, 5)
    conn_pwd = get_item(params, 6)

    for file_name in read_dir(path):
        print(connector_create(read_file(path, file_name), kafka_api, kafka_host, conn_url, conn_user, conn_pwd))


def get_item(array=[], index=0):
    if array.__sizeof__() > 0:
        return array.__getitem__(index)
    return


def read_dir(path):
    return os.listdir(path)


def read_file(path, file_name):
    with open(path+'\\'+file_name) as reader:
        return reader.read()
    return ''


def prepare_file(content='', connection_url='', connection_user='', connection_password=''):
    content = replace_value(content, CONNECTION_URL, connection_url)
    content = replace_value(content, CONNECTION_USER, connection_user)
    return replace_value(content, CONNECTION_PASSWORD, connection_password)


def replace_value(content='', find='', new_value=''):
    return content.replace(find, new_value)


def connector_create(file_content, kafka_api, kafka_host, connection_url, connection_user, connection_password):
    file_content = prepare_file(file_content, connection_url, connection_user, connection_password)
    url = kafka_api + '/api/' + kafka_host + '/connectors'
    return do_post(url, file_content, {'Content-Type': 'application/json', 'Accept': 'application/json'})


def do_post(url, data, headers):
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()


args = sys.argv
connectors_create(args)
