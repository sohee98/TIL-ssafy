/* eslint-disable */
import React, {useState} from 'react' ;
import logo from './logo.svg';
import './App.css';

function App() {

  let [글제목, 글제목변경] = useState(['남자코트 추천', '짜장면 맛집', '여자가방 추천']);
  let [따봉, 따봉변경] = useState([0, 0, 0]);
  // let posts = '강남 고기 맛집';
  
  // let [modal, modal변경] = useState(false);
  let [modal2, modal2변경] = useState(false);
  let [누른제목, 누른제목변경] = useState(0);

  let [입력값, 입력값변경] = useState('');

  function 제목바꾸기(){
    var newArray = [...글제목];
    newArray[0] = '여자코트 추천'
    글제목변경( newArray );
  } 

  function 글발행(){
    var newArray2 = [...글제목];
    newArray2.push(e.target.value)
    글제목변경( newArray2 )

    var newGood2 = [...따봉];
    newGood2.push(0)
    따봉변경( newGood2 )
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div>개발 Blog</div>
      </div>

      {/* <button onClick={ 제목바꾸기 }>버튼</button>

      <div className="list">
        <h3> { 글제목[0] } </h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3> { 글제목[1] }</h3>
        <p>5월 10일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3 onClick={ ()=>{ modal변경(true) } }> { 글제목[2] }</h3>
        <p>1월 8일 발행</p>
        <hr/>
      </div> */}

      {
        글제목.map(function(글, i){
          return (
          <div className="list" key={i}>
            <h3 onClick={ ()=>{ 누른제목변경(i) } }> { 글 } 
              <span onClick={ ()=>{
                  var newGood = [...따봉];
                  newGood[i] += 1
                  따봉변경( newGood );
                } } 
              >👍</span> {따봉[i]} 
            </h3>
            <p>5월 10일 발행</p>
            <hr/>
          </div>
          )
        })
      }

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


      {/* { 입력값 }
      <input onChange={ (e)=>{ 입력값변경(e.target.value) } }></input> */}

      {/* <button onClick={ ()=>{ 누른제목변경(0) } }>버튼1</button>
      <button onClick={ ()=>{ 누른제목변경(1) } }>버튼2</button>
      <button onClick={ ()=>{ 누른제목변경(2) } }>버튼3</button> */}

      {/* <button onClick={ ()=>{ modal2===true ? modal2변경(false) : modal2변경(true) } }>열고닫는버튼</button> */}
      <button onClick={ ()=>{ modal2변경(!modal2) } }>열고닫기</button>
      {
        modal2 === true
        ? <Modal 글제목={글제목} 누른제목={누른제목} ></Modal>
        : null
      }

    </div>
  );
}

function Modal(props){
  return (
    <div className="modal">
      <h2>{props.글제목[props.누른제목]} </h2>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  );
}







export default App;
