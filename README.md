# aws-data-ingestion-visualization Project

![](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)




## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Schema](#schema)
- [Dashboard](#dashboard)
- [Author](#author)
- [Acknowledgements](#acknowledgements)


## Overview
This is an end to end data engineering project that ingest data from an external API, use AWS tools such as Lambda and Glue to transform and visualize findings by Grafana.
Lambda function is paired up with Eventbridge which automates function calls.
Using Kinesis Firehose, the data is delivered to s3 bucket. Glue Crawler identifies the table schemas and creates a table to view in Athena self sustainably.
Glue Jobs are performed with python scripts using work orchestration for seamless interaction.

![image] (https://github.com/alexkimrow/aws-data-ingestion-visualization/blob/main/images/data%20orechestration.png)

## Architecture
![architecture_diagram](https://github.com/alexkimrow/aws-data-ingestion-visualization/blob/main/images/Project%20Architecutre%20Diagram.png)


## Tech Stack
- `Lambda`: Executed serverless functions for data transformation, validation, and triggering subsequent data pipeline steps.
- `Kinesis`: Enabled real-time data streaming and ingestion from the weather API.
- `Athena`: Performed interactive SQL queries on data stored in S3 for on-demand analysis.
- `EventBridge`: Managed event-driven workflows by routing events to AWS services and Lambda functions.
- `S3`: Acted as the central data lake for storing raw and processed data.
- `Glue Crawler`: Automatically discovered data schema in S3 and updated the data catalog.
- `Grafana`: Provided real-time dashboards and visualizations by connecting to Athena for monitoring weather data.

## Schema
- `time`: Current Time of Houston
- `latitude`: Latitude of Houston, TX
- `longitude`: Longitude of Houston, TX
- `temp`: Temperature of that time
- `humidity`: Humidity of that time
- `rain`: The sum of rain that time
- `row_ts`: Timestamp of the data row

![image] (https://github.com/alexkimrow/aws-data-ingestion-visualization/blob/main/images/athena%20query.png)

## Dashboard
![image] (https://github.com/alexkimrow/aws-data-ingestion-visualization/blob/main/images/visualization%20grafana.png)


## Acknowledgements

    - [Build Your First Serverless Data Engineering Project Course](https://maven.com/david-freitag/first-serverless-de-project)
    - [Weather Data Open Meteo API](https://api.open-meteo.com//)
    - [Grafana Dashboards](https://grafana.com/)

