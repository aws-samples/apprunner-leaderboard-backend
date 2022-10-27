from flask import Flask
import logging
import os
import requests
import redis
import json
import random

app = Flask(__name__)
    
@app.route("/getdata")
def root():
  logging.basicConfig(level=logging.DEBUG)
  REDIS_URL = os.getenv('REDIS_URL')
  logging.debug("Getting redis path" + str(REDIS_URL))
  r = redis.Redis(host=REDIS_URL, port=6379, db=0)
  leaderboard_data = r.get('leaderboard_data')

  # Randomly change player scores
  random_json = json.loads(leaderboard_data);
  for val in random_json:
    val['score'] = random.randint(1000, 3000)
  random_json.sort(key=lambda x: x["score"], reverse=True)

  rank = 0
  for val in random_json:
    rank = rank + 1
    val['id'] = rank
  
  logging.info("Response: " + str(random_json))
  return str(random_json).replace("\'", "\"")

if __name__ == "__main__":
  app.run()

