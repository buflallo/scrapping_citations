import scrapy
from scrapy.http import headers
import re

class CarDealersSpider (scrapy.Spider):
    name = "car_dealers"
    headers_home_advisor = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'cookiesEnabled': '1',
        'aff_track': '2|*|23116563|*|0',
        'originatingSessionID': '1676851529514site-545fb5b75d-j86fh7C38B8E749F44BD3446ABB1AE77C762F',
        'csacn': '746971',
        'AMCVS_D5C06A65527038CC0A490D4D@AdobeOrg': '1',
        's_ecid': 'MCMID|33561830398888401901318217502581917265',
        'AMCV_D5C06A65527038CC0A490D4D@AdobeOrg': '1585540135|MCIDTS|19409|MCMID|33561830398888401901318217502581917265|MCAAMLH-1677456331|6|MCAAMB-1677456331|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1676858731s|NONE|MCAID|NONE|vVersion|4.4.0',
        's_eVar8': 'unknown',
        'c_m': 'undefinedType-InType-In',
        's_e69': 'Type-In',
        'v71': '[["Type-In", "1676851531785"]]',
        'v72': '[["0", "1676851531785"]]',
        's_evar48': 'Weekend',
        's_cc': 'true',
        '_gcl_au': '1.1.2049507585.1676851532',
        '_ga': 'GA1.2.1242567351.1676851532',
        '_gid': 'GA1.2.594539560.1676851532',
        '_fbp': 'fb.1.1676851532456.1098594798',
        '_li_dcdm_c': '.homeadvisor.com',
        '_lc2_fpi': '0f1834a81c24--01gsp27napn0cx3nc8vr3fbhq0',
        '_clck': 'cx01i2|1|f9a|0',
        's_e4': 'event4',
        'reese84': '3:xBCyvDosVMX55WxQrLGa5Q==:7GnkOQpxhL5EyiG84h5BdwCuC3dnD5WVjCVThrwNMqt+bCYEN97lB1jasnC8k3wHM3TqrsBG78RUSwBqMyYVBGdyP9iC3xrv1n6aQKZqbjwx4EL1oWans87HGZt3yNLxp4Zw14B85ISP9LIFtDLHZ1EFxPNHVxH1ubXuhkL5cv/CbTgAQzOUwDn476ndz4a2qb50+m9I/jWPa8z4Gbe9r9MDyfIWHUs1ZqYqUp4BQzilZTXeRXSnTcT6W7MzhFA/Z3EUszCiK+yvKwLEKgKQg5D+k2LfIARmYC+jDiweE/U63I'
    }
    headers_porch = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    us_info_cookies = {
        
    }
    headers_us_info = {
        'HttpOnly': '',
        'ASP.NET_SessionId': 'ytbdbrzad4xh4f00kvdcaxi3',
        'GloutonCookie': 'Ng0wO3q/N6rixX+xyKD1XtcKbWTOef3REo4stqtVZUkYIG1rO6fePtcI6Ct27fP5QWkzRGy8aVRPxrUwnvQ1ZNRvRpj8iP3eeaEocAr0sTbXEjbUCiLEZZAedlsS9q9eJmJctTxHLLnlA2SWRaxkslgZjrGT0iLG6w6I8mYuTweMyxcGIG5RYS6BIYWeWNDmh5OsLXTpFZkVWOEgdhQpzSUgiD9l2cTkB2jMaSZZpSiMlW8qU4yBZA/tD6pqdprAZ0Ncxe4MTFVRbA++5PQ5Y6b9prZB3IQK0ul7wv9s+rpbUbc6TpCI+vBHDSOEWB8uT7+eNDTT7N0yXJFojtajdA==',
        'SERVERID': 'WEB52',
        '__atuvc': '21|8',
        '__atuvs': '63f8fa3238263cce000',
        '__gads': 'ID=0a7d58653cd7c618-22d684e620dc00e1:T=1677088411:S=ALNI_MaNu6LVIapKxIuIjUkvmqfITu2eRQ',
        '__gpi': 'UID=00000bddfa2d44d9:T=1677088411:RT=1677261101:S=ALNI_MaF7N4B-f1pEcR2XZAlqCQwmYXPiQ',
        '_ga': 'GA1.2.957291552.1677088414',
        '_gid': 'GA1.2.471441298.1677261100',
        '_gcl_au': '1.1.467099721.1677088414',
        '__gsas': 'ID=817707288380d9b1:T=1677088461:S=ALNI_MbG7LXaLfs8JFaxmy7eSqZr4IzJcg',
        'hubspotutk': 'efc4d35511a385f3136da2c36fe47c30',
        '__hssc': '209030989.17.1677261100402',
        '__hssrc': '1',
        '__hstc': '209030989.efc4d35511a385f3136da2c36fe47c30.1677088414926.1677088414926.1677261100402.2',
        '__hs_opt_out': 'no',
        '__hs_initial_opt_in': 'true',
        'sel_lang': 'fr',
        'sel_sort_order': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
    }
    headers_superpages = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    headers_dexknows = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    headers_tupalo = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    def start_requests(self):

        cities = ['Aberdeen', 'Belle_Fourche', 'Box_Elder', 'Brandon', 'Brookings']
        for city in cities:
                # url_home_advisor = 'https://www.homeadvisor.com/c.Electrical.'+city+'.SD.-12026.html'
                # url_porch = "https://porch.com/"+city.replace('_','-').lower()+"-"+"sd/electricians/cp"
                url_us_info = "http://us-info.com/fr/usa/business/160500/energie_extraction_electricite/"+city.replace('_','-').lower()+"-"+"sd"
                # url_superpages = "https://www.superpages.com/"+city.replace('_','-')+"-"+"SD/electricians"
                # url_dexknows = "https://www.dexknows.com/"+city.replace('_','-')+"-"+"sd/electricians"
                # url_tupalo = "http://www.tupalo.co/"+city.replace('_','-')+"-"+"South Dakota/c/electricians"
                # yield scrapy.Request(url=url_home_advisor, callback=self.parse_listings_home_advisor_page, headers=self.headers_home_advisor)
                # yield scrapy.Request(url=url_porch, callback=self.parse_listings_porch_page, headers=self.headers_porch)
                yield scrapy.Request(url=url_us_info, cookies=self.us_info_cookies, callback=self.parse_listings_us_info_page, headers=self.headers_us_info,  meta={'proxy': 'http://YF7YE0ZDWRP8SHXOQFMSCGJQDMQ2NMKC0GBYCXTNZD8W8MIYVRR5LRP3SA9UCBMG6Z6XNUGVNX1LIJV2:render_js=TRUE@proxy.scrapingbee.com:8886'})
                # yield scrapy.Request(url=url_superpages, callback=self.parse_listings_superpages_page, headers=self.headers_superpages)
                # yield scrapy.Request(url=url_dexknows, callback=self.parse_listings_dexknows_page, headers=self.headers_dexknows)
                # yield scrapy.Request(url=url_tupalo, callback=self.parse_listings_tupalo_page, headers=self.headers_tupalo)

    def parse_listings_home_advisor_page(self, response):
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_home_advisor, callback=self.parse_dealer_home_advisor_page, meta={'dealer_name': name})

    def parse_dealer_home_advisor_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj

    def parse_listings_porch_page(self, response):
        dealers = response.xpath('//*[@id="app"]/div[1]/main/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[1]/h3/a')
        for dealer in dealers:
            name = dealer.xpath('text()').extract()
            dealer_link = dealer.xpath('@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_porch, callback=self.parse_dealer_porch_page, meta={'dealer_name': name})

    def parse_dealer_porch_page(self, response):
        pattern = r'("telephone"+):"(.*?)(?<!\\)"'
        data = response.xpath('//*[@id="app"]/div[2]/div').extract()[1]
        phone = re.search(pattern, data)
        print (phone.group(2))
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
                'phone' : phone.group(2)
        }
        site = response.xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/a/@href').extract_first()
        if not site:
            yield dealer_obj

    def parse_listings_superpages_page(self, response):
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_superpages, callback=self.parse_dealer_superpages_page, meta={'dealer_name': name})

    def parse_dealer_superpages_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj

    def parse_listings_us_info_page(self, response):
        dealers = response.css('.customer-box.regular-customer')
        # dealer_obj = {
        #     'body' : response.body
        # }
        # yield dealer_obj
        for dealer in dealers:
            name = dealer.xpath('div[1]/div[1]/div[1]/h2/a/text()').extract()
            dealer_link = dealer.xpath('div[1]/div[1]/div[1]/h2/a/@href').extract_first()
            print (name)
            print (dealer_link)
            yield dealer_obj
            # yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_us_info, callback=self.parse_dealer_us_info_page, meta={'dealer_name': name})

    def parse_dealer_us_info_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj
    def parse_listings_tupalo_page(self, response):
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_tupalo, callback=self.parse_dealer_tupalo_page, meta={'dealer_name': name})

    def parse_dealer_tupalo_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj
    def parse_listings_dexknows_page(self, response):
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_dexknows, callback=self.parse_dealer_dexknows_page, meta={'dealer_name': name})

    def parse_dealer_dexknows_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj