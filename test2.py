import requests
import json

url = 'https://wabi-south-central-us-redirect.analysis.windows.net/export/xlsx'

headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSIsImtpZCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzg5MzU3MWItNmMyYy00Y2VmLWI0ZGEtN2Q0YjI2NmEwNjI2LyIsImlhdCI6MTU5NDczOTE0OSwibmJmIjoxNTk0NzM5MTQ5LCJleHAiOjE1OTQ3NDMwNDksImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBU1FBMi84UUFBQUF1TUxxbUgwZHhvTGNWMk9zb29VeTJ5YmhDSkFkeUNnMEoxS1JCVzFLc2N3PSIsImFtciI6WyJ3aWEiXSwiYXBwaWQiOiJkZWU4NDk2ZC1kZjMyLTQ3NTAtYWQ3MS01M2I3Yzg2OTUwNTEiLCJhcHBpZGFjciI6IjEiLCJmYW1pbHlfbmFtZSI6IkdBUlJPRkUgU0FNUEFJTyIsImdpdmVuX25hbWUiOiJCUlVOTyIsImlwYWRkciI6IjE0Mi40MC4xNzYuNjkiLCJuYW1lIjoiQnJ1bm8gR2Fycm9mZSIsIm9pZCI6Ijg0YWRjOTQzLTU0ODQtNDJjNy1hYmEyLTMzZjE5ZTRjYTQwNCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xMTYxOTc1ODk4LTMwMjM2MTkyMjQtODkwMTM3NDk4LTIwNTA1OCIsInB1aWQiOiIxMDAzM0ZGRjg4NDAxQzU4Iiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgUmVwb3J0LlJlYWQuQWxsIFJlcG9ydC5SZWFkV3JpdGUuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWQuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWRXcml0ZS5BbGwgV29ya3NwYWNlLlJlYWQuQWxsIFdvcmtzcGFjZS5SZWFkV3JpdGUuQWxsIiwic3ViIjoiZTVTYzh0SVdraTE2YjNvbEp6b2p4YUpmak95VFZZQmU3Tjd6Mkdrbnl0VSIsInRpZCI6Ijc4OTM1NzFiLTZjMmMtNGNlZi1iNGRhLTdkNGIyNjZhMDYyNiIsInVuaXF1ZV9uYW1lIjoiYnJ1bm8uZ2Fycm9mZUB2YWxlLmNvbSIsInVwbiI6ImJydW5vLmdhcnJvZmVAdmFsZS5jb20iLCJ1dGkiOiJnTEtjTmw0QkxrR3AzS2FJRnA2YkFBIiwidmVyIjoiMS4wIn0.G3PVPT7loVPBPZlEiic8crWo413VdvBlKdWaD1WtPpdBTb_aVvMXf5bx-T3RwKY8Tr1J_bme424yZd9kRkFtuKuXj0ZU4dQswO9f5pUVb2uTiHu-P7NXzizYvgwsQtT1w92J0eJgwjfkRlN7mmuwVfZQJ5JrTtn7Cq7C5Vr5gB0R9p7nOUZ_8Kh00099HWNsAJy3VWTqs0cBUOM1_dxuWQgjq_C_ECtqB-z4IXgJH3BCrUP3Wia3fJp0f-N5CJSiB-j5J46fNtYEz7aQSqs9GimkgaYqNXnd1YczEdSylFlEg304RmdnGm3kF2wKcx6rNzrk6CylIjXSENuAXN9ayA',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.powerbi.com',
    'referer': 'https://app.powerbi.com/groups/me/apps/7434fbfe-fd0f-4cfc-89fb-f9aac7c3a40a/reports/9a0e7cc0-2697-414e-a854-5857084da2b2/ReportSection?noSignUpCheck=1',
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
