### CLI

* ctrl l : 화면 위로 밀림
* tab : 이름 자동완성



* touch : 새로운 파일 만들기

* start . : 지금 있는 폴더(파일 탐색기) 열기 (== 더블클릭)
* ls : 목록
* ls -a : 모든 목록
* mkdir <dirname> : 폴더 만들기
* cd <dirname> : 지정한 폴더로 이동
* cd .. : 상위로 이동
* rm -r <dirname> : 삭제(영구 삭제)
* rm -rf <dirname> : 강제 삭제



* code . : 현재폴더에서 VS code 열기





### Git

directory => `$ git init` => repository[작업공간/스테이지/저장소]

* 주의

1. Home 폴더(~)에서 초기화 하지 않는다.
2. repo 안에 repo를 만들지 않는다.(이미 `git init`한 폴더 안에서는 또 하지 않는다.)



`$ git config --global user.name <이름>` : 서명에 사용할 이름 설정

`$ git config --global user.email <이메일>` : 서명에 사용할 이메일 설정

> 계정당 한번만 하면 됌



#### 저장소 만들기 

`$ git init`

#### 작업 후 버전기록 
`$ git add`
`$ git commit -m '커밋메시지'`

#### 상태보기 
`$ git status`
`$ git log`

#### 원격저장소 

* 원격저장소를 origin에 저장 : `$ git remote add origin URL`

- 업로드 : `$ git push origin master`















