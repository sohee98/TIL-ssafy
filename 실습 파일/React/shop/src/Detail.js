import axios from 'axios';
import React, {useState, useEffect} from 'react';
import { useHistory, useParams } from 'react-router-dom';
import styled from 'styled-components'
import './Detail.scss';

let 박스 = styled.div`
  padding : 20px;
`;

let 제목 = styled.h4`
  font-size : 25px;
  color : ${ props => props.색상 }
`;

function Detail(props){

  let [alert, alert변경] = useState(true);
  useEffect(()=> {
    // 페이지를 방문하자마자 Ajax요청을 실행하고 싶으면
    // axios.get()

    // 2초 후에 alert 창 사라지게
    let 타이머 = setTimeout(()=>{ alert변경(false) }, 2000)
    return ()=>{ clearTimeout(타이머) }
  },[]);


  let { id } = useParams();
  let history = useHistory();
  let 찾은상품 = props.shoes.find(function(상품){
    return 상품.id == id
  });
  let [inputData, inputData변경] = useState();


  return (
    <div className="container">
      <박스>
        <제목 className="red"> Detail</제목>
      </박스>
      
      { inputData }
      <input onChange={(e)=>{ inputData변경(e.target.value) }}/>

      {
        alert === true
        ? (<div className='my-alert2'>
            <p>재고가 얼마 남지 않았습니다.</p>
           </div>)
        : null
      }

      <div className="row">
        <div className="col-md-6">
          <img src={"https://codingapple1.github.io/shop/shoes" + (찾은상품.id+1) + ".jpg"} width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">{찾은상품.title}</h4>
          <p>{찾은상품.content}</p>
          <p>{찾은상품.price}원</p>

          <Info 재고={props.재고} id={찾은상품.id}></Info>

          <button className="btn btn-danger" onClick={()=>{
            let 새로운재고 = [...props.재고]
            새로운재고[찾은상품.id] -= 1
            props.재고변경(새로운재고)
          }}>주문하기</button> 
          <button className="btn btn-danger" onClick={()=>{
            history.goBack()
          }}>뒤로가기</button> 
        </div>
      </div>
    </div> 
  )
}

function Info(props){
  return(
    <p>재고 : {props.재고[props.id]}</p>
  )
}


export default Detail;