import mysql.connector
from SimilarSentences import SimilarSentences
import json
import random
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='9840382936',
    database ="chatdata"
)
my_cursor = mydb.cursor()

def chatAnswer(text):
    model = SimilarSentences('model.zip',"predict")
    detailed = model.predict(text, 1, "detailed")
    detailed = detailed.replace("[","")
    detailed = detailed.replace("]","")
    jsonReturn = json.loads(detailed)
    if jsonReturn['score'] >=0.80:
        simple=jsonReturn['sentence']
        my_cursor.execute("SELECT * FROM trafficData WHERE questions=%s",(simple,))
        result =my_cursor.fetchall()
        return result[0][2]
    else:
        return "No"
