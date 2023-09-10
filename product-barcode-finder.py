""" import http.client

conn = http.client.HTTPSConnection("www.trendyol.com")

headers = {
    'cookie': "userid=undefined; COOKIE_TY.IsUserAgentMobileOrTablet=false; hvtb=1; VisitCount=1; SearchMode=1; platform=web; WebAbTesting=A_65-B_52-C_92-D_26-E_6-F_100-G_99-H_71-I_78-J_58-K_27-L_53-M_14-N_53-O_44-P_63-Q_84-R_14-S_10-T_9-U_11-V_8-W_18-X_64-Y_35-Z_49; __cf_bm=CFT0ZBJmtuW5UVlkTqU4SERh.9hV4L2OJuHe3s.kaQg-1693777266-0-AQ2BLD%2FFgxB4bnelWTKapABgJnywu65gVy7TJrXBStQ7JbwGK7jKiOdRReZuEcSB6PWmiMZ7KbMvl0K0fSPgtoY%3D; __cflb=0H28vSBxxmVRpbspxXnjRKkmcsVEkGWk8JyBxnnXBAt; __cfruid=a8005bd07fe9c765da05dfa608b59b769ef275c1-1693777266; _cfuvid=F437HmYNH0K7U5LWhq.QcR.9gUQ_7oaChgMTenvjiL0-1693777266174-0-604800000; userid=undefined; ForceUpdateSearchAbDecider=True; WebAbDecider=ABSuggestion_A-ABRelevancy_1-ABFilterRelevancy_1-ABListingScoringAlgorithmId_1-ABSmartlisting_70-ABSuggestionBadges_B-ABProductGroupTopPerformer_B-ABOpenFilterToggle_2-ABBadgeBoost_A-ABRF_1-ABPastSearches_B-ABSuggestionPopularCTR_B; OptanonAlertBoxClosed=2023-09-03T21%3A41%3A23.530Z; OptanonConsent=isGpcEnabled%3D0%26datestamp%3DMon%2BSep%2B04%2B2023%2B00%253A41%253A23%2BGMT%252B0300%2B(GMT%252B03%253A00)%26version%3D6.30.0%26isIABGlobal%3Dfalse%26hosts%3D%26genVendors%3DV77%253A0%252CV67%253A0%252CV79%253A0%252CV71%253A0%252CV69%253A0%252CV7%253A0%252CV5%253A0%252CV9%253A0%252CV1%253A0%252CV70%253A0%252CV3%253A0%252CV68%253A0%252CV78%253A0%252CV17%253A0%252CV76%253A0%252CV80%253A0%252CV16%253A0%252CV72%253A0%252CV10%253A0%252CV40%253A0%252C%26consentId%3D9f61e5ec-79b1-4865-a2ae-22c868f85528%26interactionCount%3D2%26landingPath%3DNotLandingPage%26groups%3DC0002%253A1%252CC0004%253A1%252CC0003%253A1%252CC0001%253A1%252CC0007%253A1%252CC0009%253A1%26AwaitingReconsent%3Dfalse; initialTrafficSource=utmccn%3D(not%20set); __utmzzses=1; _gcl_au=1.1.173820954.1693777284; pid=65qVXGJYHO; sid=bEw1Q3cT72; _ga_8F2NHTRF7T=GS1.1.1693777284.1.0.1693777284.60.0.0; _ga=GA1.2.814965150.1693777284; _gid=GA1.2.1166031793.1693777284; _dc_gtm_UA-13174585-1=1; _fbp=fb.1.1693777284513.1043007418; _tt_enable_cookie=1; _ttp=8Wdxk-kJhL5jBG_UrHQL3-cQdNt; cto_bundle=MEjAI18lMkJORGJyT21LdG1BY0cwQXRBbE5PQU1VMSUyQm5Id2VDQ0hyb01RWFgwQ1h5dWxTUk9NUHJwazRpTndDRFRYTUE0c3BQdTBpclJsM1ZBNnU5YWpNUTFQR1RKMyUyQllvY2xXREZhMVRQY2kzVzMyWGx2bXdrZWt1cmZrSDdablhKNVRHMA; _ym_uid=1693777286872914276; _ym_d=1693777286; _ym_isad=2",
    'authority': "www.trendyol.com",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'accept-language': "tr",
    'sec-ch-ua': "'Chromium';v='116', 'Not)A;Brand';v='24', 'Google Chrome';v='116'",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "'Windows'",
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "none",
    'sec-fetch-user': "?1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

conn.request("GET", "/rise-and-shine/antiperspirant-whitening-roll-on-75-ml-p-316160450", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")) """

import requests

url = 'https://www.trendyol.com/rise-and-shine/antiperspirant-whitening-roll-on-75-ml-p-316160450'


req = requests.get(url, 'html.parser')

barcode = req.text.split('barcode":"')
barcode_real = barcode[1].split('"')
print(barcode_real[0])
