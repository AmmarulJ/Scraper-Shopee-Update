import pandas as pd
import requests
import json

with open('config.json', 'r') as f:
    config = json.load(f)
    headers = config['headers']

raw_url = input('Enter the url to scrape: ')
num_of_comments = int(input('Enter the number of comments: '))
offset = 0
while (True):

    # API endpoint and parameters
    url = "https://shopee.vn/api/v2/item/get_ratings"
    params = {
        "itemid": raw_url.split('i.')[1].split('.')[1].split('?')[0],
        "shopid": raw_url.split('i.')[1].split('.')[0],
        "limit": 59,
        "offset": offset
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Print the response
    res = json.loads(response.text)
    ratings = res['data']['ratings']
    df = pd.DataFrame(
        columns=['cmtID', 'itemID', 'shopID', 'userID', 'comment', 'rating_star', 'user_name', 'anonymous', 'region',
                 'item_name'])

    for rating in ratings:
        rating_dict = {
            "cmtID": rating['cmtid'],
            "itemID": rating['itemid'],
            "shopID": rating['shopid'],
            "userID": rating['userid'],
            "comment": rating['comment'],
            "rating_star": rating['rating_star'],
            "user_name": rating['author_username'],
            "anonymous": rating['anonymous'],
            "region": rating['region'],
            "item_name": rating['original_item_info']['name'],
        }
        print(rating_dict)
        row_df = pd.DataFrame(rating_dict, index=[0])
        df = pd.concat([df, row_df], ignore_index=True, axis=0)
        num_of_comments -= 1
        if num_of_comments == 0:
            break
    if num_of_comments == 0:
        break
    offset += 59
