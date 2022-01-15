### 1. import / export

* 내보내기 : export default 변수명
  * 한 파일에 한번만 쓸 수 있음
  * 내보낼 변수가 많다면 `export {변수1, 변수2}`

* 가져오기 : import 변수명 from 경로

  * export한 변수이름 그대로 사용해야함

  ```
  import name from './data.js'
  ```

  

### 2. Router1 페이지 나누기

* 설치 : `npm install react-router-dom@5`

* index.js -> `<BrowserRouter>`

  ```js
  import { BrowserRouter } from 'react-router-dom';
  
  ReactDOM.render(
    <React.StrictMode>
      <BrowserRouter>
        <App/>
      </BrowserRouter>
    </React.StrictMode>,
    document.getElementById('root')
  );
  ```

* Hashrouter : 라우팅 안전하게 할 수 있게 도와줌

  * `http://localhost:3000/#/` : 사이트 주소 뒤에 #이 붙는데 #뒤에 적는것은 서버로 전달 X

* BrowserRouter : 라우팅을 리액트가 아니라 서버에게 요청할 수도 있어서 위험



### 3. Router2 : Link, Switch, history 기능

`import { Link, Route, Switch } from 'react-router-dom'`

* #### Route

  ```html
  <Route exact path="/"> 
    <div>메인페이지인데요</div>
  </Route>
  <Route path="/detail">
    <div>상세페이지인데요</div>
  </Route>
  <Route path="/어쩌구" component={Card} ></Route>
  ```

  * 리액트 라우터 특징 : HTML 내부의 내용을 갈아치워서 다른 페이지처럼 보여주는 것
  * 컴포넌트 만들기
    * Detail.js 파일 생성 : 보통 컴포넌트이름 그대로 파일 만듬
      * 컴포넌트 파일 만들 때 `import React` 꼭 해야함

* #### Link

  * 페이지 이동버튼 만들기

  ```html
  <Nav.Link> <Link to='/'>Home</Link> </Nav.Link>
  <Nav.Link> <Link to='/detail'>Detail</Link> </Nav.Link>
  ```

  ```html
  <Nav.Link as={Link} to='/'>Home</Nav.Link>
  <Nav.Link as={Link} to='/detail'>Detail</Nav.Link>
  ```

* history : 뒤로가기 버튼 만들기

  ```js
  import { useHistory } from 'react-router-dom';.
  
  function Detail(){
    let history = useHistory();
    return (
      <button onClick={()=>{ 
        history.goBack() }} className="btn btn-danger"
      >뒤로가기</button> 
    )
  };
  ```

  * useHistory라는 훅 import -> useHistory() 훅 사용
  * `goBack()` : history에 저장된 여러 자료들 중 뒤로가기 할 때 사용
  * 특정경로로 이동시키기 = `history.push('/')` 

* #### Switch

  * 여러개가 맞아도 하나만 보여주세요~

  * 중복 매칭을 허용하지 않겠다는 의미

  * Switch 안에 담았더니 Route들이 하나씩만 보임

    ```html
    <Switch>
    	<Route path="/detail">디테일</Route>
    	<Route path="/:id">아무거나</Route>
    </Switch>
    ```

    > =>디테일만 보임  ("/:id" = 모든문자)



### 4. Router3 : URL parameter

* `detail/0` 하면 0번 데이터가 나오게

* `/detail/:id `: 아무문자나 받겠다는 URL 작명법

  * 클론뒤에 맘대로 작명, 여러개 사용가능

* ```html
  <Route path="/detail/:id">
  ```

* ```js
  import { useHistory, useParams } from 'react-router-dom';
  
  function Detail(props){
  	let { id } = useParams();
  }
  ```

* `let { id } = useParams();` : {사용자가 입력한 URL파라미터들} 

  * useParams() 라는 함수는 현재 URL에 적힌 모든 파라미터를 {파라미터1,파라미터2} 로 저장
  * id라는 변수는 :id 자리에 있던 숫자를 의미



### 5. Styling1 : styled-components

* 설치 : `npm install styled-components`
* `import styled from 'styled-components'` : import 해야 함

* CSS를 미리 입혀놓은 컴포넌트를 사용 (className 작명 필요없음)

  * 가장 큰 장점 : 컴포넌트가 많아지면 class 겹칠 일이 줄어들음

  ```js
  let 박스 = styled.div`
    padding : 20px;
  `;
  let 제목 = styled.h4`
    font-size : 25px;
    color : ${ props => props.색상 }
  `;
  ```

  ```html
  <박스>
      <제목 색상="red"> Detail</제목>
  </박스>
  ```

* props 문법 

  * 보낼이름={변수명}
  * 보낼이름="일반문자"



### 6. styling2 : SASS

* 설치 : `npm install node-sass`
* SASS : CSS를 프로그래밍 언어스럽게 작성가능한 Preprocessor(전처리엔진언어)
  * 브라우저는 SASS 문법 모름 -> SASS로 작성한 파일을 다시 CSS로 컴파일 해야함 (node-sass가 알아서 해줌)

* Detail.scss 파일 만듬
  * Detail.js => `import './Detail.scss';`

* SASS  문법

  1. 변수사용 (원하는 곳에서 `$변수명` 으로 사용)

      * `$변수명 : 집어넣을값;`
      
  2. @import 파일경로
      * 다른 css (혹은 scss)파일에 저장해두고 필요해질 때마다 `@import` 해오면 편리
  
  3. 셀렉터 대신 쓰는 nesting
  
        ```css
        div.container {
          h4 {
            color: blue;
          }
          p {
            color: green;
          }
        }
        ```
  
  4. 복붙하지말고 @extend
  
     ```css
     .my-alert {
       background: #eeeeee;
       padding: 20px;
       border-radius: 5px;
       max-width: 500px;
       width: 100%;
       margin: auto;
     }
     
     .my-alert2 {
       @extend .my-alert;
       background-color: #ffe591;
     }
     ```
  
  5. 함수는 @mixin / @include
  
        ```css
        @mixin 함수() {
          background: #eeeeee;
          padding: 20px;
          border-radius: 5px;
          max-width: 500px;
          width: 100%;
          margin: auto;
        }
        
        .my-alert {
         @include 함수()
        }
        ```
  
        

### 7. lifecycle Hooks 

* Hook으로 컴포넌트의 인생 중간주간에 뭔가 명령을 줄 수 있음
  * componentDidMount(){}
  * componentWillUnMount(){}

```
useEffect(()=>{
    //코드를 적습니다 여기
  });
```

* useEffect 훅 : 컴포넌트가 mount 되었을 때/ update 될 때 특정 코드를 실행
  * `setTimeout( ()=>{  1초 후 실행할 코드 }, 1000);`
* useEffect 훅2 : 컴포넌트가 사라질 때 코드를 실행시킬 수도 있음
  * `return funtion 어쩌구(){ 실행할 코드~~~~ }`

* useEffect 훅3 : 여러개를 사용하고 싶다면
  * useEffect  여러개 사용하면 됨. 순서대로 실행됨

* useEffect 훅4 : 특정 state가 변경될때만 실행

  *  ```js
      useEffect(()=> {
         // 2초 후에 alert 창 사라지게
         let 타이머 = setTimeout(()=>{ alert변경(false) }, 2000)
       },[alert]);	// alert라는 state가 변경이 될때만 실행
     ```

  * [] 안에 아무것도 없으면 => <Detail>등장시 한번 실행하고 끝남

> setTimeout  타이머를 사용했으면 타이머해제도 사용해야함
>
> ```
> useEffect(()=> {
>   let 타이머 = setTimeout(()=>{ alert변경(false) }, 2000)
>   return ()=>{ clearTimeout(타이머) }
> },[alert]);
> ```
>
> `**clearTimeout(타이머이름)**`



### 8. Ajax in React1

* Ajax : 서버에 새로고침없이 요청을 할 수 있게 도와줌
* 요청의 종류
  * GET 요청 : 주소창에 URL 적는 요청. 특정 페이지 / 자료 읽기
  * POST 요청 : 서버로 중요 정보 전달. 
  * 항상 새로고침됨

* Ajax
  1. jQuery 설치해서 $.ajax() 쓰든가
  2. axios 설치해서 axios.get() 쓰든가
  3. 쌩자바스크립트 fetch() 쓰든가

* axios : `npm install axios`
              `import axios from 'axios';`

  1. axios.get(데이터 요청할 URL)
  2. 성공하면 .then()
  3. 실패하면 .catch()

  ```js
  <button className="btn btn-primary" onClick={()=>{ 
    axios.get('https://codingapple1.github.io/shop/data2.json')
    .then((result)=>{ 
        console.log(result.data) 
        shoes변경([...shoes, ...result.data])
    })
    .catch(()=>{ console.log('실패했어요') })
  }}>더보기</button>
  ```
  
  * 가져온 자료 출력하는 법 : .then((가져온자료)=>{})

* fetch

  ```js
  fetch('https://codingapple1.github.io/shop/data2.json').then()
  ```

  따옴표가 있는 JSON 

  -> axios 쓰면 JSON을 알아서 Object로 바꿔줌

  -> fetch는 Object로 바꿔줘야함



### 9. Component in Component

1. 하위 컴포넌트가 몇개든 데이터를 전송하려면 props를 씁니다.
2. 하위컴포넌트가 상위 컴포넌트 state변경하려면 state변경함수 씁니다. 그게 상위에 있으면 props로 전송해서 사용함.









