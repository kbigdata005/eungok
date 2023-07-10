# markdown 문서 작성

# **명령어**

깃을 시작하기 위해서는 컴퓨터에 반드시 깃을 가지고 있어야 합니다. 설치하지 않았다면 [여기](https://git-scm.com/)로 가서 지시사항들을 따라하면 됩니다.

### **새로운 깃 저장소 초기 설정: Git init**

모든 코드 내용은 저장소 안에 추적됩니다. 깃 저장소를 초기 설정하려면 해당 프로젝트 폴더 안에 이 명령어를 사용하세요. 이것이 .git 폴더를 만들어 줄 것입니다.

```powershell
git init

```

### **Git add**

이 명령어는 하나 또는 모든 변경 파일들을 본 무대 영역으로 더합니다.

어떤 하나의 특정 파일을 올리기 위해서는:

```powershell
git add filename.py

```

신규 또는 수정되거나 삭제된 파일들을 올리기 위해서는:

```
git add -A

```

신규 또는 수정 파일들을 올리기 위해서는:

```
git add .

```

수정 또는 삭제된 파일들을 올리기 위해서는:

```
git add -u

```

### **Git commit**

이 명령어는 버전 이력을 파일 안에 기록합니다. -m이 뜻하는 것은 어떤 커밋 메세지가 뒤따른다는 의미입니다. 이 메세지는 커스텀이며 반드시 이것을 동료에게 알리는 용도로 또는 미래의 스스로에게 무엇이 해당 커밋 안에 더해졌는지 알리기 위해 사용해야 합니다.

```
git commit -m "your text"

```

### **Git status**

이 명령어는 파일들을 초록색과 빨간색으로 리스트해 줄 것입니다. 초록색 파일들은 무대로 올려졌지만 아직 커밋되지 않은 것들입니다. 빨간색으로 표시된 파일들은 무대로 아직 올려지지 않은 것들입니다.

```
git status

```

# **브랜치에 작업하는 것**

### **Git branch branch_name**

이것은 새 브랜치를 생성합니다:

```
git branch branch_name

```

### **Git checkout branch_name**

어떤 브랜치에서 다른 브랜치로 변경하려면:

```
git checkout branch_name

```

### **Git checkout -b branch_name**

새로운 브랜치를 생성하고 그것으로 자동 전환하려면:

```
git checkout -b branch_name

```

이것은 간략하게:

```
git branch branch_name
git checkout branch_name

```

입니다.

### **Git branch**

모든 브랜치를 리스트하고 현재 어떤 브랜치에 있는지 확인하려면:

```
git branch

```

### **Git log**

이 명령어는 현재 브랜치에서 모든 버전 이력을 리스트해줄 것입니다:

```
git log

```

# **Push와 Pull**

### **Git push**

이 명령어는 커밋된 변경점들을 원격 저장소에 보냅니다:

```
git push

```

### **Git pull**

원격 저장소에서 개인 컴퓨터로 변경점들을 가져오려면:

```
git pull

```

더 많은 명령어들과 해당 목록에 대한 상세 설명들을 알고 싶다면 공식 [깃 문서](https://git-scm.com/docs/)를 확인하길 추천합니다.

# **유용한 정보 (Tip & Tricks)**

### **커밋되지 않은 모든 변경점을 보낼 때**

문자 그대로 이 명령어는 커밋되지 않은 모든 변경점을 보냅니다:

```
git reset --hard

```

### **개인 컴퓨터에서는 삭제하지 않고 깃에서만 파일을 삭제**

종종 "git add" 명령어를 사용하면서 추가하지 않고 싶어했던 파일을 더해버릴 수도 있습니다.

"git add"를 사용하는 동안 주의하지 않는다면 커밋하기 원하지 않았던 파일을 더하게 될지도 모릅니다. 파일의 기록 버전(staged version)을 반드시 삭제해야 하고, 그리고나서 파일에 .gitignore를 추가하여 같은 실수를 두번 하는 일을 방지할 수 있습니다:

```
git reset file_name
echo filename >> .gitignore

```

### **커밋 메세지 수정**

커밋 메세지를 수정하는 건 굉장히 쉽습니다:

```
git commit --amend -m "New message"
```