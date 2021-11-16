#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- DRF Server는 단순히 요청에 따라 데이터 및 인증을 처리하는 등의 역할만 담당할 뿐 반드시 Vue가 Client일 필요는 없다. - T
- Vue & DRF가 기존에 Django만 사용했을 때와 다른 점은 Django의 MTV 중 Template 부분을 Vue가 대체한 것이다. - T
- 같은 localhost에서 활성화 되어있는 Django와 Vue.js 서버는 서로 제약없이 리소스를 요청하고 응답 받을 수 있다. - F



#### 2. Server-Client 구조의 애플리케이션에서 사용자 인증 기능을 구현하고자 한다. Client는 Vue 그리고 Server는 DRF를 이용하여 구현했다고 할 때, DRF에서 지원하는 세션 인증 방식과 토큰 인증 방식의 차이점을 서술하시오.

#### * 세션인증방식

* 동작방식
  * 사용자가 로그인을 요청하고 id, pw 정보가 유효하다면, 세션이 서버의 메모리 상에 저장된다. 이때 세션 식별키로 SessionId를 기준으로 정보를 저장한다.
  * 서버에서 sessionId를 cookie에 담아 브라우저로 전달한다.
  * 브라우저는 모든 request에 cookie(sessionId)를 함께 전송한다.
  * 서버는 브라우저가 보낸 sessionId를 키로 서버 메모리에서 사용자의 session 정보를 식별하고 유효하다면, 원하는 응답을 제공해준다.

* 세션 기반 인증 방식은 클라이언트로부터 요청을 받으면, 클라이언트의 상태를 서버에서 계속 유지하고 이 정보를 서비스에 이용하는 Stateful 서버이다.



#### * 토큰인증방식 - JWT

* JWT는 서버와 클라이언트 간 정보를 주고 받을 때 HTTP request header에 JSON 토큰(access token)을 넣은 후 서버는 별도의 인증 과정 없이 헤더에 포함되어 있는 JWT 정보를 통해 인증한다.

* 동작 방식
  * 사용자가 로그인을 요청하고 id, pw 정보가 유효하다면, 서버에서 Secret Key를 사용해서 JWT(access token, refresh token)을 발급한다.
  * 서버에서 JWT를 브라우저로 전달한다. 이때, 사용자의 local storage에 JWT(access token, refresh token)를 저장한다.
  * 브라우저는 모든 request의 헤더에 access token을 함께 전송한다.
  * 서버는 브라우저가 보낸 access token을 식별하고 유효하다면, 원하는 응답을 제공해준다.

* 서버는 클라이언트의 정보를 저장하지 않고, JWT의 발급과 매 요청마다 header에 넘어오는 access token의 유효성 검사만 진행한다.
* 클라이언트는 JWT를 local storage에 저장한다.
* 서버가 클라이언트의 정보를 저장하지 않으므로 Stateless 서버이다.



#### 차이점

* 세션인증방식은 서버에서 저장하지만, 토큰인증방식은 클라이언트에서 저장하므로 서버의 메모리, DB등의 부담이 없다.



#### 3. DRF Server에서 JWT 인증 방식을 이용하여 사용자 인증 기능을 구현했다고 하자. 이 때, Client에서 인증이 필요한 API endpoint로 요청을 보내기 위해서는 JWT 값을 HTTP __(a)__ request header에 실어서 요청을 보내야 한다. __(a)__ request header의 이름과 특징을 작성하시오.

* (a) Authorization

* HTTP `Authorization` 요청 헤더는 서버의 사용자 에이전트임을 증명하는 자격을 포함하여, 보통 서버에서 `401 Unauthorized` 상태를 WWW-Authenticate (en-US) 헤더로 알려준 이후에 나온다.

