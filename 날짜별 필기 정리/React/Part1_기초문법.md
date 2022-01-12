### 1. React 프로젝트 만들기

```bash
npx create-react-app 폴더명

# 코드 미리보기
npm start
```

> https://ko.reactjs.org/docs/create-a-new-react-app.html

* App.js : 메인페이지에 들어갈 HTML 짜는 곳  ==index.js==> index.html

* node_modules : 라이브러리 모은 폴더
* public : static 파일 보관함
* src : 소스코드 보관함
* package.json : 설치한 라이브러리 목록 (건들필요없음)



### 2.  JSX

* 태그에 class 주기

    ```js
    import './App.css';		// App.css 에서 디자인
	
    // class="" 안됌
    <div className="클래스명"></div>
	```

* 리액트에서 데이터 바인딩 쉽게하는 법 

  * 데이터 바인딩 : 데이터를 HTML에 꽂아넣는 것
  * 중괄호 안에 변수명, 함수 등 넣으면 됨
  * src, id, href 등의 속성에도 {변수명, 함수 등}
  * 모든 곳에 {}로 변수 집어넣기 가능

  ```js
  let posts = '강남 고기 맛집'
  ```

  ```html
  <h4> { posts } </h4>
  <img src={ logo }/>
  ```

* JSX에서 style 속성 집어넣을 때

  * style={object 자료형으로 만든 스타일}
  * camelCase 작명 관습에 따라 속성명을 바꿔야 함
  * `let post = { color:'blue', fontSize:'30px' }` 
    `style={ posts }` 도 가능

  ```html
  <div style={ { color:'blue', fontSize:'30px' } }>개발 Blog</div>
  ```

  

### 3. useState

* 데이터 저장 방법
  1. 변수에 넣거나
  2. state에 넣거나

* 리액트의 데이터 저장공간 state 만드는 법

  1. { useState } 상단에 첨부 -

     ```
     import React, {useState} from 'react' ;
     ```

  2. `useState(데이터)`

     * [a, b] => 두개의 데이터가 있는 array가 남음
     * a : '' 안에있는 데이터 == state  데이터
     * b : '' 안에있는 데이터 정정해주는 함수 == state 데이터 변경 함수

> [참고] ES6 destructuring 문법 - array, object에 있던 자료를 변수에 쉽게 담고 싶을 때
>
> var [a, b] = [10, 100] ;
>
> var a = 10
> var b = 100

* state는 
  * 변수 대신 쓰는 데이터 저장공간
  * `useState()`를 이용해 만들어야 함
  * 문자, 숫자, array, object 다 저장가능

* state에 데이터 저장해놓는 이유 
  * 웹이 App처럼 동작하게 만들고 싶어서
  * HTML이 **자동으로 재렌더링**이 된다
  * 그냥 변수는 변경되어도 자동 재렌더링 안됨 -> 새로고침 해야됨

* 자주 바뀌는, 중요한 데이터를 변수말고 state로 저장해서 쓰세요.



### 4. event

* `onClick={클릴될 때 실행할 함수}`
* `onClick={ ()=>{실행할 내용} }`

* state는 그냥 변경 안됨
  * 변경함수(대체할 데이터)
  * state 변경함수로 변경해야 재렌더링이 잘 일어난다

```html
<span onClick={ ()=>{따봉변경(따봉+1)} } >👍</span> {따봉}
```



### 5. setState

* `<button onClick={ 제목바꾸기 }>버튼</button>`  
  * 제목바꾸기() => 소괄호가 있으면 바로 실행됨. 소괄호 없어야 눌러야 실행됨

* 수정된 [데이터]를 만듬

  * 그런데 원본 state 수정 x (특히 state가 array, object 자료형이면)

  * state의 복사본을 만들어서 수정 => deep copy해서 수정

    ```js
    var newArray = 글제목; //이건 복사가 아니라 값공유. reference data type특징
    var newArray = [...글제목]; //값공유X 서로 독립적인 값을 가지는 복사
    ```

* Array, Object state 데이터 수정 방법 

  * 일단 변경함수 써야함
  * 변경함수(대체할데이터)
  * state는 직접 건들지 마셈 => deep copy해서 그걸 변경

  ```js
  let [글제목, 글제목변경] = useState(['남자코트 추천', '짜장면 맛집', '여자가방 추천']);
  function 제목바꾸기(){
    var newArray = [...글제목];
    newArray[0] = '여자코트 추천' 
    글제목변경( newArray );
  } 
  ```

* #### 리액트에서 state를 수정할 때

  1. **일단 기존 state 카피본 만들고**
  2. **카피본에 수정사항 반영하고**
  3. **변경함수()에 집어넣기**



### 6. component

* return 안에 div 연달아 쓰는거 불가능. 하나의 html 태그로 끝나야함

  ```
  return(
    <div></div>
    <div></div>		# 불가능
  );
  ```

* HTML을 한 단어로 줄여서 쓸 수 있는 방법: 리액트의 Component 문법

* Component 만드는법

  1. 함수 만들고 이름짓고
  2. 축약을 원하는 HTML 넣고
  3. 원하는 곳에서 <함수명 />

  ```js
  function Modal(){
    return (
      <div className="modal">
        <h2>제목</h2>
        <p>날짜</p>
        <p>상세내용</p>
      </div>
    );
  }
  ```

  ```html
  <Modal />
  ```

* Component 유의사항

  1. 이름은 대문자

  2. return() 안에 있는건 태그 하나로 묶어야함

     > return() 내부를 묶을 때 의미없는 `<div>`쓰기 싫으면 `<></>` 

  3. function 만들 때 나란히 만듬

* Component 만드는 기준 
  * 반복출현하는 HTML 덩어리들
  * 자주 변경되는 HTML UI들
  * 다른 페이지 만들 때도 컴포넌트로 만듦
* Component 장단점
  * 장점 : 관리가 편해짐
  * 단점 : state 쓸 때 복잡해짐 (상위 component에서 만든 state 쓰려면 props 문법 이용해야함)



### 7. Modal UI

*  if 대신 삼항연산자

  * { 조건식 ? 참일 때 실행할 코드 : 거짓일 때 실행할 코드 }

  ```html
  {
      modal === true
      ? <Modal></Modal>
      : null					# 텅빈 HTML이라는 뜻
  }
  ```

* 리액트에선 UI를 만들 때 state 데이터를 이용

  * 모달창을 켜고 닫는 스위치(UI 보임/안보임 스위치) 

    ```
    let [modal, modal변경] = useState(false);
    ```

  * 제목을 눌렀을 때 true로 바꿔줌 -> 모달창 띄움

    ```
    <h3 onClick={ ()=>{ modal변경(true) } }> { 글제목[2] }</h3>
    ```

* React 에서 클릭시 등장하는 UI 만드는 법

  * UI가 보임/안보인 정보를 state로 저장해둠
  * 그리고 if문을 이용해 state가 true일 때 UI를 보여줌

  

* Modal창 열고닫는 버튼 만들기

  ```js
  let [modal2, modal2변경] = useState(false);
  return (
    <div>
        <button onClick={ ()=>{ modal2변경(!modal2) } }>열고닫는버튼</button>
  	  {
          modal2 === true
          ? <Modal></Modal>
          : null
  	  }
    </div>
  )
  ```



### 8. map / for

* 반복문 쓰는 법 : `{ map() }`

  * array내의 모든 데이터에 똑같은 작업을 시켜주고 싶을 때 .map()

    ```js
    var 뉴어레이 = 어레이.map(function(a){
      return a*2
    })
    ```

  * { 반복할데이터.map( ()=>{ return <HTML> } ) }

* for 반복문을 쓰고 싶다면 -> 그냥 따로 함수를 만들어서 쓰셔야합니다.

  1. 따로 일반 함수를 만들고 

  2. 함수안에 HTML을 담을 array 자료를 하나 생성합니다. 

  3. 함수안에서 for 반복문을 이용해 array내에 HTML을 추가해줍니다.

  4. 완성된 array를 return 해줍니다. 

  5. 그리고 함수를 원하는 곳에 { 함수명() } 데이터바인딩 해주시면 됩니다. 

  ```js
  function App (){
    function 반복된UI(){
      var 어레이 = [];
      for (var i = 0; i < 3; i++) {
        어레이.push(<div>안녕</div>)
      }
      return 어레이
    }
    return (
      <div>
        HTML 잔뜩있는 곳
        { 반복된UI() }
      </div>
    )
  }
  ```

  

### 9. props

* 부모 컴포넌트 : <App>
  자식 컴포넌트 : <Modal>
  * App이 가진 State 쓸 수 있게 전송 가능
  * props로 전송해줘야 자식컴포넌트는 부모 컴포넌트가 가진 state 사용가능

* props 사용법

  1. `<자식컴포넌트 전송할이름={state명} />`

  2. ` function Modal(props){} `-> Modal 함수 소괄호 내에 props 파라미터를 하나 추가해줌
  3. `props.전송할이름` 

  ```html
  <Modal 글제목={글제목} ></Modal>
  ```

  ```js
  function Modal(props){
    return (
      <div className="modal">
        <h2>제목 {props.글제목[0]} </h2>
        <p>날짜</p>
        <p>상세내용</p>
      </div>
    );
  }
  ```

  

### 10. input

* 사용자가 input에 입력한 값을 입력값 state로 저장

* `<input onChange={ ()=>{} }></input>`
  * onChange : 뭔가 입력이 될 때 안의 함수가 실행됨

* 사용자가 입력한 값 = e.target.value

  ```js
  { 입력값 }
  <input onChange={ (e)=>{ 입력값변경(e.target.value) } }></input>
  ```

  

* map 반복문으로 돌린 HTML에는 key={}가 필요함 (warning이 안생김)

  ```js
  {
  	글제목.map(function(글, i){
          return (
          <div className="list" key={i}>			// key 필요
              <h3 onClick={ ()=>{ 누른제목변경(i) } }> { 글 } 
                <span onClick={ function 따봉더하기(){
                    var newArray2 = [...따봉];
                    newArray2[i] += 1
                    따봉변경( newArray2 );
                  } } 
                >👍</span> {따봉[i]} 
              </h3>
              <p>5월 10일 발행</p>
              <hr/>
          </div>
          )
      })
  }
  ```

  

* 글 발행 기능

  ```js
  <div className='publish'>
    <input onChange={ (e)=>{ 입력값변경(e.target.value) }}/>
    <button onClick={()=>{
      var newArray2 = [...글제목];
      newArray2.unshift(입력값)
      글제목변경( newArray2 )
      var newGood2 = [...따봉];
      newGood2.unshift(0)
      따봉변경( newGood2 )
      }}
    >저장</button>
  </div>
  ```

  1. 글제목을 복사해서 newArray2라는 카피본을 하나 만들고,
  2. 그걸 수정하고
  3. 그걸 새로운 글제목state가 되도록 입력.





