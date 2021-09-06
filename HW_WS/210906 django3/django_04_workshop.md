# django 04 workshop

1. Model Form을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오. 

   ```
   (a) forms.Modeform
   (b) Meta
   ```

   

2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오. 

   * method가 POST이고 데이터가 유효하지 않을 때 아무 페이지도 렌더링하지 못해 오류가 발생한다.

   * method가 POST이고 데이터가 유효할 때는 이미 return을 했고, 그 외에 항상 create페이지를 render해야 한다.

   * context 구문과 return 구문을 `if request.method == 'POST'`와 같은 레벨에 위치시켜야 한다.

     

3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

   ```python
   (a) form = ReservationForm(request.POST, instance=reservation)
   (b) form = ReservationForm(instance=reservation)
   ```

   

4. form 출력을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

   ```
   as_p()
   as_ul()
   as_table() 
   ```

   

