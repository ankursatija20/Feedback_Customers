#! /usr/bin/env python3

import os
import requests

path = "/home/kali/Realwrld/week2/data/feedback/"

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
    response = requests.post("http://10.0.2.15/feedback/",
    json = fb)




    print(response.request.body)
    print(response.status_code)
