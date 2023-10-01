from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession \
    .builder \
    .appName("Postgres Table Load") \
    .master("local") \
    .enableHiveSupport().getOrCreate()


dburl="jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"

database_name_hive = "fraud_project"
table_name_hive = "fraud_full_load_external"


table_name_postgres = "frauddetection_sample"


hive_query = "select max(row_id) from fraud_project.fraud_full_load_external"

max = spark.sql(hive_query)

max = max.first()['max(row_id)']

postgres_query = "(select * from " + table_name_postgres +" where row_id >"+str(max)+ ") as max_table"

df = spark.read.format("jdbc").option("url",dburl) \
    .option("driver", "org.postgresql.Driver").option("dbtable", postgres_query) \
    .option("user", "consultants").option("password", "WelcomeItc@2022").load()

df.write.mode('append').format("parquet").saveAsTable(database_name_hive+ "." + table_name_hive)


spark.stop()
