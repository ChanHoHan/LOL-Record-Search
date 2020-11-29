import requests
import json


if __name__ == "__main__":
    word = str(input("검색어 : "))
    request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-b7d085d6-5037-4f93-b540-fdf0e59dda24"}
    summoner_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + word
    s_response = requests.get(summoner_url,headers = request_headers)
    s_dict = json.loads(s_response.text)

    match_url = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/"+s_dict["puuid"]+"/ids?count=20"
    m_response = requests.get(match_url,headers = request_headers)
    m_dict = json.loads(m_response.text)

    for match in m_dict:
        print(match)
        record_url = "https://asia.api.riotgames.com/tft/match/v1/matches/" + match
        r_response = requests.get(record_url,headers = request_headers)
        print(r_response.text)