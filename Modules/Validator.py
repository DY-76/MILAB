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

    data['Validate'] = (data['상태 갱신 일자'] < data['최종 충전종료 일시']) | (data['최종 충전종료 일시'] < data['최종 충전시작 일시'])
    data['Validate'] = data['Validate'].replace(True, 1)
    data['Validate'] = data['Validate'].replace(False, 0)


    #유효성 오류 발생 데이터 선별
    print(len(data.index[data['Validate'] == 1]))
    d_datas = data.index[data['Validate'] == 1]
    print(data)

    # for d_data in tqdm(d_datas, ascii=True, desc="Creating report ..."):
    #     #리포트 작성 코드 . . .
    #     print(d_data, end=" ")
    #     data = data.drop(data.index[d_data])

    print(data)
    data.to_csv("./" + SavePath + "/" + FileNm + ".csv", mode='w', encoding='utf-8-sig')