### FiveSimApi
A modern, easy to use, and async API wrapper for 5sim.net in Python.

### Installation
Before proceeding, you should register an account on 5sim.net and generate a [Api key](https://5sim.net/settings/security) to use.

```pip install fivesimapi```

### Example Code
```python
import FiveSimApi, asyncio
from FiveSimApi import fivesim

api_key = "....." # put your api key here

async def main():
    client = fivesim.FiveSim(api_key)
    data = await client.get_profile()
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
### User
```python
# Provides profile data: email, balance and rating.
await client.get_profile()

# Provides orders history by choosen category.
await client.order_history(category)

# Provides payments history.
await client.payment_history()
```
### Product and Prices
```python
# To receive the name, the price, quantity of all products, available to buy.
await client.product_details(country, product)

# Returns product prices.
await client.get_prices()

# Returns product prices by country.
await client.get_prices_by_country(country)

# Returns product prices for a specific product.
await client.get_prices_by_product(product)

# Returns product prices by country and specific product.
await client.get_prices_by_country_and_product(country, product)

