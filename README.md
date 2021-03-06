## FiveSimApi
<a href="https://pypi.python.org/pypi/fivesimapi"><img src="https://img.shields.io/pypi/v/fivesimapi.svg"></a>
<a href="https://pypi.python.org/pypi/fivesimapi"><img src="https://img.shields.io/pypi/pyversions/fivesimapi.svg"></a>

A modern, easy to use, and async API wrapper for [5sim.net](https://5sim.net/) in Python.

## Installation
Before proceeding, you should register an account on [5sim.net](https://5sim.net/) and generate a [Api key](https://5sim.net/settings/security) to use.

```pip install fivesimapi```

## Example Code
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
```
### Purchase
```python
# Buy activation number.
await client.buy_activation_number(country, operator, product)

# Buy hosting number.
await client.buy_hosting_number(country, operator, product)

# Buy again a old number.
await client.re_buy_number(product, number)
```
### Order Management
```python
# Check order history of a number by order's id..
await client.check_order(order_id)

# Get sms of a number by order's id.
await client.get_sms(order_id)

# Finish a order by order's id.
await client.finish_order(order_id)

# Cancel a order by order's id.
await client.cancel_order(order_id)

# Ban a order by order's id.
await client.ban_order(order_id)

# Provides sms inbox list by order's id.
await client.sms_inbox_list(order_id)
```
### Notifications
```python
# Get notifications.
await client.get_notifications(language)
```
### Vendors
```python
# Return Vendor statistics.
await client.vendor_stats()

# Available reserves currency for partner.
await client.wallets_reserve()

# Provides vendor's orders history by chosen category.
await client.vendor_orders_history(category)

# Provides vendor's payments history.
await client.vendor_payments_history()

# Create payouts for a partner.
await client.create_payouts(receiver, method, amount, fee)
```
### Countries List
```python
# Returns a list of countries with available operators for purchase.
await client.countries_list()
```
### Others
```python
# Return rates of cryptocurrencies.
await client.crypto_rates()

# Return address to crypto payment.
await client.get_deposit_address(amount, currency, address_type = None)
```
