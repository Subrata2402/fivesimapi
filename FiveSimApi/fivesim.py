import aiohttp, asyncio, json

class FiveSim(object):
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
        """Provides profile data: email, balance and rating."""
        return await self.fetch("GET", "/user/profile")
        
    async def order_history(self, category: str, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        """Provides orders history by choosen category."""
        params = {"category": category, "limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/user/orders", params)
        
    async def payment_history(self, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        """Provides payments history."""
        params = {"limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/user/payments", params)
        
    async def product_details(self, country: str = "any", operator: str = "any"):
        """To receive the name, the price, quantity of all products, available to buy."""
        return await self.fetch("GET", "/guest/products/{}/{}".format(country, operator))
        
    async def get_prices(self, country: str = None, product: str = None):
        """Returns product prices by country and specific product."""
        params = {"country": country, "product": product}
        return await self.fetch("GET", "/guest/prices", params = params)

    async def buy_activation_number(self, country: str, operator: str, product: str, forwarding: str = None, number: str = None, reuse: str = None, voice: str = None, ref: str = None):
        """Buy a activation number."""
        params = {"forwarding": forwarding, "number": number, "reuse": reuse, "voice": voice, "ref": ref}
        return await self.fetch("GET", "/user/buy/activation/{}/{}/{}".format(country, operator, product))
        
    async def buy_hosting_number(self, country: str, operator: str, product: str):
        """Buy a hosting number."""
        return await self.fetch("GET", "/user/buy/hosting/{}/{}/{}".format(country, operator, product))
        
    async def re_buy_number(self, product: str, number: str):
        """Buy again a old number."""
        return await self.fetch("GET", "/user/reuse/{}/{}".format(product, number))
    
    async def check_order(self, id):
        """Check order history of a number."""
        return await self.fetch("GET", "/user/check/{}".format(id))
        
    async def get_sms(self, id):
        """Get sms of a number."""
        return await self.fetch("GET", "/user/check/{}".format(id))
        
    async def finish_order(self, id):
        """Finish a order by order."""
        return await self.fetch("GET", "/user/finish/{}".format(id))
        
    async def cancel_order(self, id):
        """Cancel a order by order's id."""
        return await self.fetch("GET", "/user/cancel/{}".format(id))
        
    async def ban_order(self, id):
        """Ban a order by order's id."""
        return await self.fetch("GET", "/user/ban/{}".format(id))
    
    async def sms_inbox_list(self, id):
        """Get SMS inbox list by order's id."""
        return await self.fetch("GET", "/user/sms/inbox/{}".format(id))
        
    async def crypto_rates(self):
        """Return rates of cryptocurrencies."""
        return await self.fetch("GET", "/user/payment/crypto2/rates")
        
    async def get_deposit_address(self, amount: str, currency: str, address_type: str = None):
        """Return address to crypto payment."""
        data = {"amount": amount, "currency": currency, "address_type": address_type}
        return await self.fetch("POST", "/user/payment/crypto2/invoice", data = data)
        
    async def get_notifications(self, lang: str):
        """Get a flash notification."""
        return await self.fetch("GET", "/guest/flash/{}".format(lang))
        
    async def vendor_stats(self):
        """Return Vendor statistics."""
        return await self.fetch("GET", "/user/vendor")
        
    async def wallets_reserve(self):
        """Available reserves currency for partner."""
        return await self.fetch("GET", "/vendor/wallets")
        
    async def vendor_orders_history(self, category: str, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        """Provides vendor's orders history by chosen category."""
        params = {"category": category, "limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/vendor/orders", params = params)
        
    async def vendor_payments_history(self, limit: str = None, offset: str = None, order: str = None, reverse: str = None):
        """Provides vendor's payments history."""
        params = {"limit": limit, "offset": offset, "order": order, "reverse": reverse}
        return await self.fetch("GET", "/vendor/payments", params = params)
        
    async def create_payouts(self, receiver: str, method: str, amount: str, fee: str):
        """Create payouts for a partner."""
        data = {"receiver": receiver, "method": method, "amount": amount, "fee": fee}
        return await self.fetch("POST", "/vendor/withdraw", data = data)
        
    async def countries_list(self):
        """Returns a list of countries with available operators for purchase."""
        return await self.fetch("GET", "/guest/countries")
