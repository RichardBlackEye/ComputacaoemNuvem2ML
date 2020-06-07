from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.feature import VectorAssembler

# Server
import uvicorn              #connexion
from fastapi import FastAPI

app = FastAPI()


sc = SparkContext()

spark = SparkSession(sc)

model = RandomForestClassificationModel.load("gs://germl/model")

data= spark.read.format("bigquery").option("table", "germany_regression.germany").load()


# create features vector
feature_columns =['NY_ADJ_NNTY_KD_ZG','NY_ADJ_NNTY_KD','NY_ADJ_NNTY_CD','NY_ADJ_NNTY_PC_KD_ZG','NY_ADJ_NNTY_PC_KD','NY_ADJ_NNTY_PC_CD','NY_ADJ_SVNX_GN_ZS','NY_ADJ_SVNX_CD','NY_ADJ_SVNG_GN_ZS'] # here we omit the final column


assembler = VectorAssembler(inputCols=feature_columns,outputCol="features")

data_2 = assembler.transform(data)

algo = RandomForestClassifier(featuresCol='features', labelCol='Crise')
model = algo.fit(data_2) 

model.save("gs://germl/model")

@app.post("/predict")

def predict():

    predictions = model.transform(data_2) 

    #predictions.select(['Crise','prediction', 'probability']).show()

    return (predictions.select(['Crise','prediction', 'probability']))
