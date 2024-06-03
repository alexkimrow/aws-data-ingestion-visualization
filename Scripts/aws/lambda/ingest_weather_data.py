import json
import boto3
import urllib3
import datetime

# REPLACE WITH YOUR DATA FIREHOSE NAME
FIREHOSE_NAME = "PUT-S3-axEqG"


def lambda_handler(event, context):

    http = urllib3.PoolManager()

    r = http.request(
        "GET",
        "https://api.open-meteo.com/v1/forecast?latitude=29.7633&longitude=-95.3633&current=temperature_2m,relative_humidity_2m,rain&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago&start_date=2024-05-01&end_date=2024-05-31",
    )

    # turn it into a dictionary
    r_dict = json.loads(r.data.decode(encoding="utf-8", errors="strict"))

    # extract pieces of the dictionary
    processed_dict = {}
    processed_dict["latitude"] = r_dict["latitude"]
    processed_dict["longitude"] = r_dict["longitude"]
    processed_dict["time"] = r_dict["current"]["time"]
    processed_dict["temp"] = r_dict["current"]["temperature_2m"]
    processed_dict["humidity"] = r_dict["current"]["relative_humidity_2m"]
    processed_dict["rain"] = r_dict["current"]["rain"]
    processed_dict["row_ts"] = str(datetime.datetime.now())

    # turn it into a string and add a newline
    msg = str(processed_dict) + "\n"

    fh = boto3.client("firehose")

    reply = fh.put_record(DeliveryStreamName=FIREHOSE_NAME, Record={"Data": msg})

    return reply
