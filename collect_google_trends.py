from pytrends.request import TrendReq

print("Starting...")

pytrend = TrendReq()

pytrend.build_payload(
    ["Python"],
    timeframe='today 3-m'
)

data = pytrend.interest_over_time()

print(data.head())
print("Done!")