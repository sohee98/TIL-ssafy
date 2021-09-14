### 1. CSS flex-direction
Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

* row : 주축방향이 왼쪽에서 오른쪽이다.  기본값이다.
* row-reverse : 주축방향이 오른쪽에서 왼쪽이다. 
* column : 주축방향이 위쪽에서 아래쪽이다. 
* column-reverse : 주축방향이 아래쪽에서 위쪽이다. 



### 2. Bootstrap flex-direction
  flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

* row : flex-row
* row-reverse : flex-row-reverse
* column : flex-column
* column-reverse : flex-column-reverse



### 3. align-items
  align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

* align-items-start : cross축 기준 위쪽 정렬
* align-items-end : cross축 기준 아래쪽 정렬
* align-items-center : cross축 기준 가운데 정렬
* align-items-baseline : item내부의 text에 기준선을 맟춤
* align-items-stretch : 컨테이너를 가득 채움(기본값)



### 4. flex-flow
  flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.
  (1) flex-direction, flex-wrap
  (2) flex-direction, align-items
  (3) justify-content, flex-wrap
  (4) justify-content, align-items

* **정답)** (1)  flex-direction, flex-wrap



### 5. Bootstrap Grid System
  하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, __(a)__, __(b)__ 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class="__(a)__">
    <div class="__(b)__">
        <div class="col-__(c)__-__(d)__"></div>
        </div>
    </div>
</div>
```

* **정답)** (a) = container  (b) = row



### 6. Breakpoint prefix
  Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.
1. __(c)__에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.

   * 공백, sm, md, lg, xl, xxl 이 들어갈 수 있다.
   * 768px > sm >= 576px
     992px > md >= 768px
     1200px > lg >= 992px
     1400px > xl >= 1200px
     xxl >= 1400px
   * 창이 위 범위에 속할때의 col의 수를 결정할 수 있다.

   

2. __(d)__에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
   * 1~12까지의 숫자가 들어갈 수 있다.
   * 한 row가 col 12개이고, 각 col이 12칸 중 몇칸을 차지할건지 결정할 수 있다.

