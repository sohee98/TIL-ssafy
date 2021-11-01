## Pair-programming

팀원 : A - 김소희, B - 이주용

| 수정 사항                                   | 작성자 |
| ------------------------------------------- | ------ |
| pjt05 프로젝트 생성, gitignore 작성         | A      |
| 가상환경 만든 후 requirements 작성          | B      |
| 가상환경 만든 후 requirements로 패키지 설치 | A      |
| movies app 생성, 프로젝트 구조 수정         | A      |
| models.py, admin.py, urls.py 작성           | B      |
| base.html 수정, forms.py, views.py 작성     | A      |
| base.html - navbar 추가                     | B      |
| create.html, detail.html 작성               | B      |
| update.html, index.html 작성                | A      |
| update.html 수정                            | B      |
| forms.py 수정, 스타일 수정                  | A      |
| 영화 목록 추가                              | B      |



## 소감

git에 pull, push를 반복하며 협업한 것은 처음이여서 많이 어려울거 같았는데, 오히려 같이 작성해 나가니깐 훨씬 수월했던 것 같다. 

처음에 가상환경 만드는 것 부터 막혀서 한참을 헤맸었다. pip list에 컴퓨터에 있는 모든 패키지가 떠서 당황했는데, 알고보니 가상환경을 만들어 놓고 활성화를 하지 않았어서 생긴 문제였다. 결국 프로젝트 파일을 다시 만들고 가상환경을 제대로 활성화 시킨 다음에 pip install을 해서 해결하였다. 

그 다음부터는 수월하게 수행했다. 프로젝트를 만들고, 앱을 만든 다음에 각 파일 안에 내용을 번갈아가며 작성했다. forms.py를 작성하는게 가장 헷갈렸는데, title과 poster_path는 forms.TextInput으로 설정하고, overview도 처음엔 forms.TextInput으로 해서 overview의 텍스트박스가 너무 작았는데, Textarea로 바꾸면 된다고 주용님이 알려주셔서 쉽게 해결할 수 있었다. 이처럼 서로 코드에 오류가 있는지 어디가 잘못됬는지 확인해가며 작성하니깐 혼자 할 때 보다 빠르게 할 수 있었다. 

협업해서 하는 점의 장점도 많지만, git에 올릴 때 오류나기가 쉽고 코드를 각자 작성하는 스타일이 달라서 협업하는 것은 정말 까다로운 것 같다. 그 점들만 잘 맞춰 나간다면 서로 배우는것도 많고 좋은 것 같다.



