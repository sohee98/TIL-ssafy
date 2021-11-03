#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- SPA는 Single Pattern Application의 약자이다. - F
- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이지 갱신에 필요한 데이터만 전달받는다. - T
- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다 - T





#### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

* **M** - Model, **V** - View, **VM** - View Model
* Model : JavaScript의 Object 자료 구조. Vue Instance 내부에서 data로 사용되는데, 이 값이 바뀌면 View(DOM)가 반응.
* View : DOM(HTML). Data의 변화에 따라서 바뀌는 대상
* View Model : 모든 Vue Instance. View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리
  * View Model을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민하는 것





#### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

(a) message

(b) new Vue

(c) '#app'

