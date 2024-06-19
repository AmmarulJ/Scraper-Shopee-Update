# Shopee Comments Scrape
A python script to fetch shopee comments on a product using the shopee link of the product
## Installation
1. Follow this link "https://shopee.vn/api/v2/item/get_ratings?itemid=17489310712&shopid=35445890&limit=12&offset=99" (Make sure you have logged in shopee on your browser)
2. On the page, right click -> Inspect or F12.
3. Choose Network tab then reload the page.
4. On right side in the select Request Headers select raw then copy all.
5. Convert the copied content into this format:
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
6. Create config.json file and paste that.
