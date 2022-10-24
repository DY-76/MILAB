import pandas as pd

def ToSourceData(OriginPath, SavePath, FileNm):
    """
    ~made for LDY~
    :param OriginPath: 오리지널 파일 경로
    :param SavePath: 저장 경로
    :param FileNm: 오리지널 파일 이름
    :return: SourceData로 전처리 된 파일과 파일 이름
    """
    data = pd.read_csv(OriginPath+'/'+FileNm+'.csv')
    data = data[["충전소 명",
                 "충전소 ID",
                 "충전기 ID",
                 "충전 용량",
                 "위도",
                 "경도",
                 "상태 갱신 일자",
                 "최종 충전시작 일시",
                 "최종 충전종료 일시" ]]
    data.to_csv("./" + SavePath + "/SD_" + FileNm + ".csv", mode='w', encoding='utf-8-sig')
    print(data)


def ToValidatedData(OriginPath, SavePath, FileNm):
    """
    ~made for LDY~
    :param OriginPath: 오리지널 파일 경로
    :param SavePath: 저장 경로
    :param FileNm: 오리지널 파일 이름
    :return: ValidatedData로 전처리 된 파일과 파일 이름
    """
    data = pd.read_csv(OriginPath+'/'+FileNm+'.csv')
    data = data[["충전소 ID",
                 "충전기 ID",
                 "충전 용량",
                 "위도",
                 "경도",
                 "상태 갱신 일자",
                 "최종 충전시작 일시",
                 "최종 충전종료 일시" ]]
    data.to_csv("./" + SavePath + "/VD_" + FileNm + ".csv", mode='w', encoding='utf-8-sig')
    print(data)