import logging
import os

import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_API_v2.settings')
django.setup()
from testAPI_v2.models import ProductSet, Recipient

product_sets_url = 'https://stepik.org/media/attachments/course/73594/beautyboxes.json'
recipients_url = 'https://stepik.org/media/attachments/course/73594/recipients.json'

result = []
short_data = {}
short_data_list = []
try:
    response = requests.get(url=product_sets_url)
except requests.exceptions.Timeout as ex:
    logging.error(ex)

try:
    product_sets = response.json()

    for item in product_sets:
        short_data.update({'title': item['name']})
        short_data.update({'description': item['about']})
        short_data_list.append(short_data)
        short_data = {}
    product_sets = short_data_list
except Exception as ex:
    logging.error(ex)

try:
    responce = requests.get(url=recipients_url, timeout=5)
except requests.exceptions.Timeout as ex:
    logging.error(ex)

shortdata = {}
shortdatalist = []

try:
    recipients = responce.json()
    for item in recipients:
        shortdata.update(item['info'])
        shortdata.update({'phone_number': item['contacts']['phoneNumber']})
        shortdatalist.append(shortdata)
        shortdata = {}
    recipients = shortdatalist
except Exception as ex:
    logging.error(ex)

# Добавление данных в базу

""" Наборы """
for product_set in product_sets:
    new_product_set = ProductSet(title=product_set["title"], description=product_set["description"])
    # Раскоментить для добавления
    # new_product_set.save()

""" Получатели """
for recipient in recipients:
    new_recipient = Recipient(surname=recipient['surname'], name=recipient['name'], patronymic=recipient['patronymic'],
                              phone_number=recipient['phone_number'])
    # Раскоментить для добавления
    # new_recipient.save()
