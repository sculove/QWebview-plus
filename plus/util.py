# -*- coding: utf-8 -*-
# -*-coding: utf-8 -*-
from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtWebEngineWidgets import QWebEngineScript


def parseErrorCode(code):
    """에러코드 메시지

    :param code: 에러 코드
    :type code: str
    :return: 에러코드 메시지를 반환

    ::

        parseErrorCode("00310") # 모의투자 조회가 완료되었습니다
    """
    code = str(code)
    ht = {
        "0": "정상처리",
        "-10": "실패",
        "-100": "사용자정보교환에 실패하였습니다. 잠시후 다시 시작하여 주십시오.",
        "-101": "서버 접속 실패",
        "-102": "버전처리가 실패하였습니다.",
        "-105": "함수입력값 오류",
        "-106": "통신연결 종료",
        "-200": "시세조회 과부하 (조회횟수 제한 초과)",
        "-201": "REQUEST_INPUT_st Failed",
        "-202": "요청 전문 작성 실패",
        "-204": "조회가능한 종목수 초과 (한번에 조회 가능한 종목개수는 최대 100종목)",
        "-205": "데이터 수신 실패",
        "-206": "조회가능한 FID수 초과 (한번에 조회 가능한 FID개수는 최대 100개)",
        "-300": "주문 입력값 오류(허용되지 않는 입력값)",
        "-301": "계좌비밀번호를 입력하십시오.",
        "-302": "타인계좌는 사용할 수 없습니다.",
        "-303": "주문가격이 20억원을 초과합니다.",
        "-304": "주문가격은 50억원을 초과할 수 없습니다.",
        "-305": "주문수량이 총발행주수의 1%를 초과합니다.",
        "-306": "주문수량은 총발행주수의 3%를 초과할 수 없습니다.",
        "-307": "주문전송 실패",
        "-308": "주문전송 과부하 (주문횟수 제한 초과)",
        "-340": "계좌정보 없음",
        "-500": "종목코드 없음",
    }
    return ("[%s] " + ht[code]) % code if code in ht else code


def readFile(filepath):
    file = QFile(filepath)
    if not file.open(QIODevice.ReadOnly):
        raise SystemExit(
            "Failed to load qwebchannel_plus.js with error: %s" % file.errorString()
        )
    file = bytes(file.readAll()).decode("utf-8")
    return file


def createScript(sourceCode, injectionPoint=QWebEngineScript.DocumentCreation):
    script = QWebEngineScript()
    script.setSourceCode(sourceCode)
    # script.setName(name)
    script.setWorldId(QWebEngineScript.MainWorld)
    script.setInjectionPoint(injectionPoint)
    script.setRunsOnSubFrames(True)
    return script
