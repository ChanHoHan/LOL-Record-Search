import requests

if __name__ == "__main__":
    word = str(input("검색어 : "))
    url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + word

    request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-bd3ce269-f928-4eb5-9aa8-093cdfa83db3"}
    response = requests.get(url,headers = request_headers)
    print(response.text)