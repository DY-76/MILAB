import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tqdm import tqdm

# 항목 parsing 함수
def parse(item):
    try:
        STATNM = item.find("statNm").get_text()
        STATID = item.find("statId").get_text()
        CHGERID = item.find("chgerId").get_text()
        CHGERTYPE = item.find("chgerType").get_text()
        ADDR = item.find("addr").get_text()
        LOCATION = item.find("location").get_text()
        LAT = item.find("lat").get_text()
        LNG = item.find("lng").get_text()
        USETIME = item.find("useTime").get_text()
        BUSIID = item.find("busiId").get_text()
        BNM = item.find("bnm").get_text()
        BUSINM = item.find("busiNm").get_text()
        BUSICALL = item.find("busiCall").get_text()
        STAT = item.find("stat").get_text()
        STATUPDDT = item.find("statUpdDt").get_text()
        LASTTSDT = item.find("lastTsdt").get_text()
        LASTTEDT = item.find("lastTedt").get_text()
        NOWTSDT = item.find("nowTsdt").get_text()
        OUTPUT = item.find("output").get_text()
        METHOD = item.find("method").get_text()
        ZCODE = item.find("zcode").get_text()
        ZSCODE = item.find("zscode").get_text()
        KIND = item.find("kind").get_text()
        KINDDETAIL = item.find("kindDetail").get_text()
        PARKINGFREE = item.find("parkingFree").get_text()
        LIMITYN = item.find("limitYn").get_text()
        LIMITDETAIL = item.find("limitDetail").get_text()
        DELYN = item.find("delYn").get_text()
        DELDETAIL = item.find("delDetail").get_text()
        return {
            "충전소 명": STATNM,
            "충전소 ID": STATID,
            "충전기 ID": CHGERID,
            "충전기 타입": CHGERTYPE,
            "주소": ADDR,
            "상세 주소": LOCATION,
            "위도": LAT,
            "경도": LNG,
            "이용가능시간": USETIME,
            "기관 ID": BUSIID,
            "기관 명": BNM,
            "운영기관 명": BUSINM,
            "운영기관 연락처": BUSICALL,
            "충전기 상태": STAT,
            "상태 갱신 일시": STATUPDDT,
            "최종 충전시작 일시": LASTTSDT,
            "최종 충전종료 일시": LASTTEDT,
            "(충전중)충전시작 일시": NOWTSDT,
            "충전 용량": OUTPUT,
            "충전 방식": METHOD,
            "지역 코드": ZCODE,
            "지역 상세 코드": ZSCODE,
            "충전소 구분 코드": KIND,
            "충전소 구분 상세 코드": KINDDETAIL,
            "주차무료 여부": PARKINGFREE,
            "이용자 제한 여부": LIMITYN,
            "이용자 제한 사유": LIMITDETAIL,
            "삭제 여부": DELYN,
            "삭제 사유": DELDETAIL
        }
    # 버그나 parsing 항목 이슈 컨트롤을 위한 예외처리
    except AttributeError as e:
        return {
            "충전소 명": None,
            "충전소 ID": None,
            "충전기 ID": None,
            "충전기 타입": None,
            "주소": None,
            "상세 주소": None,
            "위도": None,
            "경도": None,
            "이용가능시간": None,
            "기관 ID": None,
            "기관 명": None,
            "운영기관 명": None,
            "운영기관 연락처": None,
            "충전기 상태": None,
            "상태 갱신 일시": None,
            "최종 충전시작 일시": None,
            "최종 충전종료 일시": None,
            "(충전중)충전시작 일시": None,
            "충전 용량": None,
            "충전 방식": None,
            "지역 코드": None,
            "지역 상세 코드": None,
            "충전소 구분 코드": None,
            "충전소 구분 상세 코드": None,
            "주차무료 여부": None,
            "이용자 제한 여부": None,
            "이용자 제한 사유": None,
            "삭제 여부": None,
            "삭제 사유": None
        }

def Colec(Num, Zcode, path):
    """
    ~made for LDY~
    :param Num: 총 호출할 데이터 수 입니다. 지역당 9000개 정도면 충분합니다. 9999를 호출할 경우 전체 데이터를 뽑습니다.
    :param Zcode: 지역코드입니다. 자세한건 가이드 참조
    :param path: 저장 경로입니다.
    :return: 저장 경로에 수집한 데이터를 csv로 변환하여 저장하고, 그 파일명(일시)를 출력합니다.
    """

    # 초기 선언(1회 실행을 위해 9999)
    page_num = 0
    tot_sum = 9999
    while(tot_sum == 9999):
        page_num += 1
        response = call_data(Num, Zcode, page_num)

        # Item 화
        soup = BeautifulSoup(response.text, 'lxml-xml')
        print("stat : "+soup.find("resultMsg").get_text())
        print("statCode : "+soup.find("resultCode").get_text())

        items = soup.find_all("item")

        # 데이터 임시저장소
        row = []
        tot_sum = 0
        for item in tqdm(items, ascii=True, desc="Parsing "):
            row.append(parse(item))
            tot_sum += 1

        # pandas 데이터프레임에 넣기
        df = pd.DataFrame(row)

        # 현재 시간의 csv 파일로 저장하기
        now = datetime.now()
        current_time = now.strftime("%Y%m%d%H%M%S")
        print(current_time+"_"+str(tot_sum)+"item_"+"Success!")
        df.to_csv("./"+path+"/"+current_time+'_p'+str(page_num)+".csv", mode='w', encoding='utf-8-sig')

    return current_time

def call_data(Num, Zcode, page):
    # API 호출
    print("API OriginalData Request..")
    url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
    # 전국데이터 출력
    if Zcode == 0:
        params = {
            'serviceKey': 'Zxc+L1BY7vTH4mkcjzGShFsue5yUAk2q55yjb3nUf7EeeXcsQTv9nE7qIjVN2oU01PuQMJ+iHQGuo2fa2ZlJlw==',
            'pageNo': page, 'numOfRows': Num}
    else:
        params = {
            'serviceKey': 'Zxc+L1BY7vTH4mkcjzGShFsue5yUAk2q55yjb3nUf7EeeXcsQTv9nE7qIjVN2oU01PuQMJ+iHQGuo2fa2ZlJlw==',
            'pageNo': page, 'numOfRows': Num, 'zcode': Zcode}

    return requests.get(url, params=params)