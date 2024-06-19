# Shopee Comments Scrape
A python script to fetch shopee comments on a product using the shopee link of the product
## Installation
1. Follow this link (Make sure you have logged in shopee/lazada on your browser)
   For Shopee: "https://shopee.vn/api/v2/item/get_ratings?itemid=17489310712&shopid=35445890&limit=12&offset=99"
   For lazada" "https://my.lazada.vn/pdp/review/getReviewList?itemId=1982814076&pageSize=10&sort=0&pageNo=0"
3. On the page, right click -> Inspect or F12.
4. Choose Network tab then reload the page.
5. On right side in the select Request Headers select raw then copy all.
6. Convert the copied content into this format:
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
7. Create config.json file and paste that.
