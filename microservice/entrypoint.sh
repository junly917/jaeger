#!/bin/bash

python3 manage.py runserver 0.0.0.0:8080

tail -f debug.log
