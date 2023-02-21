import scrapy
from scrapy.http import headers

class CarDealersSpider (scrapy.Spider):
    name = "car_dealers"
    headers = {
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
    def start_requests(self):
        #OHIO CITIES 30 most populated
        cities = ['Aberdeen', 'Belle_Fourche', 'Box_Elder', 'Brandon', 'Brookings', 'Canton', 'Clark', 'Dell_Rapids', 'Eagle_Butte', 'Ellsworth_AFB', 'Flandreau', 'Fort_Pierre', 'Gregory', 'Harrisburg', 'Hot_Springs', 'Huron', 'Lead', 'Lennox', 'Madison', 'Milbank', 'Mitchell', 'Mobridge', 'North_Sioux_City', 'Parker', 'Pierre', 'Pine_Ridge', 'Platte', 'Rapid_City', 'Redfield', 'Sioux_Falls', 'Sisseton', 'Spearfish', 'Springfield', 'Sturgis', 'Tea', 'Tyndall', 'Vermillion', 'Volga', 'Wagner', 'Watertown', 'Webster', 'Winner', 'Yankton']
        for city in cities:
                url = 'https://www.homeadvisor.com/c.Electrical.'+city+'.SD.-12026.html'
                yield scrapy.Request(url=url, callback=self.parse_listings_page, headers=self.headers)

    def parse_listings_page(self, response):
        # get each individual dealer section
        # //*[@id="service-pros"]/section/div/ul/div/div/div[2]/div[3]/h5/a
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            #extracting the name for every dealer
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            # extract the stars            
            # list comprehension

            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers, callback=self.parse_dealer_page, meta={'dealer_name': name})

    def parse_dealer_page(self, response):
        # verify the phone number
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
        }
        site = response.xpath('//*[@id="details"]/div/div[1]/div/div/div[1]/a/text()').extract_first()
        if not site:
            yield dealer_obj
            # getting the url of the specific page of the dealer
        # next = response.xpath('//*[@id="service-pros"]/div/div[2]/nav/a[@aria-disabled="false" and @title="next page"]')

        # print ("eqwfqef\n")
        # print (next.get())

        # if (next) :
        #     nexturl = response.xpath('//*[@id="service-pros"]/div/div[2]/nav/a[2]')
        # #     # pass the url to new request
        #     yield scrapy.Request(url=nexturl, callback=self.parse_listings_page, headers=headers)
        # else :
        #     return


        