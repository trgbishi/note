#### 更新到最新
conda update conda

#### 创建虚拟环境
conda create -n python38  python=3.8

#### 进入虚拟环境
conda activate python38

#### 安装指令
conda install ......

#### 查看安装了哪些包
conda list 

#### 查看当前存在哪些虚拟环境
conda env list 

#### 退出虚拟环境
linux:source deactivate
windows:deactivate

#### 删除虚拟环境
conda remove -n env_name --all

#### 删除环境中的某个包
conda remove --name env_name package_name 