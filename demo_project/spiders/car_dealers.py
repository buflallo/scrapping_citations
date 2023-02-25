import scrapy
from scrapy.http import headers
import re

class CarDealersSpider (scrapy.Spider):
    name = "car_dealers"
    headers_home_advisor = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'JSESSIONID': 'E180B9E0455F462109507F0895EC5A0B',
        'cookiesEnabled': '1',
        'aff_track': '2|*|23116563|*|0',
        'originatingSessionID': '1677283504560site-6cd99748b6-m5mcpE180B9E0455F462109507F0895EC5A0B',
        'csacn': '746971',
        'csdcn': '1677283504560',
        'psacn': '""',
        'psdcn': '0',
        'sess_log': '1677283504560site-6cd99748b6-m5mcpE180B9E0455F462109507F0895EC5A0B',
        '__cflb': '0H28vcAZaTP4ptpqrB3WECLQyMNamMKsSEwrACN943D',
        '__cf_bm': 'M5GtwrT_kCbIH5m1jooHbVds6rZZNbwZHKt75bkHWWg-1677283504-0-AXQQkW7Iued5qz2hwaxcauEf/K21qRq9IlLjGFpH29fctYRftif1mdD50IWtz1b/dA9YUMYBn35+ywDKqNxur2E=',
        'AMCVS_D5C06A65527038CC0A490D4D@AdobeOrg': '1',
        's_ecid': 'MCMID|28948151415078795890386169278950781922',
        's_eVar8': 'unknown',
        'fpv': '1',
        'c_m': 'undefinedType-InType-In',
        's_e69': 'Type-In',
        'v71': '[["Type-In", "1677283509930"]]',
        'v72': '[["0", "1677283509931"]]',
        's_evar46': '5%3A00PM',
        's_evar48': 'Weekday',
        's_dslv2': '1677283509933',
        's_dslv2_s': 'First%20Visit',
        's_gnr': '1677283509934-New',
        's_gnr2': 'New',
        's_vnum': '1677625200936&vn=1',
        's_invisit': 'true',
        's_visNum': '1',
        'v11': '52.30.117.125',
        's_cc': 'true',
        'AMCV_D5C06A65527038CC0A490D4D@AdobeOrg': '1585540135|MCIDTS|19414|MCMID|28948151415078795890386169278950781922|MCAAMLH-1677888307|6|MCAAMB-1677888307|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1677290709s|NONE|MCSYNCSOP|411-19421|MCAID|'
    }
    headers_porch = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    headers_superpages = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    headers_tupalo = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    def start_requests(self):

        cities = ['Aberdeen', 'Brookings']
        for city in cities:
                url_home_advisor = 'https://www.homeadvisor.com/c.Electrical.'+city+'.SD.-12026.html'
                # url_porch = "https://porch.com/"+city.replace('_','-').lower()+"-"+"sd/electricians/cp"
                # url_superpages = "https://www.superpages.com/"+city.replace('_','-').lower()+"-"+"sd/electricians"
                # url_tupalo = "http://www.tupalo.co/"+city.replace('_','-').lower()+"-"+"south-dakota/c/electricians"
                yield scrapy.Request(url=url_home_advisor, callback=self.parse_listings_home_advisor_page, headers=self.headers_home_advisor)
                # yield scrapy.Request(url=url_porch, callback=self.parse_listings_porch_page, headers=self.headers_porch)
                # yield scrapy.Request(url=url_superpages, callback=self.parse_listings_superpages_page, headers=self.headers_superpages)
                # yield scrapy.Request(url=url_tupalo, callback=self.parse_listings_tupalo_page, headers=self.headers_tupalo)

    def parse_listings_home_advisor_page(self, response):
        dealers = response.xpath('//*[@id="service-pros"]/section/div/ul/div')
        for dealer in dealers:
            name = dealer.xpath('div/div[2]/div[3]/h5/a/text()').extract()
            #print sound bp bp bp
            print ('\a\a\a')
            dealer_link = "https://www.homeadvisor.com" + dealer.xpath('div/div[2]/div[3]/h5/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_home_advisor, callback=self.parse_dealer_home_advisor_page, meta={'dealer_name': name})

    def parse_dealer_home_advisor_page(self, response):
        # verify the phone number
        pattern = r'("telephone"+):"(.*?)(?<!\\)"'
        dataa = response.xpath('/html/head/script').extract()
        datab = ''.join(dataa)
        # return
        if not datab:
            print("no data tfoo")
            pass

        phone = re.search(pattern, datab)
        print(phone.group(2))
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
                'phone' : phone.group(2),
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
        dealers = response.xpath("//*[@id[starts-with(., 'lid')]]/div/div/div[2]")
        for dealer in dealers:
            name = dealer.xpath('div[1]/h2/a/span/text()').extract()
            phone = dealer.xpath("div[2]/div[1]/a[1]/span[1]/text()").extract()
            website = dealer.xpath("div[2]/div[1]/a[2]/@href").extract_first()
            if not website:
                dealer_obj = {
                        'business name' : name,
                        'phone' : phone
                }
                yield dealer_obj
        if (response.css('.next.ajax-page ::attr(href)').extract_first() is not None):
            yield scrapy.Request(response.urljoin("https://www.superpages.com" + response.css('.next.ajax-page ::attr(href)').extract_first()), headers=self.headers_superpages, callback=self.parse_listings_superpages_page)

    def parse_listings_tupalo_page(self, response):
        dealers = response.xpath('//*[@id="spot_url"]')
        for dealer in dealers:
            name = dealer.xpath('div/h2/span[2]/text()').extract()
            dealer_link = dealer.xpath('@href').extract_first()
            yield scrapy.Request(response.urljoin(dealer_link), headers=self.headers_tupalo, callback=self.parse_dealer_tupalo_page, meta={'dealer_name': name})

    def parse_dealer_tupalo_page(self, response):
        # verify the phone number
        site = response.xpath('/html/body/div/div/section/div[2]/div[2]/dl/div/dd/a/@href').extract_first()
        phone = response.xpath('/html/body/div/div/section/div[2]/div[2]/dl/dd/span/text()').extract_first()
        dealer_obj = {
                'business name' : response.meta['dealer_name'],
                'phone' : phone,
        }
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