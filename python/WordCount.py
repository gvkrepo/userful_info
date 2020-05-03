import sys
from pyspark import SparkContext

if _name_ == "_main_":
	sc = SparkContext("local[3]","word count")
	sc.setLogLevel("ERROR")
	lines = sc.textFile("/home/gvk/Desktop/word_count.txt")
	words = lines.flatMap(lambda line: line.spilt(" "))
	wordCounts = words.countByValue()
	for word, count in wordCounts.items():
		print(word,count)