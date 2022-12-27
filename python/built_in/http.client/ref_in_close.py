"""
우연히 디버깅을 하다가, python built in에서 http client의 소스를 분석하게 되었다. python SSL socket은 close할 때 _real_close 플래그를 체크하는데, 이는 socket을 참조하는 대상을 체크하여 사용중인 소캣을 종료하지 못하도록 되어 있다.

그렇기에 사용중인 (예를 들어, 다운로드 중이라거나) HTTPConnection object는 close가 불가하다.
"""