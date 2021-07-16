# Config

> Git과 관련된 설정

* global 설정을 기준으로 하나 git 저장소 단위의 local 설정도 가능
  * global의 경우 홈 디렉토리(`~`)의 `.gitconfig` 에 기록
  * local의 경우 해당 git 저장소의 `.gitconfig` 에 기록

## config 확인하기

```bash
$ git config --global -l
```

## author

> author 설정이 없으면, 커밋이 되지 않음
>
> Github에서는 기본적으로 author로 설정된 이메일을 바탕으로 커밋 작성자를 파악
>
> 로그인과는 전혀 상관 없음!

```bash
$ git config --global user.name ''
$ git config --global user.email ''
```

## 기본 편집기 설정

> 기본 편집기가 vim으로 설정되어 있는데 이를 VS code로 변경하여 VS code 창을 저장하고 닫으면 커밋 메시지 등을 편집할 수 있도록

 ```bash
 $ git config --global core.editor "code --wait"
 ```

