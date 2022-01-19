import React from 'react';
import {Table} from 'react-bootstrap';
import { connect } from 'react-redux';

function Cart(props){
  return (
    <div>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경</th>
          </tr>
        </thead>
        <tbody>
          {
            props.state.map((상품, i) => {
              return (
                <tr>
                  <td>{ props.state[i].id }</td>
                  <td>{ props.state[i].name }</td>
                  <td>{ props.state[i].quan }</td>
                  <td><button onClick={()=>{ props.dispatch({ type:'수량증가' })}}>+</button></td>
                  <td><button onClick={()=>{ props.dispatch({ type:'수량감소' })}}>-</button></td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>
      { props.alert열렸니 === true
        ? (<div className="my-alert2">
            <p>지금 구매하시면 20% 할인</p>
            <button onClick={()=>{ props.dispatch({type:'alert닫기'})}}>닫기</button>
          </div>)
        : null
      }
    </div>
  )
}

function 함수명(state){
  return {
    state : state.reducer,
    alert열렸니 : state.reducer2,
  }
}

export default connect(함수명)(Cart);
// export default Cart;