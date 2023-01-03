import pandas as pd
from tqdm import tqdm





def Validate(OriginPath, SavePath, ReportPath, FileNm):
    """
    ~made for LDY~
    :param OriginPath:
    :param SavePath:
    :param ReportPath:
    :param FileNm:
    :return:
    """
    data = pd.read_csv(OriginPath+'/'+FileNm+'.csv')

    data = data.drop([data.columns[0]], axis=1)

    data['Validate'] = (data['상태 갱신 일시'] < data['최종 충전종료 일시']) | ((data['최종 충전종료 일시'] < data['최종 충전시작 일시']) & (data['(충전중)충전시작 일시'] < data['최종 충전시작 일시']))
    data.loc[data['충전 용량'].isnull(), 'Validate'] = True
    data.loc[data['최종 충전종료 일시'].isnull(), 'Validate'] = True
    data.loc[data['최종 충전시작 일시'].isnull(), 'Validate'] = True
    data['Validate'] = data['Validate'].replace(True, 1)
    data['Validate'] = data['Validate'].replace(False, 0)


    # 유효성 오류 발생 데이터 선별
    print(len(data.index[data['Validate'] == 1]))
    d_datas = data.index[data['Validate'] == 1]
    print(data)

    # Operating Entity Check
    data['운영기관 명'] = data['운영기관 명'].apply(OperEntChk)


    data.to_csv("./" + SavePath + "/" + FileNm + ".csv", mode='w', encoding='utf-8-sig')

    dData = data[data['Validate'].isin([0])]
    dData.to_csv("./" + SavePath + "/D" + FileNm + ".csv", mode='w', encoding='utf-8-sig')

def OperEntChk(x):
    if x in ['퍼워큐브','파워큐브','파워큐브코리아']: x = '파워큐브'
    if x in ['대영채비','대영채비(주)','대영채비㈜']: x = '대영채비'
    if x in ['삼성EVC','삼성이브이씨','(주)삼성이브이씨']: x = '삼성EVC'
    if x in ['(주)이카플러그', '이카플러그']: x = '이카플러그'
    if x in ['주식회사 에버온', '에버온']: x = '에버온'
    if x in ['HUMAX EV', '휴맥스이브이']: x = 'HUMAX EV'
    if x in ['타디스테크놀로지(evPlug)', 'evPlug(타디스테크놀로지)']: x = 'evPlug'
    if x in ['(주)스타코프', '스타코프','스타코프(주)스타코프','스타코프스타코프']: x = '스타코프'
    print(x)
    return x