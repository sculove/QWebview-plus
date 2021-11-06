# QWebview-plus V2.0
 - 키움 오픈 API+ for JavaScript를 지원하는 Chromium 기반의 WebView 브라우저
 - 키움 오픈 API를 사용할 수 있는 WebView와 DevTool을 제공
 - 키움 오픈 API의 데이터 인터페이스 변경

## Development Environment
 - Window OS 32bit 권장
 - 키움증권 Open API+ (https://www1.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)
 - Python 3.8.10 `32bit` (https://www.python.org/downloads/release/python-344/)
   - PyQt5.9 이상
   - PyQtWebEngine
   - pandas

## Install
> pip install qwebview-plus


## How to use
> 

## 키움 Open API+를 제공하는 kiwoom 객체
### window.kiwoom
 - [키움 오픈 API](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.5.pdf?dummyVal=0)와 동일한 메소드를 제공
 - 키움 오픈 API와 네이밍 규칙이 다름
    - 첫 문자가 대문자 아닌 소문자 `CommConnect => commConnect`

### 이벤트
 - [키움 오픈 API](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.5.pdf?dummyVal=0)와 동일한 이벤트를 제공
 - 모든 이벤트는 `document`에서 발생한다.
 - 키움 오픈 API와 네이밍 규칙이 다름
    - `kiwoom` 이라는 event namespace가 붙음
    - 이벤트 명에서 `on`이라는 prefix가 제거하고, 첫 문자를 소문자로 변경 `OnReceiveTrData => receiveTrData.kiwoom`
    - 이벤트에 의해 전달되는 속성은 detail에 포함되어 전달됨
    - 이벤트에 전달되는 속성명은 타입약어가 제거되고, 첫 문자를 소문자로 변경 `sScrNo => scrNo`

### 키움 오픈 API와의 차별점
  - 로그인 API인 commConnect는 브라우저에서 별도의 API를 제공하지 않는다.
     - 로그인은 자동으로 QWebViewPlusWidget 생성시 자동으로 로그인을 진행한다.
     - 로그인 이벤트는 제공하지 않는다.
  - 데이터를 얻을 때 필요한 함수들은 제공하지 않는다.
     - getRepeatCnt
     - commGetData
     - getCommDataEx
     - getCommRealData
     - getChejanData
  - 대신 이벤트에서 발생한 데이터는 QWebview-plus 이벤트에서 정제하여 전달된다.
  - TR요청시 설정하는 setInputValue 함수는 제공하지 않고 setInputValue로 설정 가능한 dictionary 파라미터를 TR요청 함수에서 제공한다.
     - commRqData(rQName, trCode, prevNext, screenNo, `inputDic`)
     - commKwRqData(arrCode, next, codeCount, typeFlag, rQName, screenNo, `inputDic`)
    

## License
Licensed under MIT:

https://opensource.org/licenses/MIT
