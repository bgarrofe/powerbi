import requests
import json

url = 'https://token.docs.microsoft.com/accesstokens'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': """MUID=2A9BED9AFF63681A00A7E684FB636BDC; optimizelyEndUserId=oeu1509019196345r0.5445929089534514; msdn=L=en-ca; _ga=GA1.2.1659562823.1508355403; _mkto_trk=id:157-GQE-382&token:_mch-microsoft.com-1509019196644-42647; ClicktaleReplayLink=https://dmz01.app.clicktale.com/Player.aspx?PID=1011&UID=2348084990575225&SID=2348084990575225; MC1=GUID=c26315c6204a4a78bf38455d4ed96e2e&HASH=c263&LV=201910&V=4&LU=1571321740856; AAMC_mscom_0=REGION%7C4; MSCC=1583340966; LPVID=E0OGE0ZTEzN2Y1NzU2ZTll; _fbp=fb.1.1583843532310.622219524; utag_main=v_id:015f588d9cd50014f4eb2aced1f504073002406b0086e$_sn:13$_ss:1$_st:1589373920784$ses_id:1589372120784%3Bexp-session$_pn:1%3Bexp-session; at_check=true; WT_FPC=id=23fdc833be8124175b91532093425681:lv=1593014447144:ss=1593014447144; __CT_Data=gpv=16&ckp=tld&dm=microsoft.com&apv_1068_www32=16&cpv_1068_www32=16&cpv_1022_www32=1; ctm={'pgv':3723481301997802|'vst':3173433345449671|'vstr':3124692510746092|'intr':1593107255515|'v':1|'lvst':39}; AMCVS_EA76ADE95776D2EC7F000101%40AdobeOrg=1; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=-1303530583%7CMCMID%7C72518858335260279934094859937743347443%7CMCAAMLH-1593786238%7C4%7CMCAAMB-1593786238%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1593188638s%7CNONE%7CMCAID%7CNONE%7CMCIDTS%7C18440%7CvVersion%7C3.3.0%7CMCCIDH%7C-1817596892; aam_uuid=72079773191542087264068971451240708092; AADNonce=828f0685-81a0-4746-8c81-4c28a840d65e.637287787109062279; AADAuth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlNzWnNCTmhaY0YzUTlTNHRycFFCVEJ5TlJSSSIsImtpZCI6IlNzWnNCTmhaY0YzUTlTNHRycFFCVEJ5TlJSSSJ9.eyJhdWQiOiI0YjIzMzY4OC0wMzFjLTQwNGItOWE4MC1hNGYzZjIzNTFmOTAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83ODkzNTcxYi02YzJjLTRjZWYtYjRkYS03ZDRiMjY2YTA2MjYvIiwiaWF0IjoxNTkzMTgxNjE0LCJuYmYiOjE1OTMxODE2MTQsImV4cCI6MTU5MzE4NTUxNCwiYWlvIjoiRTJCZ1lIanZjS3ZRSjBCRjJ0UG1sT0VQbHdtdnFtcStSMlMyYlhTNytrNytpZjJsOEJVQSIsImFtciI6WyJ3aWEiXSwiY19oYXNoIjoiTTBnX1ktX3BBU3duS1ViWVR1VFFBQSIsImZhbWlseV9uYW1lIjoiR0FSUk9GRSBTQU1QQUlPIiwiZ2l2ZW5fbmFtZSI6IkJSVU5PIiwiaXBhZGRyIjoiMTQyLjQwLjE3Ni42OSIsIm5hbWUiOiJCcnVubyBHYXJyb2ZlIiwibm9uY2UiOiI4MjhmMDY4NS04MWEwLTQ3NDYtOGM4MS00YzI4YTg0MGQ2NWUuNjM3Mjg3Nzg3MTA5MDYyMjc5Iiwib2lkIjoiODRhZGM5NDMtNTQ4NC00MmM3LWFiYTItMzNmMTllNGNhNDA0Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTExNjE5NzU4OTgtMzAyMzYxOTIyNC04OTAxMzc0OTgtMjA1MDU4IiwicHVpZCI6IjEwMDMzRkZGODg0MDFDNTgiLCJzdWIiOiJxTmJBTFkwN3pJQld1LXpvbTZFYXkyU1h2eUQtV3huU3hnN1dkNFFDS0FBIiwidGlkIjoiNzg5MzU3MWItNmMyYy00Y2VmLWI0ZGEtN2Q0YjI2NmEwNjI2IiwidW5pcXVlX25hbWUiOiJicnVuby5nYXJyb2ZlQHZhbGUuY29tIiwidXBuIjoiYnJ1bm8uZ2Fycm9mZUB2YWxlLmNvbSIsInV0aSI6ImVKQzJHc0xTcUVtczJxYnBFZFZKQVEiLCJ2ZXIiOiIxLjAiLCJ4bXNfbXBjaSI6MjU5MjAwLCJ4bXNfcGNpIjozNjAwfQ.WyCHvBpgNS_dOQrUF9CyrcHOMN54qwQ5SKKaB7LcVzzFXfLnkGk3f2Ttq3vHoiESwY4Uw3kYSccqHQQP8ggGqH0nUQyVxnbkrdV-jSn0urN47wW8zaIi087jsoqsNwA6jmCIIiJAQCjMQMkfzyVSqgRj1VdbrcP4aaK5Fzc-Vw4AXjJR3Ap3OEYC7PNNUd55ur-CEWxDnsAQ8qvzjMpHetQdYOE_9q4N-00ladnvzMQS34taxqHNfUHiALbc_1PqGA68bVLbpNxWDKNAGDmkWaqHq3kI5mta_jnChOBUQmmoNmXXcOmBP-No2SFv8bAzDA3FXlZJebFY4Qjg4JNJNA; AADAuthCode=AQABAAIAAAAGV_bv21oQQ4ROqh0_1-tAgLu1upwl1Jyh1Fog3yG8OroVG3Ya-ZQtW2TECqxXVqUCiyEFbZ1vOG1-z8LISC5UXzqVXu5Q7dDz9Q5We_PH5xGENSRXX0EbQKOxqwNcF80BMerqP98in-71OBXeGbBk7SutPWS50sBdcsURbJNYE6129tmIm0MEh8TZa0_TV8rEr_hTgmAbpr1vDuTLF5FkCewIrsLTD86fdhyy-d6a93aCy41zWL1UiKjYrMbz_sodq-QSrP3AJ6nzPYCbmGic5nHjOlYMXOsRR_prL2JuEg7CwpGxNpKLFaclhsX5D9IH-fyuCy-rv3hw8-FgxfNlDQ8cGDIviYtQc_oG3Sy3E5SwkhodCZ4KcBdW-JFJ4w5xy7FfpczYTbgpw7QqSd9X5v1U9Rd3H_9LjeLkIg6Y_Z8nx-r-ZLF8sEfswCudFr2d4qQEr7m_pL3XtLTxycPCwBBZheXCv_FGbHJ1ql6GwXlZ_dj9rex2lFHOpxAGqeHZzPfyu6YwVMqIg3-loiEWoC0Lu5qCRR8-8b9TJDNHf2NiiL4SWNCcCg86ew6V43o1n7SteClnaE4N0lf-PIal26KlogDpXoyYAsXc7nYF3sBCny3p2lQccLwmYgEiLAj5qces7v6a_Locjq-JYN5KBxz9kmOU042zKA_r1QQxTPU85h4bVS6U_tlfn2dpiBmTyGVIOGU5dNSXZYvKnX0s-dwrSJi6_dCqpHHr8Tz5DX_9X7ge1HK4QDvWKA5PEJif2tHFYXLeEVoVm_fsphkkIAA; AADSID=596420d1-d1f5-4fb9-ba46-97752724e077; AADState=1; _gid=GA1.2.1942633577.1593623299; .TokenAuthCookies=CfDJ8JvUilcOiwxHiY_bjlNe_J8wAPXTUr5iyYZ0h_jTbrXqEZKvSGxSr5HIEeLzUSXAACtTQGLZdhS3aA4Gpm937YgN_T2ILDfbz4IeU3WpZSt89oj3oqOXlPuQIOvo4wLmtDTR9P8Ps_rENUHEAIT__FYmF4e3m9mUWoTKuGopx7L6Xa-QfJXHI0w4GZ8oeiEvVv0AZuR0VKzA5MCq1OaM_BhbX9On2njf9V5muz09WGpsXv9g-lcleVb3lzRTJlewyofyqnidzKfuoby9ZV91tAGobkykVs4aJxuI_c6fOVNw9kNR69zvgkcvMfitaBd3I7xeIgDWU_7EsrCzrw_uQoYm2p7FiCRRlZw7E7AlYIIZN5Vyr8-KYircqMmPLGR4i6c5hgusAA7Y97Y4X2Y7y-OVvtlzY6gdY1YU9LljyWC-GwtEXyxVgGuxHZnSJEZHUO0cwOGAd4tXrvlfISmF_0wi418LzHyVfXW00IixMmBAX4kJ_U4kYGz_qKmaQetoYxvNWNK5g_PHNPKViZPab6u-AYqQ2Kw259P6pz1Ix4ZV4tezDGSvEP0wYZt4-xCeLExuAtaJhy06kWk4aNbJ6W1paqbMBob6ekK9OBUh4kRJivkjZiF0g3V051iEtJ0Abr-7VjpDKwYCSfpru0rrNphCVAdaBw5BR3SQSIZgUoMwqLMcdSBsQwmG56uXHWBwPFuSOC5KorbT0K7b9jGhDOT-tpJQ8triXKolHx93zqYzIirESFR0R43_amugUeAf6KLFfC6mJaaeKo3kbRgPsuH6NS27iiWc2XQ7uXNxUrhILdE-PyUlIF0Ji04t4A1pCqK_m9RDvkgyief5TdyYx1RADs7G_jGID1hQBMaOP9hM3NOQvusMhuUW3foY5tQrNZJtAETUELtjkbOvygQN4Nk0GHsB1oRyaASb8fDjgNaSJ7hO3Rz_R5Z8pltfcLoWIHAHD-a2nOxHkKUAbQuEXESjZNnS6dn7gFYr7CKClbjG1h5i2qccMonNk8JmzRp_J-Vv08SPYwC-kojwjdE1ryA4Om_MsGMtxI4mb94UDR1sbP2rg435yhp_TOIck_oOBkn2ZYK0jAYn89x5UPwErfRznC779bJ9EU24Q-oPQDJcsPO5-l9fZS4fS9nYc-tFJmv3S6m_TxuNczK91L3_crqnpj4bp2bwaBbcH8IzUD-dKqxunWpCGwOj96OHeAmYuhoynqjvxjVhHGAAJ8_FvOCppbEkGiF2FphgVd0-21RUox1Jn09dzfQwGFsnL_DN-koVhmbzcFrie4WYyHcxSDg89WoqAiKmeeof72Dc5h10Flq3t3m2saYe4_LoMrI92kL22VLXy8p9mCtjr4p9R_WPw2GFFXMROuxFnYgNnVIY_2WGcrO3QrlCPwLE7jDpYqJeAJeYuBCiMSHW3u1mMJKY572gqkZALvhY1dB0o36B_H6C5MoxXuGQv7Aa7Xx9954ZRF60HzReerXpgY6-_6tgXHILTxgEes12iHKz2ulyMEWqAk26rrnHDShDbtBiliLSGylXfpM9WbSprucsv4T6871jOLAvdr02l7fUb7cotSoQ62CqhPWDoAQTsufqbiHb5fgCb1DF-MfPfYwRG2e4_lHl230_j_Y0DSn7E1kqmhLRD_9WeIEzrtj-VEvXzv0qe_y7XpnmeNzeCpXLkNypzQtvmXwRg56u9qBPkyoJQmojV4yRrB8FkBszP6nmWnKmWDYB5ooA6a0L62b5uUMaHOUaI0PgrJL2Juwmfgsk91c6EF2Ev1as-9PHzQduhZ0BZTGoid3GUYIFQIAEkHKUJ2VVHHWNoGZobPy4iIQhvShPcNlUQu_FG36UffYWO4i_0oxfArSIuuWn8-WyqNisDV8rzBzftF5EM1VB8NhIw1Ml8chpVxWWHV3NiaC3JqKAXNMbyKEPfUMxl_G5VYsW4uwcDqu0auUeuEmEuDMUfQOS8Sg0RDTR9ojQtmsFViOqE8flWo23Q_IVGaE7micY6KVKb9U7fByeNIKzTyP0zhDWd-VUtj8uIVPBjwWGkGAH9AJlnqzEqgCAhNbfjy1CPJFCdlTe86oqCXsRb8K-nfuxKNpBk6jSGb1UxMkw4R7V5nNPpLwtneQ1eoAHCHcUVqTzyjVWEpRNs8jgB-_TuA86984rdSNxdW8Y3r8gzInQncKdeJul3v-vlWkwm9txNXGfZeUKBL4rIqrOzDAuSzgxlNYT-IevbLau1hA24EIRkVbixF2SI_b3MT-LuKX5Qg8ifueQkJ1_Qq-vcCh3iNRCGuI1lng5aCtWRJByz1wF5Q33lQyi4ul3cZrKUMtyIsHltU3FgM-boictA0hvi4l8nY1TogmJjdFGBXnpDoxM9TR4ba7uc0e_1gzlauRkQX1b0jAXSQojzoyVMtiuzc99RIlY9RsubnuSVFCGZ-SUWu_s3InfH75TnKGtt3pEsIB8Oq3Jvs2L_7G55zpHRZark_i2gFy_t_XJ4oF6Whpscqbh50OWsoUCQZjEubU5ZfOzSmo6Cr51xYUQgGQA4TEkgax9Sl6jWXI0_xiuLkQarI-vopRwlsiBOSI-60PkmefW1jSc0N0FsqYqWwmB5-iY7cQkPkLd-T71bTIKPnDGoCYLyuCflvJ74VOSxFc6jqk8zlKRz03zrG5o2xa9gbm7EHCEX4eQZ3v-Fj5loZRqwYN4JdHYcP7ZkLyyUEbEtyxvQAcRR9uU2Db4pya6xpeYEkUZ-5QBQdfG8CxCFhcJLba6Cbo44VCrJQBLjTYsBD9iEdguxTDK8-Zpadd-w-m6H170Daf6564MxUjXsleqyxlD63uRjv0EPLus7w-nqDJQFvKS3fx15PwaR88Gce7-syQWDXAuRbpZsYlKn90CyLHuDwPcbiJMhyyFzhtCJlnIJBQqbnOdh0h_4rXqF-pr0L33punpYnQC25xurGI-UNxoHsmJOfVhrnZZVI6nH23LA-0eJ64hPbdIlEYQGIP0XjRUxjGnvdUkvMr_14s4GyDBhh_boqmVX9HxchVHCtofQgrmcKFnKOkIZj6RuHLSt_hbKRrbsJenZ-XAKQjQFzvC7CwtpFXXRPyO4WopXYCVmR9QtQweHcyfnMpgdbh4G-EDfD1ekLzMNg0O6WWZIPf6r94aJ38WIV2ce13mLgVzMQzts3NXKXM69olifj5Ct73XybpP2eOOhs2ZrEpVNkN5iv0xSqn88CBah0KU9porb3T1zKLph-_VtrlL00vq7-pRQcAV4fNoqJTqPbJ-VyQ1ewaPXBf8MKa90ZvQ_q1jXmoT3Fzrba_LYmxFhN6iAGhXRCUMwEfHIgiFAngz4vcTcz1TcaD0DBYCReXI_ahmjoAVXW7fOiVEpQGUn8sV-z5KnKiFRKjx9gG2tubiLeOzvvLPI52_zX-vffrMuS6ECfhfVbbLMRvddQnl_8WBFoOfoYHVpkFcA9E9Qrc1gxsXUypZ21Ze7zXPlQhwL78OXyy-hZlDB9knFzOKM8y4J6mZyC3WYpAl59zyX1dp-KH_gqsKuXbRfo2vvNObXvn0logFjscxINbKdB5_Bg_0KQYrYP_jjlYbSGhfv3SsL4mhTdLoE-Wqt3jJhKyJoPjiNcFXNuQn75NS6tR3ox1GerYT68P2jdNjfz52eL_Fpm9fmCe0UThPlbk6tuOpW9SzLPDK9UXvjsRkyppnk-bYbhAFF6mUgQrYp625uyP90pOE9PahPLFyXXreuo0n3tUY5rLF5sCoy1IgsNzd9SoWU9-qxmRF_l3IiWF0JgBiNkylra1wD24meR6Rqdwu4lkjkbwy5uQxVdIZDevr; MS0=b8f3ad1d1151470282e922033384fe17; mboxEdgeCluster=34; __CT_Data=gpv=353&ckp=tld&dm=microsoft.com&apv_1068_www32=351&cpv_1068_www32=351&apv_1080_www32=2&cpv_1080_www32=2; ctm={'pgv':6185466940242346|'vst':7938142342768431|'vstr':3124692510746092|'intr':1593719378873|'v':1|'lvst':1769}; _gat=1; _uetsid=ac74ffd3-5be4-4cac-cc88-b3dd2db2dd37; mbox=PC#f00075fbeb694296a88cb20c9ce43c0d.34_0#1656964315|session#108d2795e79544b7bf530e0192084e59#1593720457""",
    'Host': 'token.docs.microsoft.com',
    'Origin': 'https://docs.microsoft.com',
    'Referer': 'https://docs.microsoft.com/pt-br/rest/api/power-bi/embedtoken/reports_generatetokenforcreateingroup',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
}

r = requests.post(url, headers=headers)
data = r.json()
token = data[0]['access_token']

print('OPTIONS Status: {}'.format(r.status_code))
print('OPTIONS Header: {}\n'.format(r.headers))

url = 'https://wabi-south-central-us-redirect.analysis.windows.net/export/xlsx'

headers = {
    #'accept': 'application/json, text/plain, */*',
    #'accept-encoding': 'gzip, deflate, br',
    #'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #'activityid': '7b62c09d-74f8-4895-98e3-04b826a524e8',
    #'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlNzWnNCTmhaY0YzUTlTNHRycFFCVEJ5TlJSSSIsImtpZCI6IlNzWnNCTmhaY0YzUTlTNHRycFFCVEJ5TlJSSSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzg5MzU3MWItNmMyYy00Y2VmLWI0ZGEtN2Q0YjI2NmEwNjI2LyIsImlhdCI6MTU5MzcyMzAwNSwibmJmIjoxNTkzNzIzMDA1LCJleHAiOjE1OTM3MjY5MDUsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJFMkJnWUFqVWtjN3pxWHl2YXpBaFlJSjd6ZnpYQWNYdkdnSzlmMjlyTUpHWWxuemJ1aDRBIiwiYW1yIjpbIndpYSJdLCJhcHBpZCI6Ijg3MWMwMTBmLTVlNjEtNGZiMS04M2FjLTk4NjEwYTdlOTExMCIsImFwcGlkYWNyIjoiMiIsImZhbWlseV9uYW1lIjoiR0FSUk9GRSBTQU1QQUlPIiwiZ2l2ZW5fbmFtZSI6IkJSVU5PIiwiaXBhZGRyIjoiMTQyLjQwLjE3Ni42OSIsIm5hbWUiOiJCcnVubyBHYXJyb2ZlIiwib2lkIjoiODRhZGM5NDMtNTQ4NC00MmM3LWFiYTItMzNmMTllNGNhNDA0Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTExNjE5NzU4OTgtMzAyMzYxOTIyNC04OTAxMzc0OTgtMjA1MDU4IiwicHVpZCI6IjEwMDMzRkZGODg0MDFDNTgiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJlNVNjOHRJV2tpMTZiM29sSnpvanhhSmZqT3lUVllCZTdON3oyR2tueXRVIiwidGlkIjoiNzg5MzU3MWItNmMyYy00Y2VmLWI0ZGEtN2Q0YjI2NmEwNjI2IiwidW5pcXVlX25hbWUiOiJicnVuby5nYXJyb2ZlQHZhbGUuY29tIiwidXBuIjoiYnJ1bm8uZ2Fycm9mZUB2YWxlLmNvbSIsInV0aSI6InZfd0tnZFFkWDB5UG5KbDZGM05iQUEiLCJ2ZXIiOiIxLjAifQ.SZJiA5uQGGlocHhvTZYFtUBt9NF9cOxFpdmowomOysDyA0KmyLQKg2xLs8a2ljPQuZJkpnVsqkZK3Ejfcr9v3pTIe3uYTActSixa1AKhmyzPtOhOT0WoGrSF79T4T7kpRAjiiMl5V1tOwEROsES6kcGe5jENA5Dv6ZPsweWhYLXOoqZXk15ESWiHEo6qLvdiwnh0Ca4azU-a8uuzsuRB54hc-bAWmhflfccJukzqELPxcefxgKyEfM4-DWN4ta2N55Kbhzm3WPqn7oMXXFZ1jWL7AuUtmM6ZPhKrP4wWS6EMjp6TPZVmVNfjcCOaexMc0nlr4V09fI6tqIcXOaAIpA',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSIsImtpZCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzg5MzU3MWItNmMyYy00Y2VmLWI0ZGEtN2Q0YjI2NmEwNjI2LyIsImlhdCI6MTU5NDczOTE0OSwibmJmIjoxNTk0NzM5MTQ5LCJleHAiOjE1OTQ3NDMwNDksImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBU1FBMi84UUFBQUF1TUxxbUgwZHhvTGNWMk9zb29VeTJ5YmhDSkFkeUNnMEoxS1JCVzFLc2N3PSIsImFtciI6WyJ3aWEiXSwiYXBwaWQiOiJkZWU4NDk2ZC1kZjMyLTQ3NTAtYWQ3MS01M2I3Yzg2OTUwNTEiLCJhcHBpZGFjciI6IjEiLCJmYW1pbHlfbmFtZSI6IkdBUlJPRkUgU0FNUEFJTyIsImdpdmVuX25hbWUiOiJCUlVOTyIsImlwYWRkciI6IjE0Mi40MC4xNzYuNjkiLCJuYW1lIjoiQnJ1bm8gR2Fycm9mZSIsIm9pZCI6Ijg0YWRjOTQzLTU0ODQtNDJjNy1hYmEyLTMzZjE5ZTRjYTQwNCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xMTYxOTc1ODk4LTMwMjM2MTkyMjQtODkwMTM3NDk4LTIwNTA1OCIsInB1aWQiOiIxMDAzM0ZGRjg4NDAxQzU4Iiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgUmVwb3J0LlJlYWQuQWxsIFJlcG9ydC5SZWFkV3JpdGUuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWQuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWRXcml0ZS5BbGwgV29ya3NwYWNlLlJlYWQuQWxsIFdvcmtzcGFjZS5SZWFkV3JpdGUuQWxsIiwic3ViIjoiZTVTYzh0SVdraTE2YjNvbEp6b2p4YUpmak95VFZZQmU3Tjd6Mkdrbnl0VSIsInRpZCI6Ijc4OTM1NzFiLTZjMmMtNGNlZi1iNGRhLTdkNGIyNjZhMDYyNiIsInVuaXF1ZV9uYW1lIjoiYnJ1bm8uZ2Fycm9mZUB2YWxlLmNvbSIsInVwbiI6ImJydW5vLmdhcnJvZmVAdmFsZS5jb20iLCJ1dGkiOiJnTEtjTmw0QkxrR3AzS2FJRnA2YkFBIiwidmVyIjoiMS4wIn0.G3PVPT7loVPBPZlEiic8crWo413VdvBlKdWaD1WtPpdBTb_aVvMXf5bx-T3RwKY8Tr1J_bme424yZd9kRkFtuKuXj0ZU4dQswO9f5pUVb2uTiHu-P7NXzizYvgwsQtT1w92J0eJgwjfkRlN7mmuwVfZQJ5JrTtn7Cq7C5Vr5gB0R9p7nOUZ_8Kh00099HWNsAJy3VWTqs0cBUOM1_dxuWQgjq_C_ECtqB-z4IXgJH3BCrUP3Wia3fJp0f-N5CJSiB-j5J46fNtYEz7aQSqs9GimkgaYqNXnd1YczEdSylFlEg304RmdnGm3kF2wKcx6rNzrk6CylIjXSENuAXN9ayA',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.powerbi.com',
    'referer': 'https://app.powerbi.com/groups/me/apps/7434fbfe-fd0f-4cfc-89fb-f9aac7c3a40a/reports/9a0e7cc0-2697-414e-a854-5857084da2b2/ReportSection?noSignUpCheck=1',
    #'requestid': '469b2c90-cd87-b17a-c58d-ed3922af6eec',
    #'sec-fetch-dest': 'empty',
    #'sec-fetch-mode': 'cors',
    #'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
}

payload = {
    "exportDataType": 0,
    "executeSemanticQueryRequest": {
        "version": "1.0.0", 
        "queries": [
            {
                "Query": {
                    "Commands": [
                        {
                            "SemanticQueryDataShapeCommand": {
                                "Query": {
                                    "Version": 2, 
                                    "From": 
                                    [
                                        {
                                            "Name": "b", 
                                            "Entity": "Base", 
                                            "Type": 0
                                        }, {
                                            "Name": "d", 
                                            "Entity": "de_para_plant", 
                                            "Type": 0
                                        }
                                    ], 
                                    "Select": 
                                    [
                                        {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Source": "b"
                                                    }
                                                }, 
                                                "Property": "VENDOR_NAME"
                                            }, 
                                            "Name": "Base.VENDOR_NAME"
                                        }, 
                                        {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Source": "b"
                                                    }
                                                }, 
                                                "Property": "Total_Otif"
                                            }, 
                                            "Name": "Base.Total_Otif"
                                        }, {"Measure": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "Valor_Otif_Nao"}, "Name": "Base.Valor_Otif_Nao"}, {"Measure": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "Valor_Otif_Sim"}, "Name": "Base.Valor_Otif_Sim"}, {"Measure": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "%Otif"}, "Name": "Base.%Otif"}], "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "IMPACTO_BRUMADINHO"}}], "Values": [[{"Literal": {"Value": "'N'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "FLAG_ATP"}}], "Values": [[{"Literal": {"Value": "'N'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "FLAG_CRC"}}], "Values": [[{"Literal": {"Value": "'N'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "FLAG_REJECTED"}}], "Values": [[{"Literal": {"Value": "'N'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "FLAG_REQUISITION"}}], "Values": [[{"Literal": {"Value": "'Y'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "OTIF_REMESSA_FINAL"}}], "Values": [[{"Literal": {"Value": "'Y'"}}], [{"Literal": {"Value": "'N'"}}]]}}}, {"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "SCP_COUNTRY_DESC"}}], "Values": [[{"Literal": {"Value": "'Brazil'"}}], [{"Literal": {"Value": "'Canada'"}}], [{"Literal": {"Value": "'Malaysia'"}}], [{"Literal": {"Value": "'Mozambique'"}}], [{"Literal": {"Value": "'Paraguay'"}}], [{"Literal": {"Value": "'Indonesia'"}}]]}}}, {"Condition": {"Not": {"Expression": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "PLANT_PLANT_DESCRIPTION"}}], "Values": [[{"Literal": {"Value": "'8201:PT Vale Eksplorasi Indo:1561'"}}], [{"Literal": {"Value": "'8202:PT STM Jakarta:1492'"}}], [{"Literal": {"Value": "'8203:PT STM Sumbawa:1492'"}}]]}}}}}], "OrderBy": [{"Direction": 2, "Expression": {"Measure": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "Total_Otif"}}}]}, "Binding": {"Primary": {"Groupings": [{"Projections": [0, 1, 2, 3, 4], "Subtotal":0}]}, "DataReduction":{"Primary": {"Top": {"Count": 1000000}}}, "Version": 1}}}, {"ExportDataCommand": {"Columns": [{"QueryName": "Base.VENDOR_NAME", "Name": "Vendor Name"}, {"QueryName": "Base.Total_Otif", "Name": "TOTAL OTIF"}, {"QueryName": "Base.Valor_Otif_Nao", "Name": "OTIF N"}, {"QueryName": "Base.Valor_Otif_Sim", "Name": "OTIF Y"}, {"QueryName": "Base.%Otif", "Name": "%OTIF"}], "Ordering": [0, 2, 3, 1, 4], "FiltersDescription":"Filtros aplicados:\nIMPACTO_BRUMADINHO é N\nFLAG_ATP é N\nFLAG_CRC é N\nFLAG_REJECTED é N\nFLAG_REQUISITION é Y\nOTIF_REMESSA_FINAL é Y ou N\nSCP_COUNTRY_DESC é Brazil, Canada, Malaysia, Mozambique, Paraguay ou Indonesia\nPLANT_PLANT_DESCRIPTION não é 8201:PT Vale Eksplorasi Indo:1561, 8202:PT STM Jakarta:1492 ou 8203:PT STM Sumbawa:1492"}}]}}], "cancelQueries": [], "modelId": 2293282, "userPreferredLocale": "pt-BR"}, "artifactId": 2113986}

r = requests.post(url, headers=headers, data=json.dumps(payload))

print('POST Status: {}'.format(r.status_code))
print('POST Header: {}'.format(r.headers))

with open('data.xlsx', 'wb') as fp:
    fp.write(r.content)
