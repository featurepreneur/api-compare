from flask import Flask, render_template
from flask import request
import json
import requests

app = Flask(__name__)

def getseconds(time:str):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

@app.route('/')
def checkspeed():
    r1 = requests.get("http://127.0.0.1:3000/")
    #print(r1)

    r2 = requests.get("http://127.0.0.1:4000/")
    #print(r2) 
     
    time1= getseconds(str(r1.elapsed))
    time2= getseconds(str(r2.elapsed))
    return render_template("index.html",t1=time1,t2=time2)
    
     
if __name__ == "__main__":
    app.run(debug=True,port=5000)    