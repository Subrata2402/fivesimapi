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
    five_sim = fivesim.FiveSim(api_key)
    data = await five_sim.get_profile()
    print(data) # return json data of your profile

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
