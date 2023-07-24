#!/bin/bash
# curl test getPrediction
curl -X POST -H "Content-Type: application/json" -d '{"data": "서버 개발자 지원"}' http://localhost:8000/predict