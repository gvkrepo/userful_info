import sys
sys.path.insert(0,'.')
from pyspark import SparkContext, SparkConf
from commons.Utils import Utils

def splitComma(line:str):
	splits = Utils.COMMA_DELIMITER.split(line)
	return "{},{}".format(splits[1],splits[2])
	
if __name__ == "__main__"
	conf = SparkConf().setAppName("airports").setMaster("local[2]")
	sc = SparkContext(conf = conf)
	airports = sc.textFile("/home/hadoopuser/airportdata.csv")
	airporsInUSA = airports.filter(lambda line:Utils.COMMA_DELIMITER.split(line)[3] == "\"Iceland\"")
	
	airporsNameAndCityNames = airporsInUSA.map(spiltComa)
	airporsNameAndCityNames.saveAsTextFile("/home/hadoopuser/airporsInUSA.txt")