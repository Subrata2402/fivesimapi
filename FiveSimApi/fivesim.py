import aiohttp, asyncio, json, requests, bs4

class NumberApi(object):
    def __init__(self, api_key: str = None):
        self.api_key = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODM5NDQ2OTIsImlhdCI6MTY1MjQwODY5MiwicmF5IjoiNmU3NWM0NzE1NjRmMjA1ZTlmNzZhNWYyYzkzMzlmYTIiLCJzdWIiOjEwNzcyODJ9.RxRJ2vxrwpw6J0BY0SnduNAXn3wnxxsNBlH-gGMsYZIW9YgUzc7L3TI13p3Pbqf9CR8rueHG0sWklZ9Xl_gYLyBa6_xNi0FTsnRo-wQiuOnuCeDtPjiqfiS_Q8ejt-VeTWKuhDJb8LqjVtilUmPPJIz2zId6LNjxaFnDWx_wq1lAtFyjyz4U2Ih4SQ9NaDlYqstsFfPRA8PRruHGCf9NKUIo-4oAfHb-UF1fBprio5FxRf6XBZ0F86b9tPA60xp5lGGNA8HWhbNA5IvH4N3erTijBjiJAx-CStsxB--xzPkMkBRlUkGEvlvw8xwGThyoGew1LaWAgSpqJRNSPMadEw"
        self.api_url = "https://5sim.net/v1"
        
    async def fetch(self, method = "GET", function = "", params = None, headers = None, data = None):
        headers = {"Accept": "application/json"}
        if self.api_key: headers["Authorization"] = self.api_key
        client_session = aiohttp.ClientSession()
        response = await client_session.request(method = method, url = self.api_url + function, params = None, headers = headers, data = data)
        content = await response.text()
        return json.loads(content)
        
    async def get_profile(self):
        return await self.fetch("GET", "/user/profile")
        
    async def order_history(self, category: str, limit = None, offset = None, order = None, reverse = None):
        params = {
            "category": category, # hosting or activation
            "limit": limit,
            "offset": offset,
            "order": order,
            "reverse": reverse # True or False
        }
        return await self.fetch("GET", "/user/orders", params)
        
    async def payment_history(self, limit = None, offset = None, order = None, reverse = None):
        params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "reverse": reverse # True or False
        }
        return await self.fetch("GET", "/user/payments", params)
        
    async def product_details(self, country: str = "any", operator: str = "any"):
        return await self.fetch("GET", "/guest/products/{}/{}".format(country, operator))
        
    async def get_prices(self, country: str = None, product: str = None):
        params = {
            "country": country,
            "product": product
        }
        return await self.fetch("GET", "/guest/prices", params)

    async def buy_activation_number(self, country: str, operator: str, product: str, forwarding = None, number = None, reuse = None, voice = None, ref = None):
        params = {
            "forwarding": forwarding,
            "number": number,
            "reuse": reuse,
            "voice": voice,
            "ref": ref
        }
        return await self.fetch("GET", "/user/buy/activation/{}/{}/{}".format(country, operator, product))
        
    async def buy_hosting_number(self, country: str, operator: str, product: str):
        return await self.fetch("GET", "/user/buy/hosting/{}/{}/{}".format(country, operator, product))
        
    async def re_buy_number(self, product, number):
        return await self.fetch("GET", "/user/reuse/{}/{}".format(product, number))
    
    async def check_order(self, id):
        return await self.fetch("GET", "/user/check/{}".format(id))
        
    async def get_sms(self, id):
        return await self.fetch("GET", "/user/check/{}".format(id))
        
    async def finish_order(self, id):
        return await self.fetch("GET", "/user/finish/{}".format(id))
        
    async def cancel_order(self, id):
        return await self.fetch("GET", "/user/cancel/{}".format(id))