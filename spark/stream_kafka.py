from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, IntegerType
from pyspark.sql.functions import *

import pymongo

scala_version = '2.12'
spark_version = '3.2.1'
packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    'org.apache.kafka:kafka-clients:3.2.0'
]

spark = SparkSession.builder \
   .appName("EngDados2") \
    .master("spark://spark-master:7077") \
   .config("spark.executorEnv.PYSPARK_PYTHON", "/opt/bitnami/python/bin/python3") \
   .config("spark.jars.packages", ",".join(packages))\
   .getOrCreate()

#spark.sparkContext.setLogLevel("WARN")

KAFKA_TOPIC = "CRYPTO_CURRENCY"
KAFKA_SERVER = "kafka:29092"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_SERVER) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()

schema = StructType([
    StructField("Open", DoubleType(), True),
    StructField("High", DoubleType(), True),
    StructField("Low", DoubleType(), True),
    StructField("Close", DoubleType(), True),
    StructField("Volume", DoubleType(), True),
    StructField("Dividends", DoubleType(), True),
    StructField("Stock Splits", DoubleType(), True),
    StructField("ticker", StringType(), True),
    StructField("data", StringType(), True) 
])

# Converter o valor da mensagem em uma string
#df = df.selectExpr("CAST(value AS STRING)")

# Converter a string JSON em um DataFrame
#df_json = df.selectExpr(f"from_json(value, '{schema}') AS data").select("data.*")

value_df = df.select(from_json(col("value").cast("string"), schema).alias("value"))
df_json = value_df.selectExpr("value.Open", "value.Close")


def log_df(df, epoch_id):
    value_df = df.select(from_json(col("value").cast("string"), schema).alias("value"))
    df_json = value_df.select("value.*")
    print(df_json.show())

#query = df \
#    .writeStream \
#    .foreachBatch(log_df) \
#    .start()

query = df_json.writeStream\
    .format("console")\
    .outputMode("append") \
    .start()


print("Listening to kafka")
query.awaitTermination(timeout=9999)

spark.stop()
