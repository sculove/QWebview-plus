from pandas import DataFrame
from plus.tr import TR_OUTPUT, TR_REAL_OUTPUT, FID


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
        if (
            trCode == "opt10079"
            or trCode == "opt10080"
            or trCode == "opt10081"
            or trCode == "opt10082"
            or trCode == "opt10083"
        ):
            data = self.getMultiDictionary(TR_OUTPUT["opt10079"], trCode, rQName)
        # 주식기본정보요청
        elif trCode == "opt10001":
            data = self.getSingleDictionary(TR_OUTPUT["opt10001"], trCode, rQName)

        return data


class RealParser:
    def __init__(self, kiwoom):
        self.kiwoom = kiwoom

    def getRealData(self, codes, realData):
        columns = []
        values = []
        for codeKey in codes:
            values.append(self.kiwoom.getCommRealData(realData, codeKey))
            columns.append(FID[codeKey])
        return dict(zip(columns, values))

    def parse(self, realType, realData):
        data = {}
        if TR_REAL_OUTPUT[realType]:
            data = self.getRealData(TR_REAL_OUTPUT[realType], realData)
        else:
            print("실시간 요청 TR이 존재하지 않습니다 ({realType})".format(realType=realType))
        return data
