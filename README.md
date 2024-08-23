# Shopee Comments Scrape

A python script to fetch shopee comments on a product using the shopee link of the product

## Nomenklatur Dataset

| Atribut         | Penjelasan                        |
| --------------- | --------------------------------- |
| nama pengguna   | nama user yang memberikan review  |
| review          | isi text review                   |
| rating          | rating yang diberikan pada produk |
| waktu transaksi | waktu user transaksi              |

## Persyaratan

Sebelum memulai, pastikan Anda telah memenuhi persyaratan berikut:

1. Anda telah menginstal Python 3.x.
2. Anda memiliki akses ke terminal atau antarmuka baris perintah.
3. Anda telah menginstal Git (opsional, untuk cloning repository).

## Installation

- Git Clone -> git clone https://github.com/AmmarulJ/Scraping-Shopee-Produk.git
- Masuk ke direktori - > cd Scraping-Shopee-Produk
- Follow this link (Make sure you have logged in shopee/lazada on your browser)
  - For Shopee: "https://shopee.vn/api/v2/item/get_ratings?itemid=17489310712&shopid=35445890&limit=12&offset=99"
  - For lazada" "https://my.lazada.vn/pdp/review/getReviewList?itemId=1982814076&pageSize=10&sort=0&pageNo=0"
- On the page, right click -> Inspect or F12.
- Choose Network tab then reload the page.
- On right side in the select Request Headers select raw then copy all.
- Convert the copied content into this format:
  ```
  {"headers": {
       "User-Agent": "...",
       "Accept": "...",
       "Accept-Language": "...",
       "Accept-Encoding": "...",
       "Upgrade-Insecure-Requests": "...",
       "Sec-Fetch-Dest": "..",
       "Sec-Fetch-Mode": "...",
       "Sec-Fetch-Site": "...",
       "Sec-Fetch-User": "...",
       "cookies": "...",
       "Connection": "..."
    }
  }
  ```
- Create config.json file and paste that.
