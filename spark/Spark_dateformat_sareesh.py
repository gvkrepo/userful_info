from datetime import dattetime
from pyspark.sql.functions import col,udf
from pyspark.sql.types import DateType
import Common
import re

spark_ENM_HW = SparkSession.builder.appName("enm_hw").getOrCreate()
v = []
l = ["2019-9-3","2019-12-31","2019-10-2","2020-2-12"]

for i in l:
	val = Row(START_DATE=i)
	v.append(val)
df = spark_ENM_HW.createDataFrame(v)
df.show()
func = udf(lambda x: datetime.strptime(x, '%Y-%m-%d'), DateType())
df1 =df.withColumn("dt".func(df['START_DATE']))
df1.show()