# import requests
# from twilio.rest import Client
#
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#
# account_sid = "ACc9563c4a0df11b1cb81200a716b8620b"
# auth_token = "da4310b1ee89f5bfc6b5c6e5bb36fad2"
#
# ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# function = "TIME_SERIES_DAILY_ADJUSTED"
# symbol = STOCK_NAME
# STOCK_API_KEY = "IHH4UY4TR1V0I9EK"
# NEWS_API_KEY = "462bcc903cc34a178ad67c5fd574d9de"
#
# stock_params = {
#     "function": function,
#     "symbol": symbol,
#     "apikey": STOCK_API_KEY,
# }
#
# response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]
# # print(stock_data)
# # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# data_list = [value for (key, value) in stock_data.items()]
# # print(data_list)
#
# yday_closing_price = float(data_list[0]["4. close"])
# # TODO 2. - Get the day before yesterday's closing stock price
# closing_price_before_yday = float(data_list[1]["4. close"])
# # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# closing_price_diff = abs(yday_closing_price - closing_price_before_yday)
# # print(closing_price_diff)
# # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# percentage_diff = (closing_price_diff/yday_closing_price) * 100
# # print(percentage_diff)
# # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if percentage_diff > 1:
#     # print("Get News")
# ## STEP 2: https://newsapi.org/
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
# # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#     news_params = {
#         "qInTitle": COMPANY_NAME,
#         "apiKey": NEWS_API_KEY,
#     }
#
#     news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
#     news_response.raise_for_status()
#     news_data_articles = news_response.json()["articles"]
#     # print(news_data_articles)
#
# # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
#     first_three_articles = news_data_articles[:3]
#     # print(first_three_articles)
#
# ## STEP 3: Use twilio.com/docs/sms/quickstart/python
# # to send a separate message with each article's title and description to your phone number.
#
# # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#     formatted_headlines_and_desc = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]
#     print(formatted_headlines_and_desc)
# # TODO 9. - Send each article as a separate message via Twilio.
#     client = Client(account_sid, auth_token)
#
# # Optional TODO: Format the message like this:
#     for article in formatted_headlines_and_desc:
#         message = client.messages.create(
#             body=article,
#             from_='+18776413072',
#             to='+17133519231'
#         )
#         print(message.status)
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = '+18776413072'
VERIFIED_NUMBER = '+17133519231'

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "***"
NEWS_API_KEY = "***"
TWILIO_SID = "***"
TWILIO_AUTH_TOKEN = "***"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


    ## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#If difference percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        print(message.status)