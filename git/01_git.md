# git

> 분산 버전 관리 시스템 (DVCS, Distributed Version Control System)

윈도우 환경에서는 git 설치 및 실행을 위해 git bash를 다운로드 받는다.

## 기본 명령어

### 저장소(repository) 생성

```bash
$ git init
```

* `.git` 폴더가 숨김 폴더로 생성되고, git bash에서는 `(master)` 라고 표기 된다.
  * 저장소 생성시 상위 폴더에 `.git` 저장소가 있지 않은지 확인할 필요가 있다.
    * 예) 바탕화면에 실수로 `git init` 에서 `.git` 이 있는 경우

### 기본 버전 관리 흐름

* git은 저장소 내에 모든 파일의 변경사항을 추적함
* 작업을 완료하고 `add` -> `commit` 을 통해 버전을 기록한다.
  * `working directory` 에서 `add` 명령어를 통해 `staging area` 상태(`staged`)로
  * `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 버전 기록

#### `add`

> `working directory` 에서 `add` 명령어를 통해 `staging area` 상태(`staged`)로
>
> 버전으로 기록할 파일을 모으기 위해 사용

```bash
$ git add a.txt    # 특정 파일
$ git add test/    # 특정 폴더
$ git add .        # 현재 디렉토리 (하위 디렉토리 포함)
```

#### `commit` 

> `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 **버전 기록**

```bash
$ git commit -m '커밋 메시지'
[master ce0578b] 커밋 메시지
 1 file changed, 1 deletion(-)
 delete mode 100644 a.txt
```

* 커밋 메시지는 현재 버전에 대해 알 수 있도록 작성
* 지금까지 커밋을 확인하기 위해서는 `git log` 명령어 사용

### 상태 확인 

#### `status`

> working directory와 staging area의 상태를 확인할 수 있다. 
>
> 특정 파일이 변경되었는지 (추가/수정/삭제), `staged` 상태인지

```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt
```

#### `log`

> 커밋 로그를 확인

```bash
$ git log 
$ git log --oneline # 한줄로 간략히 표기
$ git log -2 # 최근 n개의 로그만 확인
$ git log --oneline -2 # 한줄로 최근 n개만
```







