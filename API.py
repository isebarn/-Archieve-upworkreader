from ORM import Operations
from Parse import Ads
from flask import Flask, jsonify
import asyncio
from Discord import MSG

app = Flask(__name__)

@app.route('/update')
def update():
  sites = Operations.GetAllKeywords()
  old_ads = Operations.GetAllIds()

  ads = Ads(sites)
  parsed_ads = ads.ads

  new_ads = [ad for ad in parsed_ads if ad['id'] not in old_ads]
  [Operations.SaveAd(ad) for ad in new_ads]

  msg = MSG(new_ads)

  return jsonify([x.Readable() for x in Operations.GetAll()])


@app.route('/msg')
def msg():

  ads = [{'id': '01d33e2d5b0742ea28', 'title': 'Lead generation to find MSPs in USLead generation to find MSPs in US', 'url': 'https://www.upwork.com/job/Lead-generation-find-MSPs_~01d33e2d5b0742ea28/', 'payment': 'Fixed: $10'}]
  msg = MSG(ads)

  return jsonify(ads)


@app.route('/getads')
def getAds():
  return jsonify([x.Readable() for x in Operations.GetAll()])


if __name__ == "__main__":
  print(update())