# svn_counter

###LICENSE

```
The MIT License (MIT)

Copyright (c) 2016 曹建峰

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Functions:

Analysis of Subversion source repositorie

1. Count total line number of your project.
2. Count everybody`s line number of your project.
3. And more.

###BaseOn:[statsvn 0.7](https://sourceforge.net/projects/statsvn/)

###ReferTo:[SVN的可视化日志统计工具StatSVN](http://my.oschina.net/myriads/blog/15665)

###Using:

1. checkout svn project to count
2. cd svn_couter dir and call ./svn_counter.py YOUR_PROJECT_PATH
	 
		./svn_counter.py YOUR_PROJECT_PATH
	 
3. open ./output_YOUR_PROJECT_PATH/index.html


------

### 功能：

分享svn代码库：

1. 统计总代码行
2. 统计每个人的代码占比
3. 等等

###基于：[statsvn 0.7](https://sourceforge.net/projects/statsvn/)

###参考：[SVN的可视化日志统计工具StatSVN](http://my.oschina.net/myriads/blog/15665)

###使用说明:

1. 检出一份待统计的工程代码
2. 进入svn_couter 目录并调用svn_counter.py	
	 
		./svn_counter.py YOUR_PROJECT_PATH
	 
3. 打开 ./output_YOUR_PROJECT_PATH/index.html
