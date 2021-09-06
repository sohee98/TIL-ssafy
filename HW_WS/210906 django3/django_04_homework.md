# django 04 homework

1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가? 

   * method가 POST인데 데이터가 유효하지 않을 때, POST가 아닐때 create페이지를 render해야 한다.
   * 즉, method가 POST가 아닌데 유효할때를 제외하고 항상  create페이지를 render하는데, 그 때는 이미 return을 했기 때문에 함수가 끝난다.
   * 그러므로 그 외의 상황에 항상 적용 될 수 있게 조건문과 같은 레벨에 작성되어있다.

   

2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

   * GET이 먼저 있으면, else 구문에서 GET이 아닐 때, 즉 POST, PUT, DELETE등 일 때 수행되는데, POST구문은 save()가 있는, DB에 무언가 조작을 하는 코드이다. 
   * POST가 먼저 있으면, else 구문에서 POST가 아닐 때, 즉 GET, PUT, DELETE등 일 때 단순히 form 인스턴스를 생성하는 코드이다.
   * 사용자가 다른 method로 요청했을 때, DM조작을 하는 코드보다 단순히 인스턴스를 생성하는 코드를 수행하는 것이 바람직하기 때문에, DB조작과 관련되지 않은 코드가 실행되도록 하기 위함이다.

