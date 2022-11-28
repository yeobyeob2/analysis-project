import pandas as pd
import numpy as np


def relocation():
    data = pd.read_csv("Downloads/서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding="euc-kr")
    data['year'] = data['사용월'].apply(lambda x: str(x)[:4])

    data_sr = data.sort_values(by=['호선명', '지하철역'], ascending=[True, True])

    x_data = ['2015', '2016', '2017']
    data_qr = data_sr.query('year != @ex_year')

    df = data_qr.iloc[0:, 0:47]

    return df


dr_df = re_data.drop('사용월', axis = 1)

col_sum_df = dr_df.groupby('호선명').sum()