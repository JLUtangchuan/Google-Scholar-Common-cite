# Google Scholar Common cite

**通过谷歌学术查找两篇论文的公共引文**


## 目的

- 想当个缝合怪，所以要找是否有人做过想搞的两个领域结合的工作，于是就写个这个玩玩，提升搜索效率

- 输入两个论文的title，返回共同引用这两篇论文的paper

## 设计

1. 使用selenium进行内容的爬取
2. 比较时加入模糊匹配

Note：需要能访问google的环境

## 配置
1. 下载[Chrome driver](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/)
2. 去Chrome商店下载selenium插件
3. 安装必要的包
4. 配置能访问google的工具😁


## TODO
1. 目前就这一个搜索需求，其他的等用到了再开发
2. 有点蛋疼的是用多了就被google识别为机器，需要自己去进行验证
3. 当一篇论文引用量很大的时候会比较难搞，想加入更细致的搜索

## Eg
![](https://gitee.com/JLUtangchuan/imgbed/raw/master/img/20201024142622.png)