#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. - T
- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다. - T
- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다. - F
- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다. - T



#### 2. Vuex에서 Actions과 Mutations의 역할과, 각각에 작성되는 핸들러의 특징을 서술하시오.

* Actions
  * Mutations와 유사하지만 다음과 같은 차이점이 있음
    * state를 변경하는 대신 mutations를 `commit()` 메서드로 호출해서 실행
    * mutations와 달리 비동기 작업이 포함될 수 있음
  * context 객체 인자를 받음
    * context 객체를 통해 store.js파일 내에 있는 모든 요소의 속성 접근 & 메서드 호출이 가능
    * 단, 가능하지만 state를 직접 변경하지 않음
  * 컴포넌트에서 `dispatch()`메서드에 의해 호출됨
  * "Actions를 통해 state를 조작 할 수 있지만, state는 오로지 Mutations를 통해서만 조작해야함"
    * 명확한 역할 분담을 통해 서비스 규모가 커져도 state를 올바르게 관리하기 위함



* Mutations
  * "실제로 state를 변경하는 유일한 방법"
  * mutation의 핸들러 함수는 반드시 동기적이어야 함
    * 비동기적 로직은 state가 변화하는 시점이 의도한 것과 달라질 수 있으며, 콜백이 실제로 호출될 시기를 알 수 있는 방법이 없음
  * 첫번째 인자로 항상 **state**를 받음
  * Actions에서 `commit()` 메서드에 의해 호출됨



#### 3. 컴포넌트에 작성된 Todo App 관련 코드를 Vuex의Store로 옮기고자 한다. 빈 칸 (a), (b), (c), (d)에들어갈 코드를 작성하시오.

(a) state

(b) getters

(c) actions

(d) state