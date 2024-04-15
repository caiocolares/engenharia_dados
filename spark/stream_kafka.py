from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.functions import *



spark = SparkSession.builder \
   .appName("EngDados2") \
    .master("spark://spark-master:7077") \
   .config("spark.executorEnv.PYSPARK_PYTHON", "/opt/bitnami/python/bin/python3") \
   .getOrCreate()

#spark.sparkContext.setLogLevel("WARN")

KAFKA_TOPIC = "CRYPTO_CURRENCY"
KAFKA_SERVER = "kafka:29092"


# Subscribe to 1 topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_SERVER) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

df = df.selectExpr("CAST(value AS STRING)")

query = df.writeStream.format("json")\
    .option("path", "/app/data") \
    .option("checkpointLocation", "/app/data/checkpoint") \
    .outputMode("append").start()


print("Listening to kafka")
query.awaitTermination(timeout=80)

