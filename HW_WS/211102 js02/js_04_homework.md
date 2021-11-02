#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

* Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다. - T
* XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 JavaScript API이다. XHR의 메서드로 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다. - T

* axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다 - F



#### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

* Call Stack에서 `console.log('Hello SSAFY!')` 처리
  * 'Hello SSAFY!' 출력
* Call Stack에서 `setTimeout(function() {console.log('I am from setTimeout')}, 1000)` 처리
  * setTimeout()은 시간이 걸리므로 Web API으로 이동 후 처리 (대기)
* Call Stack에서 `console.log('Bye SSAFY!')` 처리
  * 'Bye SSAFY!' 출력

* Task Queue로 `function() {console.log('I am from setTimeout')}` 이동 후 대기
* main thread가 끝났으므로 Event Loop이 Task Queue에서 실행 대기중인 callback 함수가 있는지 확인 
  * 가장 앞에 있는 `console.log('I am from setTimeout')`을  CallStack으로 push
* Call Stack에서 `console.log('I am from setTimeout')` 처리
  * 'I am from setTimeout' 출력



#### 3. JS는 Event loop를 기반으로 하는 Concurrency model을 가지고 있다고 한다. Concurrency 키워드의 특징을 작성하고, 이와 비슷한 키워드로 비교되는 Parallelism의 개념과 두 개념의 차이점을 서술하시오.

* Concurrency model : Event loop을 기반으로 하는 **동시성 모델**
* Concurrency - 동시성
  *  빠르게 전환하며 여러 작업을 수행하여 동시에 여러 작업이 실행되는 것처럼 보이는 것
  * 논리적인 개념

* Parallelism - 병렬성
  * 실제로 여러 작업을 동시에 수행하는 것
  * 물리적인 개념