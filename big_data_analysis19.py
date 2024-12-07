from pyspark.sql import SparkSession

def create_spark_session(app_name="Network Security Tool"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark

def analyze_large_data_with_spark(file_path):
    spark = create_spark_session()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    df.show()
    return df
