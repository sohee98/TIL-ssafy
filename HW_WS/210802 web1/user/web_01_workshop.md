### 1. img tag 

아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는 <img>  tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.


```html
<div>
  <img src="C:\Users\sohee\Desktop\practice\210802\image\my_photo.png" alt="ssafy">
</div>
```

<div>
  <img src="C:\Users\sohee\Desktop\practice\210802\image\my_photo.png" alt="ssafy">
</div>


### 2. 파일 경로 

위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작성하면 된다. 

(a) : 절대 경로

(b) : 상대 경로

```html
<div>
  <img src="../image/my_photo.png" alt="ssafy">
</div>
```

<div>
  <img src="../image/my_photo.png" alt="ssafy">
</div>



### 3. Hyper Link 

출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.


```html
<a href="https://www.ssafy.com">
  <img class="fit picture" src="../image/my_photo.png" alt="ssafy로 이동">
</a>
```

<a href="https://www.ssafy.com">
  <img class="fit picture" src="../image/my_photo.png" alt="ssafy로 이동">
</a>



### 4. 선택자

(1)  ![image-20210802175806167](md-images/image-20210802175806167.png)

(2) ![image-20210802180651710](md-images/image-20210802180651710.png)



(3)

**`:nth-child()`**는 모든 자식들, 즉 형제 사이에서의 순서에 따라 요소를 선택합니다. `<p>첫번째 단락</p>` 이 형제사이에서 두번째에 있으므로 선택자가 적용됩니다.

**`:nth-of-type()`**는 부모 속성에서 특정 태그를 가진 자식 속성에서 순서에 따라 요소를 선택합니다. `<p>`속성을 가진 자식중에 두번째에 있는  `<p>두번째 단락</p>`에 선택자가 적용됩니다.

