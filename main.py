# sourcery skip: avoid-builtin-shadow
from __future__ import print_function
import requests
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

from datetime import date
from dateutil.relativedelta import relativedelta
import time
from bs4 import BeautifulSoup

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

time_start = time.time()


SCOPES =  ['https://www.googleapis.com/auth/spreadsheets']


DOMAINS = 'https://lms.logika.asia/group?'



date_now = date.today() - relativedelta(days = (date.isoweekday(date.today())- 1))

date_start = date_now - relativedelta(years=1)
date_end = date_now + relativedelta(years=1)

s = requests.Session()

bases = ['NLB', "NVH", "PXL", "VCP"]

for base in bases: 
    para = f'GroupSearch%5Bid%5D=&GroupSearch%5Btitle%5D={base}&GroupSearch%5Bvenue%5D=&GroupSearch%5Bactive_student_count%5D=&GroupSearch%5BnextLessonTime%5D=&GroupSearch%5BnextLessonNumber%5D=&GroupSearch%5BnextLessonTitle%5D=&GroupSearch%5Bteacher%5D=&GroupSearch%5Bcurator%5D=&GroupSearch%5Btype%5D=&GroupSearch%5Btype%5D%5B%5D=regular&GroupSearch%5Btype%5D%5B%5D=intensive&GroupSearch%5BcourseContentType%5D=&GroupSearch%5BcourseContentType%5D%5B%5D=course&GroupSearch%5BcourseStartTime%5D={date_start}+-+{date_now}&GroupSearch%5BcourseEndTime%5D={date_now}+-+{date_end}&presetType=active&export=true&name=default&exportType=html'
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "_ga=GA1.2.1620969847.1664966279; _ym_uid=1664966280852805697; _ym_d=1664966280; intercom-device-id-ufjpx6k3=fd3080c1-5a63-4af6-bd1f-15268d549a7e; userId=30454; sidebar-state=collapsed; studentId=1700942; _grid_page_size_schedule=35d0980fa38e2255112d0c62698773cab8aa12a81c6735caf172064b5eb6ea47a%3A2%3A%7Bi%3A0%3Bs%3A24%3A%22_grid_page_size_schedule%22%3Bi%3A1%3Bs%3A3%3A%22200%22%3B%7D; createdTimestamp=1675163976; accessToken=10074a7a9ea56087dea1d0ec1edd8d558d2988fae737cfcc81475a6e87542fa0; SERVERID=b410; _gid=GA1.2.1365468960.1675670812; intercom-session-ufjpx6k3=bHpqKzNWMHp4UFNYQ1hteStxMGtHcWVMeUVXdDBpdjlWUWZJSHduWGlCMVF3VEZ0S04zMjIrdXRBNHlpN01rcy0takV3Q0NoQWplVHI4cXBnanBtWDlJdz09--083afe6f3749d5c2b76be8c9154ec111cfa6ee0e; _grid_page_size=d3ebbdf9ec9235bfc4ba59572a6d3dd403a563222be148e9c705e91612194e49a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_grid_page_size%22%3Bi%3A1%3Bs%3A3%3A%22200%22%3B%7D; studentAccessToken=a258b5b2184ee88cbc5e1907d74ba098a655dd8b86415c379d966b0e0dec958c; studentCreatedTimestamp=1675851346; _backendMainSessionId=99103086a9eef43eb77a7795a8fc84be; _csrf=01fa47280f8ed371c0c37badb32b45f2b22c716ff1fa7ea594eaa2a2e98f622ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22hrh1AP90gQZfMSuDV2T0EOwQ4-4gsR8b%22%3B%7D; _ym_isad=2",
        "Referer": f"{DOMAINS}GroupSearch%5Bid%5D=&GroupSearch%5Btitle%5D={base}&GroupSearch%5Bvenue%5D=&GroupSearch%5Bactive_student_count%5D=&GroupSearch%5BnextLessonTime%5D=&GroupSearch%5BnextLessonNumber%5D=&GroupSearch%5BnextLessonTitle%5D=&GroupSearch%5Bteacher%5D=&GroupSearch%5Bcurator%5D=&GroupSearch%5Btype%5D=&GroupSearch%5Btype%5D%5B%5D=regular&GroupSearch%5Btype%5D%5B%5D=intensive&GroupSearch%5BcourseContentType%5D=&GroupSearch%5BcourseContentType%5D%5B%5D=course&GroupSearch%5BcourseStartTime%5D={date_start}%20-%20{date_now}&GroupSearch%5BcourseEndTime%5D={date_now}%20-%20{date_end}&presetType=active",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }



    end_point = DOMAINS + para
    res = s.get(end_point, headers = header)
    output = res.content.decode('utf-8')

    soup = BeautifulSoup(output, 'html.parser', from_encoding='utf-8')
    soup.find('tbody')

    table_rows = soup.find_all('tr')
    groups = []


    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    except FileNotFoundError:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    # table_rows.remove(table_rows[0])
    for tr in table_rows:
        lessons = []
        group = []
        all_td = tr.find_all('td')
        group_id = all_td[0].string
        all_li = all_td[1].find('p')      
        next_lesson_index = all_td[5].string
        next_lesson_name = all_td[6].find('div')

        


        if not group_id:
            continue
        
        all_li = str(all_li)
        url = all_li[all_li.find("https"):all_li.find("</p>")]
        start = url.find("d/")
        end = url.find("/edit")
        id = url[start+2:end]
        try:
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=id, range='Report!AC3:AC34').execute()
            values = result.get('values', [])
            for j in values:
                lessons.append(j[0]) 
                
            if len(lessons) == 0:
                result = sheet.values().get(spreadsheetId=id, range='Report!AE3:AE34').execute()
                values = result.get('values', [])
                
                for j in values:
                    lessons.append(j[0])
                  
  
        except HttpError as err:
            continue

               
        group = [all_td[0].string, str(all_td[1].find('a'))[str(all_td[1].find('a')).find('>')+1:str(all_td[1].find('a')).find('</a>')], url, all_td[2].string, (all_td[3].string)[0], str(all_td[4].string).replace("\xa0", ' '),all_td[5].string, str(next_lesson_name)[str(next_lesson_name).find('>')+1:str(next_lesson_name).find('</div>')], all_td[11].string, all_td[12].string]
        group.extend(lessons)
        groups.append(group)
    print(f"{base} Done")
    resource = {
        "majorDimension": "ROWS",
        "values": group
    }

    # 1D8uRbAJXBJMcF0e8tXWKe5dRbiv-EW_by-SpNAxZ3qA for testing
    # 1NkJo_leApQ2-KVGIxca3MbtxfJv7kS7Ke17Cp6fAl0M for real data update
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result1 = sheet.values().update(
        spreadsheetId= "1D8uRbAJXBJMcF0e8tXWKe5dRbiv-EW_by-SpNAxZ3qA",
        range= f"'{base}'!A2",
        valueInputOption="RAW",
        body=resource).execute()
        
time_end = time.time()
print(time_end - time_start)