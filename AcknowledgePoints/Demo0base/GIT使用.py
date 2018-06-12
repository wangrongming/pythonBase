##GIT使用
sudo apt-get install git
Debian或Ubuntu Linux，要把命令改为sudo apt-get install git-core

#设置当前用户
git config --global user.name "mingming"
git config --global user.email "1768389896@qq.com"
#创建一个git仓库
mkdir learngit
#初始化git目录
git init
#添加文件
git add readme.txt
#git commit 
git commit -m "just for test"

git status#掌握git仓库的状态

git status#查看git仓库修改内容

git log#查看提交日志
git log --pretty=oneline#输出日志更精简

git reset --hard 版本号#回退到某一个版本

git reflog#记录每一次的版本操作

#命令可以查看工作区和版本库里面最新版本的区别
git diff HEAD -- test.py 

#将工作区的内容回归到最近一次的git commit或git add状态
git checkout -- readme.txt  ##  -- 很重要要带上（恢复工作区的修改或者删除）

#可以把暂存区的修改撤销掉（unstage），重新放回工作区
git reset HEAD file

#将工作区的删除添加到 暂存区git commit后，分支中文件被删除
git rm

#github远程仓库设置
#本地linux环境配置ssh登录
ssh-keygen -t rsa -C "1768389896@qq.com"
#本地仓库内容推送到git里面
sudo git remote add origin git@github.com:wangrongming/mygit.git
sudo git remote add origin https://github.com/wangrongming/mygit.git
git push origin master#推送修改内容
git push -u origin master#推送所有内容

#将远程库克隆到本地
sudo git clone https://github.com/wangrongming/Flask.git

#分支管理
git checkout -b dev （创建并切换分支）<==> git branch dev（创建分支）,git checkout dev（切换到分支）
查看分支：git branch
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name>
删除分支：git branch -d <name>
#强行覆盖远程内容进行提交
git push -f origin master

？？除了克隆之外如何将远程内容添加到本地


#收藏现在的工作空间
git stash
#git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除；
#git stash pop，恢复的同时把stash内容也删了：
git stash pop<==>git stash apply,git stash drop
#删除分支
git branch -d feature-vulcan #普通删除分支
git branch -D feature-vulcan #强行删除分支

#git多人协作
查看远程库信息，使用git remote -v；

本地新建的分支如果不推送到远程，对其他人就是不可见的；

从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。

#git tag <name>就可以打一个新标签
git tag #查看所有标签
git tag v0.9 6224937 #给过去的某个版本打标签
git show <tagname>#看到标签的说明文字
git tag -d v0.1#删除标签
git push origin --tags#一次性推送全部尚未推送到远程的本地标签
git push origin v1.0#推送某个标签到远程


#git存储流程：工作区-->暂存取-->git存储分支
#git commit只会提交add内容，工作区内容不会提交


windows客户端使用：
    git2.9.4
    tortoiseGit2.5 64
    
