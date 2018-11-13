
[![Travis (.org)](https://img.shields.io/travis/zaixi/GouYong.svg)](https://github.com/zaixi/GouYong)
[![PyPI](https://img.shields.io/pypi/v/GouYong.svg)](https://pypi.org/project/GouYong/)

## 这是一个Linux词典应用程序，目标够用就好！

#### 欢迎大家一起改进开发，让够用越来越够用，用起来越来越舒服。 
*(在线翻译资源来自互联网，版权属于相关网站)*

### 图例:
##### 在线:
![image](https://cloud.githubusercontent.com/assets/1257256/5561516/1dff5d2a-8e19-11e4-9c18-17815259948d.png)
##### 离线:
![image](https://cloud.githubusercontent.com/assets/1257256/5561515/1dfd28c0-8e19-11e4-8352-67c54a2540c9.png)

### 安装和使用
只支持python3及以上
`pip install GouYong`
启动
命令行运行`GouYong`
翻译
鼠标选中后按连按左ctrl两次
查询翻译
鼠标选中后按连按右ctrl两次,将从cht.sh查询并翻译

### Features:
1. 结合ButtonRelease和owner-change实现了X window下的最优取词机制，避免了像stardict一样不能再次取同一个词，和像openyoudao一样影响复制且影响其他程序对剪贴板的使用。
2. 托盘可以暂停取词，还可以切换离线，在线模式。
3. 自动调整弹出窗口的位置，鼠标远离窗口一定范围时窗口自动关闭。
4. 更改划词翻译触发机制为连按左ctrl两次。
5. 支持段落翻译。
6. 增加连按右ctrl两次通过cht.sh查询并翻译。
7. 增加翻译引擎选择,目前支持谷歌搜狗有道。
8. 增加travis自动上传到pypi。
9. 由python2改为python3。

### TODO:
- [X] 支持谷歌搜狗翻译;
- [X] 支持段落翻译;
- [X] 通过cht.sh查询;
- [X] 顺畅自如的选词弹窗翻译;
- [ ] 简洁的操作，酷炫的UI;
- [X] 离线词典;
- [ ] OCR图像取词翻译;
- [ ] 性能优化;
- [X] 打包,软件源部署.
 
 

### 依赖:  
1. python-gi 3.12  
2. python-xlib  
3. gir1.2-appindicator3-0.1  
4. gir1.2-webkit-3.0  
5. python-marisa-trie  


### 进度:    
1. 选词翻译基本达成。2014年 08月 25日 星期一 14:58:23 CST    
2. 顺畅选词弹窗网络翻译达成。2014年 08月 31日 星期日 17:29:26 CST    
3. 离线词典使用StarDict词库达成。2014年 09月 03日 星期三 17:10:44 CST   
4. 初步优化性能。2014年 09月 07日 星期日 18:30:23 CST  
5. 简单打包。2014年 09月 07日 星期日 18:30:41 CST  
6. 生成deb包。2014年 09月 10日 星期三 02:54:05 CST  
7. 优化选词机制,可以直接再次选取同一词，不会清空selection影响其他程序。2014年 09月 11日 星期四 19:32:42 CST  

### 打包:
使用fpm，stdeb, setuptools_git等工具。  
