rom ORM import Operations
from Parse import Ads
from Discord import Discord
from flask import Flask, jsonify
import asyncio

app = Flask(__name__)


@app.route('/getads')
def getAds():
  return jsonify([x.Readable() for x in Operations.GetAll()])


if __name__ == "__main__":
  print(update())