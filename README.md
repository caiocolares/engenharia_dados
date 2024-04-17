
# Data Engineering - MBA Unifor 
Trabalho de Eng de Dados 2 - MBA Ciencias de Dados - Turma 5 - Unifor


![image](https://github.com/caiocolares/engenharia_dados/blob/7546aba3bd367075dbcf7c90e162d2d578008c72/assets/diagrama.png)

## Authors

- [@caiocolares](https://www.github.com/caiocolares) Matricula: 2316788
- [@danielripardo](https://github.com/dankiest) Matricula: 2316591
- [@rafaelreis](https://github.com/rafaelsreis) Matricula: 2316598


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

- User : airflow
- Password: airflow

Access [spark](http://localhost:8888)

#### Spark: 1 master and 2 workers
![image](https://github.com/caiocolares/engenharia_dados/blob/a1b797cad8aee922e09dd50f6d82d155781cb445/assets/spark.png)


Access [Kafdrop](http://localhost:19000) 

#### Kafka Messages
![image](https://github.com/caiocolares/engenharia_dados/blob/a1b797cad8aee922e09dd50f6d82d155781cb445/assets/kafdrop.png)

#### MongoDB (Using MongoDB Compass)
![image](https://github.com/caiocolares/engenharia_dados/blob/a1b797cad8aee922e09dd50f6d82d155781cb445/assets/mongodata.png)




## Tech Stack

- [Python](https://www.python.org/)
- [Airflow](https://airflow.apache.org/)
- [Pandas](https://pandas.pydata.org/)
- [Apache Spark](https://spark.apache.org/)
- [Apache Kafka](https://kafka.apache.org/)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Docker](https://www.docker.com/)
- [MongoDB](https://www.mongodb.com/)
- [Redis](https://redis.io/)
- [PostgreSQL](https://www.postgresql.org/)
