import pandas as pd
import requests
import json
from datetime import datetime

# Fungsi untuk membersihkan dan memformat nama produk dari URL
def clean_product_name(raw_url):
    # Ambil nama produk dari URL dan ganti karakter yang tidak valid untuk nama file
    product_name = raw_url.split('/')[-1].split('?')[0]
    product_name = product_name.replace('-', '_').replace(' ', '_').replace('(', '').replace(')', '')
    return product_name

# Load config.json untuk header
with open('config.json', 'r') as f:
    config = json.load(f)
    headers = config['Shopee_headers']

# Input URL produk dan jumlah komentar yang ingin diambil
raw_url = input('Enter the url to scrape: ')
num_of_comments = int(input('Enter the number of comments: '))

# Membersihkan nama produk dan mendapatkan timestamp
product_name = clean_product_name(raw_url)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"{product_name}_{timestamp}.csv"

offset = 0
all_data = []

while num_of_comments > 0:
    try:
        # API endpoint dan parameters
        url = "https://shopee.vn/api/v2/item/get_ratings"
        params = {
            "itemid": raw_url.split('/')[5],
            "shopid": raw_url.split('/')[4],
            "limit": 59,
            "offset": offset
        }

        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        res = response.json()

        if 'data' in res and 'ratings' in res['data']:
            ratings = res['data']['ratings']
        else:
            print("No more data available or response does not contain expected data.")
            break

        for rating in ratings:
            item_name = rating.get('original_item_info', {}).get('name', 'Unknown')  # Menggunakan 'Unknown' jika 'name' tidak ditemukan
            
            # Mengonversi waktu transaksi dari timestamp
            waktu_transaksi = datetime.fromtimestamp(rating.get("ctime", 0)).strftime("%Y-%m-%d %H:%M")

            rating_dict = {
                "Comment ID": rating['cmtid'],
                "Item ID": rating['itemid'],
                "Shop ID": rating['shopid'],
                "Username": rating.get('author_username', 'Unknown'),  # Menggunakan Username
                "Comment": rating['comment'],
                "Rating Star": rating['rating_star'],  # Rating bintang
                "User Name": rating.get('author_username', 'Unknown'),  # Memastikan nilai default jika key tidak ada
                "Anonymous": rating['anonymous'],
                "Region": rating['region'],
                "Item Name": item_name,
                "Waktu Transaksi": waktu_transaksi  # Waktu transaksi dengan format yang diminta
            }
            all_data.append(rating_dict)
            print(rating_dict)
            num_of_comments -= 1
            if num_of_comments == 0:
                break
        offset += 59

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_data)

# Save DataFrame to a CSV file with headers
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Scraping completed. Data saved to {output_file}")
