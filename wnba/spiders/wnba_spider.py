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
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
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