import requests
import json
while True:
    data=input("Which news you want to read??(Press -1 or quit to quit)")
    if data=="quit" or data=="-1":
        break
    url=f"https://newsdata.io/api/1/latest?apikey=pub_6912004c0a4f6d4c52cc96580f4b57af8541e&q={data}&country=in&language=en"
    a=requests.get(url)
    news = json.loads(a.text)
    if news["totalResults"] != 0:
        for articles in news["results"]:
            print("_____" * 25)
            print(articles["title"])#title = article.get("title", "  ")
            print(articles["description"])
            print("_____" * 25)
    else:
        print(f"There is no news available on {data}.\n Please search for another news ")
    