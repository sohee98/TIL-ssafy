/* eslint-disabled */

import React, {useState} from 'react';
import { Navbar,Container,Nav,NavDropdown,Button } from 'react-bootstrap';
import './App.css';
import data from './data.js';
import Detail from './Detail.js';
import { Link, Route, Switch } from 'react-router-dom'
import axios from 'axios';

function App() {

  let [shoes, shoes변경] = useState(data)
  let [재고, 재고변경] = useState([10,11,12]);

  return (
    <div className="App">
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">SHOP</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to='/'>Home</Nav.Link>
              <Nav.Link as={Link} to='/detail'>Detail</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Switch>
        <Route exact path="/"> 
          <div className="background">
            <div className='mt-4 p-5 text-white rounded'>
              <h1>20% Season Off</h1>
              <p>asdfasdf</p>
              <p>
                <Button variant='primary'>Learn more</Button>
              </p>
            </div>
          </div>
          <div className="container">
            <div className="row">
              {
                shoes.map((shoe, i) => {
                  return <Shoe shoe={shoe} i={i} key={i}></Shoe>
                })
              }
            </div>
            <button className="btn btn-primary" onClick={()=>{ 
              // 로딩중이라는 UI 띄움
              // axios.post('서버URL', { id:'codingapple', px:1234 }).then()

              axios.get('https://codingapple1.github.io/shop/data2.json')
              .then((result)=>{ 
                // 로딩중UI 삭제
                // console.log(result.data) 
                shoes변경([...shoes, ...result.data])
              })
              .catch(()=>{ console.log('실패했어요') })
            }}>더보기</button>
          </div>
        </Route>

        <Route path="/detail/:id">
          <Detail shoes={shoes} 재고={재고} 재고변경={재고변경}></Detail>
        </Route>

        <Route path="/:id">
          <div>asdfasdfasdf</div>
        </Route>
      </Switch>
      {/* <Route path="/어쩌구" component={Card} ></Route>  */}
    </div>
  );
}

function Shoe(props){
  return (
    <div className="col-md-4">
      <img src={"https://codingapple1.github.io/shop/shoes" + (props.i+1) + ".jpg"} width='100%'></img>
      <h4>{props.shoe.title}</h4>
      <p>{props.shoe.content} <br></br> {props.shoe.price}원</p>
    </div>
  )
}


export default App;
