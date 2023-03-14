# 가상환경 설정
```bash
# 파이썬이 모듈 중에, `venv`모듈을 써서 venv 라는 이름의 폴더에 가상환경을 만들어줘
# python -m venv { forder_name }
$ python -m venv venv
```
- 현재 진행할 프로젝트에서 사용할 환경을 구성하기 위해 만든다.
- 다른 환경, 혹은 해당 프로젝트를 실행하기 위해 필요한 모듈, 패키지, 등등을 관리하기 위함이다.

2. 가상 환경 실행
```bash
$ source venv/Scripts/activate #(window)
```

3. pip freeze
- 현재 pip가 관리중인 패키지의 버전을 포함한 내용을 txt로 작성
```bash
$ pip freeze > requirements.txt
```

4. pip install -r requirements.txt
- requirements.txt 에 작성해 둔, 패키지 목록을 모두 읽어서 설치
```bash
$ pip install -r requirements.txt
```





# git ignore
gitignore.io 사이트에서 언어 및 프로그램 선택 후 생성
-> 생성된 text 파일을 ctrl+a ctrl+c 해서 .git 있는 최상위 폴더로 가기
-> vscode 열어 새파일 만들어 .gitignore 만들어 ctrl+v
- 가상환경이 여러개 만들 때
만약 myenv 가상환경을 만들면 gitignore 열어서 여기에 myenv/도 작성
- 가상환경이 만들어 진 후부터
.gitignore에 있는 목록들은 git으로 관리하지 않게 됨
중요 ! 시점은 파일이 추가가 된 이후부터 !!

아닌 경우 : 만약 01_python 폴더의 db는 git에 올려야한다 근데 05_django db는 개인정보라서 올리면 안된다 그 떄는 그 폴더 안에서 gitignore 상대경로 작성해서 새로 작성해야함

1프로젝트 1가상환경


# forth_pjt 만들기 / pages / index