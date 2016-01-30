## Wenxiao Gu

## http://renien.github.io/blog/accessing-pyspark-pycharm/
## brew install apache-spark

import os,sys

# Path for spark source folder
# os.environ['SPARK_HOME']="/usr/local/Cellar/apache-spark/1.6.0"
os.environ['SPARK_HOME']="/Users/wenxiaog/bigdata220/spark152/"
os.environ['PYTHONPATH']="/Users/wenxiaog/bigdata220/spark152/python/lib/py4j-0.8.2.1-src.zip"
# Append pyspark  to Python Path
# sys.path.append("/usr/local/Cellar/apache-spark/1.6.0/libexec/python/")
sys.path.append("/Users/wenxiaog/bigdata220/spark152/python/")


from pyspark import SparkContext
from pyspark import SparkConf
## add the following into the environmental variables
# export PYTHONPATH=/Users/wenxiaog/bigdata220/spark152//python/lib/py4j-0.8.2.1-src.zip:$PYTHONPATH

## Test
# Initialize SparkContext
# sc = SparkContext('local')
# words = sc.parallelize(["scala","java","hadoop","spark","akka"])
# print words.count()


## Data cleaning with the Car Data set
## Big Data 220 Class3
# https://gitlab0.bigdata220uw.mooo.com/jhenri/uwbd-instructions/blob/master/Spark%20Tutorial%20Class%203.md
## read csv file

## show the data

conf = SparkConf().setMaster("local").setAppName("My App1")
sc = SparkContext(conf = conf)



os.getcwd()


## Example 11-1. Spam Classifier in python

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import LogisticRegressionWithSGD

spam = sc.textFile("learning-spark/files/spam.txt")
normal = sc.textFile("learning-spark/files/normal.txt")



from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.split(' ')]
    return LabeledPoint(values[0], values[1:])

data = sc.textFile("data/mllib/sample_svm_data.txt")
parsedData = data.map(parsePoint)

# Build the model
model = SVMWithSGD.train(parsedData, iterations=100)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))

# Save and load model
model.save(sc, "myModelPath")
sameModel = SVMModel.load(sc, "myModelPath")







############################################
#### data-from-spark_bin-1.5.2 #############
############################################

## SVM model

from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.split(' ')]
    return LabeledPoint(values[0], values[1:])

data = sc.textFile("data-from-spark_bin-1.5.2/mllib/sample_svm_data.txt")
parsedData = data.map(parsePoint)

# Build the model
model = SVMWithSGD.train(parsedData, iterations=100)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))

# Save and load model
model.save(sc, "myModelPath")
sameModel = SVMModel.load(sc, "myModelPath")

## Linear regression, Lasso (L1), and Ridge (L2)
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.replace(',', ' ').split(' ')]
    return LabeledPoint(values[0], values[1:])

data = sc.textFile("data-from-spark_bin-1.5.2/mllib/ridge-data/lpsa.data")
parsedData = data.map(parsePoint)

# Build the model
model = LinearRegressionWithSGD.train(parsedData)

# Evaluate the model on training data
valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
MSE = valuesAndPreds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()
print("Mean Squared Error = " + str(MSE))

# Save and load model
model.save(sc, "myModelPath2")
sameModel = LinearRegressionModel.load(sc, "myModelPath2")
