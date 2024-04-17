
# Data Engineering - MBA Unifor 
Trabalho de Eng de Dados 2 - MBA Ciencias de Dados - Unifor


![image](https://github.com/caiocolares/engenharia_dados/blob/7546aba3bd367075dbcf7c90e162d2d578008c72/assets/diagrama.png)

## Authors

- [@caiocolares](https://www.github.com/caiocolares)



## Run Locally

Clone the project

```bash
  git clone https://github.com/caiocolares/engenharia_dados.git
```

Go to the project directory

```bash
  cd engenharia_dados
```



## Environment Variables

```
export AIRFLOW_UID=1000
export _AIRFLOW_WWW_USER_USERNAME=airflow
export _AIRFLOW_WWW_USER_PASSWORD=airflow
```
Or write in local file .env


## Start Project 

To create folder (not mandatory)
```
sh setup.sh
```

Setup project
```
docker-compose up airflow-init
```

Run project
```
docker-compose up 
```


Access [airflow panel](http://localhost:8080)
#### DAG
![image](https://github.com/caiocolares/engenharia_dados/blob/7546aba3bd367075dbcf7c90e162d2d578008c72/assets/airfow.png)

User : airflow
Password: airflow

Access [spark](http://localhost:8888)

#### Spark: 1 master and 2 workers
![image](https://github.com/caiocolares/engenharia_dados/assets/26276218/e50628a5-d4f7-4259-9754-1c5b2c5d9593)


Access [Kafdrop](http://localhost:19000) 

#### Kafka Messages
![image](https://github.com/caiocolares/engenharia_dados/assets/26276218/e50628a5-d4f7-4259-9754-1c5b2c5d9593)

#### MongoDB (Using MongoDB Compass)
![image](https://github.com/caiocolares/engenharia_dados/assets/26276218/e50628a5-d4f7-4259-9754-1c5b2c5d9593)




## Tech Stack


**Server:** Airflow, Pandas, Python, Apache Spark, Apache Kafka, Kafdrop, Docker, MongoDB, Redis, Postgres

## Acknowledgements

- [Airflow](https://airflow.apache.org/)
- [Pandas](https://pandas.pydata.org/)

