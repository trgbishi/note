仅删除远程分支文件，不修改本地文件；执行完成后，再修改或删除本地的文件时，不再提示变更，merge也不会再报冲突
git rm --cached -r .idea
git add .
git commit -m "git rm idea"
git push