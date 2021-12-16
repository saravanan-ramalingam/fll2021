import argparse
import logging
import sys

from pyspark.sql import SparkSession

ll_argv = sys.argv[1:]
parser = argparse.ArgumentParser()
parser.add_argument('-l', "--loglevel", help="Log Level")
parser.add_argument('-c', "--CheckLevel", help="Check Level")
args = parser.parse_args()
if args.loglevel is None or args.loglevel == "INFO":
    loglevel = logging.INFO
elif args.loglevel == "DEBUG":
    loglevel = logging.DEBUG
elif args.loglevel == "ERROR":
    loglevel = logging.ERROR

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s: %(message)s')
logger.info("Welcome")
# sc  = SparkContext()
# sqlContext = SQLContext(sc)
spark = SparkSession.builder.getOrCreate()
spark.sql("select 'HelloWorld' as Colname23Test").withColumnRenamed(
    "Colname23Test", "Thisistherealtestf11orprocess"
)
