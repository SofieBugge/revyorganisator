#!/bin/bash
#Starts the python test server.

nohup python3 ./mysite/manage.py runserver 192.168.2.2:8000 &
