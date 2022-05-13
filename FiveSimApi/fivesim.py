import aiohttp, asyncio, json, requests, bs4

class NumberApi(object):
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.api_url = "https://5sim.net/v1"
        
    async def fetch(self, method = "GET", function = "", params = None, headers = None, data = None):
        headers = {"Accept": "application/json"}
        if self.api_key: headers["Authorization"] = self.api_key
        async with aiohttp.ClientSession() as client_session:
            response = await client_session.request(method = method, url = self.api_url + function, params = None, headers = headers, data = data)
            content = await response.json()
            return content
        
    async def get_profile(self):
        return await self.fetch("GET", "/user/profile")
        
    async def order_history(self, category: str, limit = None, offset = None, order = None, reverse = None):
        params = {"category": category, "limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/user/orders", params)
        
    async def payment_history(self, limit = None, offset = None, order = None, reverse = None):
        params = {"limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/user/payments", params)
        
    async def product_details(self, country: str = "any", operator: str = "any"):
        return await self.fetch("GET", "/guest/products/{}/{}".format(country, operator))
        
    async def get_prices(self, country: str = None, product: str = None):
        params = {"country": country, "product": product}
        return await self.fetch("GET", "/guest/prices", params)

    async def buy_activation_number(self, country: str, operator: str, product: str, forwarding = None, number = None, reuse = None, voice = None, ref = None):
        params = {"forwarding": forwarding, "number": number, "reuse": reuse, "voice": voice, "ref": ref}
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
        
    async def ban_order(self, id):
        return await self.fetch("GET", "/user/ban/{}".format(id))
    
    async def sms_inbox_list(self, id):
        return await self.fetch("GET", "/user/sms/inbox/{}".format(id))
        
    async def crypto_rates(self):
        return await self.fetch("GET", "/user/payment/crypto2/rates")
        
    async def get_deposit_address(self, amount: str, currency: str, address_type: str = None):
        data = {"amount": amount, "currency": currency, "address_type": address_type}
        return await self.fetch("POST", "/user/payment/crypto2/invoice", data = data)
        
    async def get_notifications(self, lang: str):
        return await self.fetch("GET", "/guest/flash/{}".format(lang))
        
    async def vendor_stats(self):
        return await self.fetch("GET", "/user/vendor")
        
    async def wallets_reserve(self):
        return await self.fetch("GET", "/vendor/wallets")
        
    async def vendor_orders_history(self, category: str, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        params = {"category": category, "limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/vendor/orders", params = params)
        
    async def vendor_payments_history(self, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        params = {"limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/vendor/payments", params = params)
        
    async def create_payouts(self, receiver: str, method: str, amount: str, fee: str):
        data = {"receiver": receiver, "method": method, "amount": amount, "fee": fee}
        return await self.fetch("POST", "/vendor/withdraw", data = data)
        
    async def countries_list(self):
        return await self.fetch("GET", "/guest/countries")