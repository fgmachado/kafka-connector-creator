# Apache Kafka Connector Creator
Apache Kafka Connector is a tool that possibility you to extract data from many sources and input it on Kafka Topics.

Has many ways to create connectors, but I chosen use Kafka Connect REST API, to make possible automate 
of this process using CI tools, like Jenkins or Azure DevOps Pipelines.

This project contains a Python script that you can use to automate the create process for your connectors.

The script read a directory that you need send as parameter, get all files inside it and make POST requests 
to Kafka Connector API to create to create the connectors. 

## Install and Run
To run this script you need to had installed Python in your host machine (Azure Agent, Jenkins Slave)

### Parameters
#### path
Directory where your json files with configuration about connectors is stored.

#### kafka_api
URL to your Kafka Connect API, example http[s]://your_host:port.

#### kafka_host
This parameter indicates the Kafka Connect Host where you whant to create the connector.
    
#### conn_url
JDBC url to configure your connection
    
#### conn_user
Connection user

#### conn_pwd
Connection password