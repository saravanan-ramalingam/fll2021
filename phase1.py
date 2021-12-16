import sys
import pyspark.sql.functions as f
from pyspark import SQLContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

print(sys.path)
# sc  = SparkContext()
# sqlContext = SQLContext(sc)
spark = SparkSession.builder.getOrCreate()
spark.sql("select 'HelloWorld'")
