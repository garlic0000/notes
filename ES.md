## windows下搭建ES

```
https://blog.csdn.net/shaixinxin/article/details/107399645
# Elasticsearch-head  界面 谷歌插件
```

## 使用python调用

使用python调用可以使用requests库，也可以使用elasticsearch库

```
from elasticsearch import Elasticsearch
```

```
https://blog.csdn.net/kent7306/article/details/51211577
https://elasticsearch.cn/article/6178
https://www.cnblogs.com/yfb918/p/10749108.html
https://www.jianshu.com/p/4e412f48e820
https://zhuanlan.zhihu.com/p/122511360
```

ES报错 

```
elasticsearch.exceptions.RequestError: RequestError(400, 'mapper_parsing_exception', 'Root mapping definition has unsupported parameters:  [type_name : {properties={country={index=true, store=true, type=text}, province={index=true, store=true, type=text}, city={index=true, store=true, type=text}}}]')

```

创建的数据为

```
body = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 0
            },
            "mappings": {
                "type_name": {
                    "properties": properties
                }
            }
        }
```

解决方法

```
参考:https://blog.csdn.net/qq_21383435/article/details/109295362
去掉"type_name": {},直接置"properties": 
body = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 0
            },
            "mappings": {
                 "properties": properties
            }
        }
更改后执行结果
{'acknowledged': True, 'shards_acknowledged': True, 'index': 'country_province_city'}
```

原因

```
ES7.x默认不支持指定索引类型，在ES7.x上执行则会报错（？在6.x上执行，则会正常执行）
```

ES报错

```
(400, 'illegal_argument_exception', {'error': {'root_cause': [{'type': 'illegal_argument_exception', 'reason': 'Malformed action/metadata line [1], expected START_OBJECT or END_OBJECT but found [VALUE_STRING]'}], 'type': 'illegal_argument_exception', 'reason': 'Malformed action/metadata line [1], expected START_OBJECT or END_OBJECT but found [VALUE_STRING]'}, 'status': 400})

```

```
https://blog.csdn.net/u010882234/article/details/106047588/
```

```
# 出现错误的代码
index = "xxx"
body = []
for country_province_city in country_province_cities:
    item = {
        "country": country_province_city[0],
        "province": country_province_city[1],
        "city": country_province_city[2]
    }
    body.append(item)
self.es.bulk(index=index, body=body)
# 注意body内部格式 插入数据时 增加 "index"项
# 要么指定 {"index": {'_index': 'xxx', '_type': 'xxx', '_id':'xxx'}}
# 要么不指定 {"index": {}}
# 更改后
body = []
for country_province_city in country_province_cities:
	index = {"index": {}}
    item = {
        "country": country_province_city[0],
        "province": country_province_city[1],
        "city": country_province_city[2]
    }
    body.append(index)
    body.append(item)
```

注意：

在ES界面进行匹配时，使用wildcard进行模糊匹配时，适合英文和单个汉字

ES中的各种查询

```
https://blog.csdn.net/u011066470/article/details/105215413
```

