## 🎉 1014 pair Project

****

![ezgif com-gif-maker](https://user-images.githubusercontent.com/70432152/196039320-6efdbb62-d87a-46a0-888f-01576c129a33.gif)

![2](https://user-images.githubusercontent.com/70432152/196039383-aa898c67-dc55-43b0-9364-670590c84fb6.gif)

## 📗 실습 내용

브랜치 전환과 커밋을 통해 페어 프로그래밍을 진행하였다.

1. 이전 개발 내용을 pull 을 통해 가져 온다.

```python
git pull origin master
```

2. 브랜치를 생성하고 전환 해 준다.

```python
git checkout -b [브랜치명]
```

3. 개발을 진행 한 후 동일한 이름의 원격 저장소에 commit,push를 진행한다.

4. 깃허브 PR을 생성하고 브랜치를  병합해준다.

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-10-16-23-16-27-image.png)

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-10-16-23-16-40-image.png)

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-10-16-23-16-51-image.png)

5. 이전 브랜치는 삭제 해 준다.

![](C:\Users\이주현\AppData\Roaming\marktext\images\2022-10-16-23-17-16-image.png)

6. 메인 브랜치로 전환 후 Pull 을 해준다.

```python
# main 브랜치로 전환
git checkout main

# main 브랜치 Pull
git pull origin main
```

7. 이전 브랜치 삭제

```python
# 토픽 브랜치 삭제
git branch -d [토픽 브랜치명]
```

8. 위와 같은 과정을 반복 해 준다.

`깃 브랜치 명령어는 다음과 같다.`

```python
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치 이름 변경
git branch -m [기존 브랜치명] [변경할 브랜치명]
```

****

- CRUD를 구현한다.

- Staticfiles 활용 및 정적 파일을 다룬다.

- Django Auth를 활용하여 회원을 관리하였다.

- `회원가입`, `로그인`, `회원 목록 조회`, `회원 정보 조회`, `정보 수정`, `로그아웃`, `네비게이션바` , `리뷰 작성 페이지` , `리뷰 조회,수정,삭제 페이지` 를 구현하였다.



## 😢 회고 및 고찰

***

- URLS &rarr; VIEWS &rarr; Templates 순으로 구성하자!

- 개발 환경 설정에서 생각보다 시간을 많이 소비했다. 꼭 필요한 과정인 만큼 다시 한번 점검하자

- Models Form 에서 역시 버벅거렸다. 기능은 구현했지만 이전의 코드를 보며 따라친 수준에 불과한 것 같다. 😢 통 채로 코드를 외우는 것은 의미없는 일이며, 하나하나의 기능을 숙지하고 자유자재로 이용 할 수 있도록 노력하자

- `return render` : 템플릿 페이지에 입력값을 띄워주고 싶을 때

- `return redirect`:  템플릿을 그대로 불러오고 싶을 때 로 생각하자


