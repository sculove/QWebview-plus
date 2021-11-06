from pandas import DataFrame

output = {
  'opt10001': ["종목코드", "종목명", "결산월", "액면가", "자본금", "상장주식", "신용비율", "연중최고", "연중최저", "시가총액", "시가총액비중", "외인소진률", "대용가", 
    "PER", "EPS", "ROE", "PBR", "EV", "BPS", "매출액", "영업이익", "당기순이익", "250최고", "250최저", "시가", "고가", "저가", "상한가", "하한가", "기준가", 
    "예상체결가", "예상체결수량", "250최고가일", "250최고가대비율", "250최저가일", "250최저가대비율", "현재가", "대비기호", "전일대비", "등락율", "거래량", "거래대비", "액면가단위", "유통주식", "유통비율"],
  'opt10079': ["종목코드","현재가","거래량","거래대금", "일자", "시가", "고가", "저가", "수정주가구분", "수정비율", "대업종구분", "소업종구분", "종목정보", "수정주가이벤트", "전일종가"]
}

FID = {
  10: "현재가",
  11: "전일대비",
  12: "등락율",
  13: "누적거래량",
  14: "누적거래대금",
  16: "시가",
  17: "고가",
  18: "저가",
  25: "전일대비기호",
  26: "전일거래량대비",
  27: "매도호가",
  28: "매수호가",
  29: "거래대금증감",
  30: "전일거래대금증감",
  31: "거래회전율",
  32: "거래비용",
  311: "시가총액",
  567: "상한가발생시간",
  568: "하한가발생시간",

}

realOutput = {
  "주식시세": [10, 11, 12, 27, 28, 13, 14, 16, 17, 18, 25, 26, 29, 30, 31, 32, 311, 567, 568],
}

class TrParser:
  def __init__(self, kiwoom):
    self.kiwoom = kiwoom
  
  def getSingleDictionary(self, columns, trCode, rQName):
    values = []
    for key in columns:
      values.append(self.kiwoom.commGetData(trCode, "", rQName, 0, key))
    return dict(zip(columns, values))

  def getMultiDictionary(self, columns, trCode, rQName):
    data = self.kiwoom.getCommDataEx(trCode, rQName)
    data = DataFrame(data, columns=columns).to_dict("records")
    return data

  def parse(self, trCode, rQName):
    # 주식 틱/분봉/일봉/주봉/월봉차트 조회 요청
    if trCode == "opt10079" or trCode == "opt10080" or trCode == "opt10081" or trCode == "opt10082" or trCode == "opt10083":
      data = self.getMultiDictionary(output['opt10079'], trCode, rQName)
    # 주식기본정보요청
    elif trCode == "opt10001":  
      data = self.getSingleDictionary(output['opt10001'], trCode, rQName)

    return data
    