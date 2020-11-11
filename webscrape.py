import sys
import io
import codecs
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import os

reload(sys)
sys.setdefaultencoding('utf-8')

current_time = datetime.datetime.now()

#job posting block
URL = 'https://ca.indeed.com/jobs?q=Software+engineer&l=Vancouver%2C+BC'
page = requests.get(URL)

#stock block
AAPLstockURL = 'https://ca.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
AAPLstockpage = requests.get(AAPLstockURL)

AMDstockURL = 'https://ca.finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch'
AMDstockpage = requests.get(AMDstockURL)

GEstockURL = 'https://ca.finance.yahoo.com/quote/GE?p=GE&.tsrc=fin-srch'
GEstockpage = requests.get(GEstockURL)
output_file = open("My_Daily_feed.txt", "w")
#stock functions
output_file.write("Hi Josh," + "\n")
output_file.write("Today is " + current_time.strftime("%a %Y-%m-%d %H:%M") + "\n")
output_file.write("---Start of Stock report Session--------------------" + "\n")
AAPLsoup =BeautifulSoup(AAPLstockpage.content, 'html.parser', from_encoding = "utf-8")
AAPLresult = AAPLsoup.find('div', class_='D(ib) Mend(20px)')
AAPL_current = AAPLresult.find('span', class_= 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
#AAPL_change = AAPLresult.find('span', class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)')
output_file.write("The current APPLE stock price is " + AAPL_current.text.strip() +"\n" + "\n")

AMDsoup = BeautifulSoup(AMDstockpage.content, 'html.parser', from_encoding = "utf-8")
AMDresult = AMDsoup.find('div', class_='D(ib) Mend(20px)')
AMD_current = AMDresult.find('span', class_= 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
#AMD_change = AMDresult.find('span', class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)')
output_file.write("The current AMD stock price is " + AMD_current.text.strip() +"\n" + "\n")

GEsoup = BeautifulSoup(GEstockpage.content, 'html.parser', from_encoding = "utf-8")
GEresult = GEsoup.find('div', class_='D(ib) Mend(20px)')
GE_current = GEresult.find('span', class_= 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
#GE_change = GEresult.find('span', class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)')
output_file.write("The current GE stock price is " + GE_current.text.strip() + "\n" + "\n")

output_file.write("-----End of Stock report Session--------------------\n" + "\n")

#job posting functions
soup = BeautifulSoup(page.content, 'html.parser', from_encoding= "utf-8")
results = soup.find(id ='resultsCol')

job_elems = results.find_all('div', class_= 'jobsearch-SerpJobCard unifiedRow row result')
output_file.write("-----Start of Job posting Session--------------------\n" + "\n")
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_= 'title')
    company_elem = job_elem.find('div', class_= 'sjcl')
    summary_elem = job_elem.find('div', class_= 'summary')
    if None in (title_elem, company_elem, summary_elem):
        continue
    title_elem.text.encode('ascii', 'ignore')
    #print(title_elem.text.strip())
    company_elem.text.encode('ascii', 'ignore')
    #print(company_elem.text.replace('\n',''))
    summary_elem.text.encode('ascii', 'ignore')
    #print(summary_elem.text.strip())
    output_file.write(title_elem.text.strip() + "\n")
    output_file.write(company_elem.text.replace('\n','') + "\n")
    output_file.write(summary_elem.text.strip()  + "\n" +"\n")
    output_file.write("<==========End of one job==========>" + "\n")

    #print('\n<=====End of one job=====>')

#output to text file
output_file.close()