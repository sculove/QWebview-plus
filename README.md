# QWebview-plus
 - 키움 오픈 API+ for JavaScript를 지원하는 Webkit2 기반의 WebView
 - ES5 지원

## Development Environment
 - Windows 32bit 권장
 - 키움증권 Open API+ (https://www1.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)
 - Python 3.4.4 32bit (https://www.python.org/downloads/release/python-344/)
 - pyQt5.5.1 32bit (https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/)

## 키움 Open API+를 제공하는 kiwoom 객체 제공

### window.kiwoom
 - [키움 오픈 API](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.1.pdf)와 동일한 메소드를 제공
 - 키움 오픈 API와 네이밍 규칙이 다름
    - 첫 문자가 대문자 아닌 소문자 `CommConnect => commConnect`

### 이벤트
 - [키움 오픈 API](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.1.pdf)와 동일한 이벤트를 제공
 - 모든 이벤트는 `document`에서 발생한다.
 - 키움 오픈 API와 네이밍 규칙이 다름
    - `kiwoom` 이라는 event namespace가 붙음
    - 이벤트 명에서 `on`이라는 prefix가 제거하고, 첫 문자를 소문자로 변경 `OnReceiveTrData => receiveTrData.kiwoom`
    - 이벤트에 의해 전달되는 속성은 detail에 포함되어 전달됨
    - 이벤트에 전달되는 속성명은 타입약어가 제거되고, 첫 문자를 소문자로 변경 `sScrNo => scrNo`

## 사용 예
```bash
python main.py -u [실행항 URL]
python main.py -f [실행할 html 파일명]
```
> 실행할 파일을 입력하지 않을 경우, 기본적으로 index.html을 부른다.
>
> - -f --file 시작 페이지 경로 (기본: ./index.html)
> - -u --url 시작 URL 경로
>
> **URL과 페이지 경로를 함께 입력했을 경우, URL이 우선한다.**

## [Kiwoom-Helper](https://github.com/sculove/Kiwoom-Helper) 유틸
QWebview-Plus에서 제공하는 kiwoom 객체와 이벤트를 손쉽게 사용할 수 있는 유틸
> 별도의 프로젝트로 관리 https://github.com/sculove/Kiwoom-Helper

## License
Licensed under MIT:

https://opensource.org/licenses/MIT
