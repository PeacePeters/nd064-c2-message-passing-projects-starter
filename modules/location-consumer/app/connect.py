import psycopg2
from kafka import KafkaConsumer
import os
import json

kafka_topic = "locations"
print('started listening ' + kafka_topic)

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_URL = os.environ["KAFKA_URL"]

kafka_consumer = KafkaConsumer(kafka_topic, bootstrap_servers=[KAFKA_URL])


def insert_location_to_db(location):
    db_connection = psycopg2.connect(
        dbname=DB_NAME,
        port=DB_PORT,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
    )
    cursor = db_connection.cursor()
    person_id = int(location["person_id"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])
    sql = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))".format(
        person_id, latitude, longitude
    )
    cursor.execute(sql)
    db_connection.commit()
    cursor.close()
    db_connection.close()

while True:
    for location in kafka_consumer:
        message = location.value.decode('utf-8')
        print('{}'.format(message))
        location_message = json.loads(message)
        insert_location_to_db(location_message)    