import aiohttp, asyncio, json, requests, bs4

class NumberApi(object):
    def __init__(self):
        self.api_key = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODM5NDQ2OTIsImlhdCI6MTY1MjQwODY5MiwicmF5IjoiNmU3NWM0NzE1NjRmMjA1ZTlmNzZhNWYyYzkzMzlmYTIiLCJzdWIiOjEwNzcyODJ9.RxRJ2vxrwpw6J0BY0SnduNAXn3wnxxsNBlH-gGMsYZIW9YgUzc7L3TI13p3Pbqf9CR8rueHG0sWklZ9Xl_gYLyBa6_xNi0FTsnRo-wQiuOnuCeDtPjiqfiS_Q8ejt-VeTWKuhDJb8LqjVtilUmPPJIz2zId6LNjxaFnDWx_wq1lAtFyjyz4U2Ih4SQ9NaDlYqstsFfPRA8PRruHGCf9NKUIo-4oAfHb-UF1fBprio5FxRf6XBZ0F86b9tPA60xp5lGGNA8HWhbNA5IvH4N3erTijBjiJAx-CStsxB--xzPkMkBRlUkGEvlvw8xwGThyoGew1LaWAgSpqJRNSPMadEw"
        self.api_url = "https://5sim.net/v1/user"
        
    async def fetch(self, method = "GET", function = "", params = None, headers = None, data = None):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Accept": "application/jsoncurl"
        }
        client_session = aiohttp.ClientSession()
        response = await client_session.request(method = method, url = self.api_url + function, params = None, headers = headers, data = data)
        content = await response.text()
        return json.loads(content)