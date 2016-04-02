#学生信息整理：
##第一步：在OS2016spring 上获取edx导出的学生信息
并查看是否有Email重复：
```
awk '{if(!a[$3]) a[$3]=1; else print $3}' student_info-20160319
```
##第二步：下载学生名单，为Excel文件，将其内容拷至文本文件，并将tab分割符换为space
```
sed 's/\t/ /g' < student_list > output
```
##第三步：用combine.go 的代码合并三个文件
注意这里的要将第一步的edx信息文件重命名为“a”，学生名单得出的文本文件为“b”和“c”。输出为标准输出，需要重定向到output.txt文件
```
go run combine.go > output.txt   
```
输出的学生信息在学生名单的后面添加了S 的账户信息。  

#代码下载（deprecated)：
##获得所有项目地址和学生帐号：  
1. 首先要用VPN 连接至内网，此不多述。
2. 参考Reference 1的内容，获得自己的cookies,并存在此目录下，命名为cookies.txt
3. 用teacher帐号登陆gitlab，并将首页的源代码下载下来存作html.txt。  
4. 用html.py分析该源代码，得到输出为账户名称项目名称和对应的地址，重定向至download.txt中。
5. 注意，html.py依赖于html.txt一个文件
```
./html.py > download.txt
```

##拉取文件
不对学生的不同账户做区分，全部拉取下来。
1. 参照Reference 1，将Cookies.txt设置好。
2. 使用download.py 将所有的项目下载并解压到指定位置。
3. 注意，download依赖于account.txt err.log 和cookies三个文件。
如果download过程中出现了错误，将会被记录在err.log 中，根据错误记录可以选择性的人工重做。

#代码下载(git clone 后台版)  
(deprecated)~~ 1. 在后台git文件夹下执行ls * > ls.log  ~~
~~ 2. 手动删除一些不用的文件夹如 tmp teacher   ~~
~~ 3. 通过ls.py 文件生成代码库文件：repo.txt ,ls.py依赖于ls.log文件。 ~~
~~ ```  ~~
~~ ./ls.py > repo.txt ~~
~~ ```  ～～(deprecated))    

1. 登陆gitlab服务器
2. 因为网络不稳定，最好使用tmux。tmux attach-session -t grade
2. 进入grade文件夹
3. 在server端通过download.py文件下载代码库，该文件依赖于download.txt文件。

```
./download.py
```

#评分
1. 将lab中的tools/grade.sh文件复制在workdir下。
2. 修改grade.sh文件，对lab变量和gradesh变量修改为对应的lab和之前拷贝的grade.sh文件。
3. 进入container
3. 执行grade.sh文件。该文件依赖于grade.sh文件并生成summary.txt和log.txt文件。
4. 将summary.txt 文件和finallist学生名单用stat.sh合并，生成成绩文件。该命令依赖于summary.txt和finallist文件，并生成score.txt文件
```
sudo docker start -i -a gradecontainer
```


```
./stat.py > score.txt
```

#Clean.sh
使用Clean.sh可以清除当前目录下所有的文件夹。
恭喜你通关了。

##Reference:
[1]. http://askubuntu.com/questions/161778/how-do-i-use-wget-curl-to-download-from-a-site-i-am-logged-into
