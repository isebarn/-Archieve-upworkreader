from ORM import Operations
from Parse import Ads
from Discord import send_messages
from flask import Flask, jsonify
import asyncio

app = Flask(__name__)

@app.route('/update')
def update():
  sites = Operations.GetAllKeywords()
  old_ads = Operations.GetAllIds()

  ads = Ads(sites)
  parsed_ads = ads.ads

  new_ads = [ad for ad in parsed_ads if ad['id'] not in old_ads]
  #[Operations.SaveAd(ad) for ad in new_ads]
  send_messages([x.Readable() for x in Operations.GetAll()])
  return jsonify([x.Readable() for x in Operations.GetAll()])



@app.route('/getads')
def getAds():
  return jsonify([x.Readable() for x in Operations.GetAll()])


if __name__ == "__main__":
  print(update())