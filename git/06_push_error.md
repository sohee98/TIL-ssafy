# Push 오류

```bash
$ git push origin master
To https://lab.ssafy.com/yyyyy01179/test.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://lab.ssafy.com/yyyyy01179/test.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

* 원격저장소랑 로컬저장소 커밋 로그가 다른 경우
  * 원격저장소를 지원하는 곳에서 직접 수정한 경우 (Github/Gitlab)
  * 혹은 저장소 만들 때, README랑 같이 만들기 이런 옵션 클릭했을 때
  * => 원격저장소에서는 파일만 만들어주지 않아요. 왜냐? 버전관리시스템이다! Git은.. 그래서 Github/Gitlab 저장소에서 보이는 모든 파일은 단순히 특정 시점의 파일 구조인 것이고 실제로는 `버전`이 기록 되어 있다.
  
* 해결 하기

  * 원격 저장소 버전 가져오기

    ```bash
    $ git pull origin master
    ```

  * Merge commit

    * 두 버전을 합치는 커밋 
      * 일반적으로 충돌이 없으면 vs code창이 열리고(커밋메시지) 저장하고 종료하면 됨
      * 동일 파일이 수정되어 있으면 충돌 발생
        * 충돌난 파일 확인해서 수정하고 `add`, `commit` 

  * 원격저장소에 올리기

    ```bash
    $ git push origin master
    ```

    

