#!/bin/bash
#uvicorn luka_api:app --host 0.0.0.0 --workers 2 --log-level critical
#nohup uvicorn main:app --reload --host 0.0.0.0 > ./two2three.log &
uvicorn main:app --reload --host 0.0.0.0
