#! /usr/bin/env python3

import os
import requests
user = os.getenv('USER')
path = "/home/{}/Feedback_Customers/data/feedback/".format(user)

keys =["title","name","date","feedback"]

folder = os.listdir(path)

for file in folder:
    keycount =0
    fb ={}

    with open(path+file) as fl:

        for line in fl:
            value =line.strip()
            fb[keys[keycount]] =value
            keycount +=1
    print(fb)
    response = requests.post("http://localhost/upload",
    json = fb)
    print(response.status_code)
