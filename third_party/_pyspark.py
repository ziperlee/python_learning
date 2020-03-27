"""
 Created by liwei on 2020/3/27.
"""
import pandas as pd
from pyspark.sql import SparkSession

session = (
    SparkSession.builder.appName("spark_pyspark")
        .config("hive.metastore.uris", "thrift://10.57.239.240:9083")
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
        .enableHiveSupport()
        .getOrCreate()
)

pdf = pd.read_csv('/tmp/fetch/tm_test_datac2e0f373e8254ba18722f2a05be21a6e/transformated_sample.csv')

df = session.createDataFrame(pdf, schema)
