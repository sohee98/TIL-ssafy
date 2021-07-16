# 원격 저장소 

## 원격저장소 설정

```bash
$ git remote add origin <url>
```

* 깃아 원격저장소 추가해줘 오리진으로 url을

## 원격저장소 push

> 파일 / 폴더가 아니라 커밋(버전)이 push 되는 것

```bash
$ git push origin master
```

* 깃아 푸시해! 원격저장소 origin master!!
* 만약 로컬저장소와 원격저장소의 커밋 로그가 다른 경우에는 오류가 발생하고, 이 과정에서 pull을 통해 해결해야함

## 원격저장소 pull

> 파일/폴더가 아니라 커밋(버전)이 pull 되는 것

```bash
$ git pull origin master
```

* 원격 저장소의 버전을 받아오는 것
* 만약 로컬저장소와 원격저장소의 커밋 로그가 다른 경우에는 병합이 발생되고, 이 과정에서 충돌 발생 가능

## 원격저장소 조회

```bash
$ git remote -v
```

## 원격저장소 복제

```bash
$ git clone <url>
# 예시
$ git clone https://github.com/asdf/test.git
```

* 외부 Git repository를 통해 프로젝트를 진행하는 경우 활용
* pull과 본질적으로 다름

## push 오류

```bash
$ git push origin master
To https://github.com/edutak/TIL-gj.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/edutak/TIL-gj.git'

# 변경사항(Updates)가 원격저장소에 있는 것과 로컬이 다름
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

