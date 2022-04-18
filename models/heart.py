from urllib.parse import urlencode, unquote
import requests
import xmltodict

class HeartVo:
    def __init__(self, ):
        url = "http://apis.data.go.kr/B552657/AEDInfoInqireService/getAedFullDown"
        queryString = "?" + urlencode(
            {
                "serviceKey": unquote(
                    "9JVC8qrDZUUkrmVHQDWSA9wAC6EbU3AdXudhkpnIuNTUF1nHlPlYdhuU%2FhBiwkoZrLkSLWAKtYqaOc0WSC8gqw%3D%3D"),
                "numOfRows": 9999
            }
        )

        queryURL = url + queryString
        response = requests.get(queryURL)

        self.r_dict = xmltodict.parse(response.text)
        self.r_response = self.r_dict.get("response")
        self.r_body = self.r_response.get("body")
        self.r_items = self.r_body.get("items")

    def __str__(self):
        return self.r_dict + ' / ' + self.r_response + ' / ' + self.r_body + ' / ' + self.r_items


class HeartService:
    def __init__(self):
        self.HeartVo = HeartVo()

    def getAedFullDown(self):  # 자동제세동기 FullData 내려받기 (전체목록조회?)
        return self.HeartVo.r_items


    def getBySido(self, sido):
        List = []
        for i in self.HeartVo.r_items['item']:
            try:
                if sido in i['sido']:
                    List.append(i)
            except KeyError as e:
                continue
        return List

    def getByModel(self, model):
        modelList = []
        for i in self.HeartVo.r_items['item']:
            try:
                if model in i['model']:
                    modelList.append(i)
            except KeyError as e:
                continue
        return modelList


    def getByOrg(self, org):
        orgList = []
        for i in self.HeartVo.r_items['item']:
            try:
                if org in i['org']:
                    orgList.append(i)
            except KeyError as e:
                continue
        return orgList