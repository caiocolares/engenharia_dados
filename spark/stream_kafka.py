from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, IntegerType
from pyspark.sql.functions import *



spark = SparkSession.builder \
   .appName("EngDados2") \
    .master("spark://spark-master:7077") \
   .config("spark.executorEnv.PYSPARK_PYTHON", "/opt/bitnami/python/bin/python3") \
   .getOrCreate()

#spark.sparkContext.setLogLevel("WARN")

KAFKA_TOPIC = "CRYPTO_CURRENCY"
KAFKA_SERVER = "kafka:29092"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_SERVER) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

schema = StructType([
    StructField("Open", DoubleType()),
    StructField("High", DoubleType()),
    StructField("Low", DoubleType()),
    StructField("Close", DoubleType()),
    StructField("ticker", StringType()),
    StructField("data", StringType())
])

value_df = df.select(from_json(col("value").cast("string"), schema).alias("value"))

query = value_df.writeStream\
    .format("json")\
    .option("path", "/home/data") \
    .option("checkpointLocation", "/home/data/checkpoint") \
    .outputMode("append") \
    .start()


print("Listening to kafka")
query.awaitTermination(timeout=80)

