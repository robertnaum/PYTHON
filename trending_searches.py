from pytrends.request import TrendReq

pytrends = TrendReq()
# region = input('enter the region: ')
# trending = pytrends.trending_searches(pn=region)
# print (trending)


keywords = ['Python','Java','C++']
pytrends.build_payload(keywords, timeframe='today 12-m')
data = pytrends.interest_over_time()
print (data)