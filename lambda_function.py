import requests
import datetime
import random

# 年の取得
year = datetime.datetime.now().year

thumbnail_url = [
    "https://nra.resonite.org/VRChat_2023-11-20_02-35-09.639_1920x1080.png",
    "https://nra.resonite.org/VRChat_2023-11-03_07-05-25.819_1920x1080.png",
    "https://nra.resonite.org/VRChat_2023-10-04_01-09-00.467_2160x3840.png",
    "https://nra.resonite.org/VRChat_2023-11-03_07-05-25.819_1920x1080.png"

]

Genere = [
    "business", 
    "entertainment", 
    "general", 
    "health", 
    "science", 
    "sports", 
    "technology"
]

# DiscordのWebhook URL
discord_url0 = 'xxxxx' 

#画像をランダムで選択
thumbnail_url_set = random.choice(thumbnail_url)
#ジャンルをランダムで選択
genere_set = random.choice(Genere)
# リクエストの設定
headers = {'X-Api-Key': 'APIキー'} #APIキーは自分のものを入れる
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'category': genere_set,
    'country': 'jp',
    'pageSize': 5
}

# リクエストを送る
response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)

# 通信が成功した場合
if response.ok:

    date_time0 = data['articles'][0]['publishedAt']
    title0 = data['articles'][0]['title']
    url0 = data['articles'][0]['url']

    data_time1 = data['articles'][1]['publishedAt']
    title1 = data['articles'][1]['title']
    url1 = data['articles'][1]['url']

    data_time2 = data['articles'][2]['publishedAt']
    title2 = data['articles'][2]['title']
    url2 = data['articles'][2]['url']

    data_time3 = data['articles'][3]['publishedAt']
    title3 = data['articles'][3]['title']
    url3 = data['articles'][3]['url']

    data_time4 = data['articles'][4]['publishedAt']
    title4 = data['articles'][4]['title']
    url4 = data['articles'][4]['url']

    # 画像の取得
    img = [
        data['articles'][0]['urlToImage'],
        data['articles'][1]['urlToImage'],
        data['articles'][2]['urlToImage'],
        data['articles'][3]['urlToImage'],
        data['articles'][4]['urlToImage']
    ]

    #画像をランダムで選択
    dog_url = random.choice(img)

    # 通知内容を作成
    send_data = {
            "username": "News Bot", #Botの名前
            "avatar_url": "{アイコン画像URL}", #discordのアイコン画像URL
            "content": "{コメント}" , #コメント内容
            "timestamp" : str(datetime.datetime.now().isoformat()),
            "embeds": [
                {
                    "title" : ":newspaper:今日の{Genre}のニュース".format(Genre=genere_set),
                    "color" : 0x00ffff,
                    "footer": {
                        "text": "© 2002-{year} ".format(year=year), #フッターに入れる文字を指定する
                        "icon_url": "" #アイコン画像URL
                    },
                    "thumbnail": {
                        "url": thumbnail_url_set
                    },
                    "image": {
                        "url": dog_url
                    },
                    "fields": [
                        {
                            "name" : "Topic-1",
                            "value" : title0 + "\n" + url0,
                        },
                        {
                            "name" : "Topic-2",
                            "value" : title1 + "\n" + url1,
                        },
                        {
                            "name" : "Topic-3",
                            "value" : title2 + "\n" + url2,
                        },
                        {
                            "name" : "Topic-4",
                            "value" : title3 + "\n" + url3,
                        },
                        {
                            "name" : "Topic-5",
                            "value" : title4 + "\n" + url4,
                        }
                    ]
                }
            ]
        }

    # 通知を送る
    requests.post(discord_url0, json=send_data) 
  
    


