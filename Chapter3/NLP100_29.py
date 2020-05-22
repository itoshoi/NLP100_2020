'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''

import NLP100_28
import requests
import webbrowser
# from pprint import pprint

def get_url(titles):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action":"query",
        "format":"json",
        "prop":"imageinfo",
        "titles":titles,
        "iiprop":"url"
    }

    R = S.get(url=URL, params=PARAMS)

    DATA = R.json()
    # pprint(DATA)

    PAGES = DATA["query"]["pages"]

    for v in PAGES.values():
        return v["imageinfo"][0]["url"]

if __name__ == "__main__":
    dict = NLP100_28.get_template_no_mediawiki_markup()
    for k, v in dict.items():
        if k == "国旗画像":
            url = get_url("File:" + v)
            print(url)
            webbrowser.open(url)