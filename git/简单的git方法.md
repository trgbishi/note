###基本操作
    cd 工程目录
    git config --global user.name "trgbishi"
    git config --global user.email "trgbishi@yeah.net "
    git init 
    touch README.md	//第一次提交，先不要在git上建README.md，在本地建然后先提交。
    git add README.md  //把文件添加到版本库
    git commit -m "注释"  //把文件添加到本地仓库
    git remote add origin https://git.oschina.net/trgbishi/******.git 
    git push -u origin master 

以上是初始化
之后就可以
    git add *
    git commit －m "如果需要就注释"
    git push -u origin master

###高级操作
1.丢弃工作区已修改但未提交的文件的修改
	git checkout -- [filename]
2.丢弃工作区所有已修改但未提交的文件的修改
	git checkout .

3.撤销git add到暂存区的文件的修改
	git reset head [filename]
撤销完修改的文件会回到工作区

4.版本回退
	git log 查询具体的修改的hashcode
	git reset --hard [hashcode]
    
5.以远程分支为源创建新的本地分支，并上传
    git checkout develop //进入develop分支
    git checkout -b develop_1.0 //以develop为源创建本地分支develop_1
    git push origin develop_1.0 //将本地develop_1分支作为远程develop_1分支




2017年08月22日