from ORM import Operations
from Parse import Ads
from Discord import Discord

def update():
    sites = Operations.GetAllKeywords()
    old_ads = Operations.GetAllIds()

    ads = Ads(sites)
    parsed_ads = ads.ads

    new_ads = [ad for ad in parsed_ads if ad['id'] not in old_ads]
    [Operations.SaveAd(ad) for ad in new_ads]
    Discord(new_ads)

if __name__ == "__main__":
  update()