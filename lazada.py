import pandas as pd
import requests
import json

# Import header
with open('config.json', 'r') as f:
    config = json.load(f)
    headers = config['Laz_headers']
raw_url = input('Enter the url to scrape: ')

# Retrieve product id
productID = raw_url.split('.html')[0].split('-i')[-1].split('-s')[0]

url = 'https://my.lazada.vn/pdp/review/getReviewList'
pageno = 0
df = pd.DataFrame(
    columns=['cmtID', 'comment', 'rating_star', 'item_name'])

while (True):
    params = {
        "itemId": productID,
        "pageSize": 10,
        "pageNo": pageno,
    }
    try:
        #Get data
        r = requests.get(url, headers=headers, params=params)

        res = json.loads(r.text)
        for i in res['model']['items']:
            rating_dict = {
                "cmtID": i['reviewRateId'],
                "comment": i['reviewContent'],
                "rating_star": i['rating'],
                "item_name": i['itemTitle']
            }
            print(rating_dict)
            row_df = pd.DataFrame(rating_dict, index=[0])
            df = pd.concat([df, row_df], ignore_index=True, axis=0)
        pageno += 2
    finally:
        continue
