import pandas as pd

def Validate(OriginPath, SavePath, ReportPath, FileNm):
    """"""
    data = pd.read_csv(OriginPath+'/'+FileNm+'.csv')

    data['Validate'] = (data['상태 갱신 일자'] < data['최종 충전종료 일시']) | (data['최종 충전종료 일시'] < data['최종 충전시작 일시'])
    data['Validate'] = data['Validate'].replace(True, 1)
    data['Validate'] = data['Validate'].replace(False, 0)

    print(data.index[data['Validate'] == 1])
    print(len(data.index[data['Validate'] == 1]))
    print(data)

    data.to_csv("./" + SavePath + "/" + FileNm + ".csv", mode='w', encoding='utf-8-sig')