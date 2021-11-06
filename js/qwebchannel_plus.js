"use strict";
// QWebchannel 사용 예
new QWebChannel(qt.webChannelTransport, function(channel){
    let kiwoom = window.kiwoom = channel.objects.kiwoom;

    // 이벤트 처리
    kiwoom.fireEvent.connect(function(kiwoomEventName, rawData) {
        const event = document.createEvent("CustomEvent");
        const data = JSON.parse(rawData);
        event.initCustomEvent(kiwoomEventName, true, true, data);
        document.dispatchEvent(event);
        console.log("EVENT", kiwoomEventName);
    });
});