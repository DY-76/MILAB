import pandas as pd
import datetime
import scipy.stats as stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

validTime = datetime.timedelta(days=1, hours=0, seconds=0)
validMTime = datetime.timedelta(days=0, hours=0, seconds=0)
def Calculate(OriginPath, SavePath, FileNm):

    data = pd.read_csv(OriginPath+'/'+FileNm+'.csv')

    data['충전 시간'] = data[['최종 충전종료 일시', '최종 충전시작 일시']].apply(date_sub, axis=1)
    data['충전 시간 초'] = data['충전 시간'].apply(time_to_sec)
    data['산출 충전 용량(kWh)'] = data[['충전 용량', '충전 시간 초']].apply(charge_capacity, axis=1)

    #Valid 임시
    data = data[data['충전 시간'] != validMTime]

    print(data)

    data.to_csv("./" + SavePath + "/" + FileNm + "_C.csv", mode='w', encoding='utf-8-sig')

    cap_data = data['산출 충전 용량(kWh)'].values.tolist()
    #임시 데이터 분석
    plt.figure(figsize=(20,5))
    sns.distplot(cap_data, bins=300, color="blue")
    plt.show()
    plt.figure(figsize=(10, 5))
    stats.probplot(cap_data, dist=stats.norm, plot=plt)
    plt.show()

def date_sub(x):
    BDate = datetime.datetime.strptime(str(int(x[0])),'%Y%m%d%H%M%S')
    SDate = datetime.datetime.strptime(str(int(x[1])),'%Y%m%d%H%M%S')
    OutDate = BDate - SDate
    if(OutDate >= validTime or OutDate < validMTime):
        OutDate = datetime.timedelta(days=0, hours=0, seconds=0)
    #print(type(OutDate), OutDate, int(OutDate.total_seconds()))
    return OutDate

def time_to_sec(x):
    return int(x.total_seconds())

def charge_capacity(x):
    return (int(x[0])*int(x[1]))/3600