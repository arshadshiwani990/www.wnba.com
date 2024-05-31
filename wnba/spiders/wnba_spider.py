import scrapy
import json

class WnbaSpiderSpider(scrapy.Spider):
    
    custom_settings = {
        'FEEDS': {
            'wnba.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True,
             
            },
        },
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.358280792.1717110934; _gid=GA1.2.332851628.1717110934; usprivacy=1---; OptanonAlertBoxClosed=2024-05-30T23:15:38.353Z; eupubconsent-v2=CP_as_gP_as_gAcABBENDgCsAP_AAAAAACiQJnQIYAFAAaABUADIAIAASAAqABaADIAHUARABFACTAEwATgAtgBfADCAIAAQgApACEAEWAI6ATsBGoCjwF5gMWAYyA2YBtQDbQG3gNzAmcAAAA4JAIAAWABUAEAAMgAiABMAEIAvMIAFABaAEkALYCjwGLBgBIACwAVABEACSAEwALYApAGLAMZEACQAFgAqACIAEkAJgAWwBSAMWAYyKABgAqACYAKQYADABUAEwAUg6AQAAsACoAIAAZABEACYARYBeY4ASAC0AJoAWwAvgCAAEIAKQAhADFiEAIABYATCAAMAJoAXwBSEoAgACwAiABMAXmSACgBNAC-AIQAUgDFikAcABYAFQAQABEACYARYBeZQAOAC0AGQATQAvgCEAFIAxYAA.f_gAAAAAAAAA; OptanonControl=ccc=PK&csc=&cic=1&otvers=202303.2.0&pctm=2024-05-30T23%3A15%3A38.353Z&reg=gdpr&ustcs=1---&vers=3.1.15-nba; AMCVS_248F210755B762187F000101%40AdobeOrg=1; _gcl_au=1.1.98120490.1717110941; AMCV_248F210755B762187F000101%40AdobeOrg=179643557%7CMCMID%7C44203109117624787472826860074248094655%7CMCAAMLH-1717715740%7C3%7CMCAAMB-1717715740%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1717118140s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; s_cc=true; aam_uuid=44200088532768052842824911154609732992; minVersion={"experiment":1026390581,"minFlavor":"Second Callmi-1.17.1.70.js100"}; aam_uuid=44200088532768052842824911154609732992; bm_mi=52F325C6E3F1EF1F20E44C2530C5885E~YAAQWZ42Fw/hw8mPAQAAUBLKyxdFaCHl5oZ60PPD33iNZxhDp7BFthHCrrNH50cwcGsNp6gZ1GbOvkPI3uQ/mQkNKgfDAjMVQs2kigMeNTUGZPpt60Si+pdxJFK8muczAnxE7czAUETUDOOoS2i9Olvca2vJasBOHpYjEr/7JY+UZWkIoKjIwc42k4Mu7smRZrk7ZF2TAEbLjJ8z/AOPZicclTMRmT4Yyamc5ViOE8dwnVXP/WToROzsf/t8pIGqECqTc5T1XpnMsEEg3Q+RlYPY+nKufwCmq9u3JqnkZwQR7NMyjY1Kmdg4fudYRPKq5GIHhENEiM0=~1; bm_sv=60F41A6F00A41AD7E6211F2ECAD88208~YAAQWZ42FxDhw8mPAQAAUBLKyxe0lCYBPTfuBk1Q83KyCg3pqgT1I7//snKTsvoKxYUiTD1OMEjpALLalwDFDuUJU/HOSyJDgEJvIgCCy8JrKtM0wgIdAh8RRzJPb8dDe08jtpzT1Ds710kyJjlbYeykthB2t+6n0I3KVJC+HMm94FQpnyxzr7VdJywXWZRIGAkoKCi03fc+x1FMDSIKi0Qv1hmQePPUtBbVLL/0NUaiph0a+n7T058kdT67EQ==~1; ak_bmsc=3722AE6E16401BE76B348FF71A516FD4~000000000000000000000000000000~YAAQWZ42F+vkw8mPAQAAfq3Kyxf7/9mUrCWTEVLVjM6dMrIZ3miX2UKOfAp2/goavaiB1SbXCvaLhgy6M4YbJIr7qvTgKK11+8RxZBQOYDGU4TU7RMUq8PLsuwSdA0ej4EY3u8cAJsRyazXXDbLsdDa7dK4t3B75k5yoFcvBIWo4XcbV80xL+rlgChtgr7QVZvSnrlNFXB4G+JZKXXF6EM7lFcwXwH+QIDFbIcqDvXu9qvpnxSDtxjcj2napEWc5OwtoyE8wqi7Wsef85FLl3im/N74JfzIF96mbyM2hmwEc36E9nyXzZiy77iuxEvWORAsKcHZrAgqAJTbw5YsmPgDYg2Spak9/9dMiFVhWpsiR589XJJ60bbyn48a7M6mlXl+Jx5yHRs4ZPkEkFKbU+tr7ou9RCKue+FaMq1ZyRMtRbp0zZvL0i7OIt+bHeo/JoLYfk4asI6RbKg6ncOpLXRHnwLl5AGnuY8cyt0DmEecrhA==; _ga_GELQE9ZCTK=GS1.2.1717110934.1.1.1717111075.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+31+2024+04%3A41%3A02+GMT%2B0500+(Pakistan+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1082e657-46f8-42a4-80ba-1eeae13cc0f5&interactionCount=1&landingPath=NotLandingPage&groups=dsa%3A1%2Ccad%3A1%2CNBAad%3A1%2Cmcp%3A1%2CNBAmt%3A1%2Cpad%3A1%2Cpap%3A1%2Cgld%3A1%2Cpcd%3A1%2Cpcp%3A1%2Cmra%3A1%2Cpdd%3A1%2Cmap%3A1%2Csid%3A1%2Csec%3A1%2Ctdc%3A1%2Ccos%3A1%2Cdlk%3A1%2Cdid%3A1%2Cven%3A1%2Creq%3A1&geolocation=PK%3B&AwaitingReconsent=false; __gads=ID=6c0e1e2c47ed578c:T=1717110947:RT=1717112463:S=ALNI_Maeteyq0KpjLR-nktJFcrIKLRlKYQ; __gpi=UID=00000e34897fcca2:T=1717110947:RT=1717112463:S=ALNI_MZtwjNRXi62pU5nzYGb_SZ3tA_qkw; __eoi=ID=509fec707d50aa5a:T=1717110947:RT=1717112463:S=AA-AfjapptSB2WAsh_JYGIKIoyAh; minUnifiedSessionToken10=%7B%22sessionId%22%3A%2249ca665d95-ebcad06e59-7be1dade66-fd3cb26990-f707221b68%22%2C%22uid%22%3A%22c2e8875837-c72d65d21d-43ef321a1c-1aa6fd585b-e6e6108e45%22%2C%22__sidts__%22%3A1717112464043%2C%22__uidts__%22%3A1717112464043%7D; s_ips=2188; s_tp=4287; s_ppv=wnba%253Astats%253Aplayer%253Arebecca-allen%253Ashooting%2C95%2C51%2C4071%2C13%2C21; _gat=1',
        # 'Referer': 'https://stats.wnba.com/player/1628263/shooting/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
    }
    
    name = 'wnba_spider'
    start_urls = ['https://www.wnba.com/players?team=all&position=all&show-historic-players=false']

    def parse(self, response):
        data = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        allPlayersData = json.loads(data).get('props').get('pageProps').get('allPlayersData')
        
        for player in allPlayersData:
            player_id = player[0]
            player_name = player[2] + " " + player[1]
            
            player_url = 'https://stats.wnba.com/stats/playerdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=10&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID=' + str(player_id) + '&PlusMinus=N&Rank=N&Season=2024&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision='
            
            yield scrapy.Request(url=player_url, callback=self.parse_player_page, headers=self.headers, meta={'player_name': player_name})
            
        
    def parse_player_page(self, response):
        data = response.json().get('resultSets')
        filtered_data = [item for item in data if item.get('name') == 'ShotTypePlayerDashboard']
        headers = filtered_data[0].get('headers')
        rowSet = filtered_data[0].get('rowSet')
        
        for row in rowSet:
            item = {}
            item['player_name'] = response.meta['player_name']
            for i in range(0, len(row)):
                value = row[i]
                key = headers[i]
                item[key] = value
                
            # Add player name to the item
            
            
            yield item