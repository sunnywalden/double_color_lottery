# double color lottery
 
## 依赖

Python version: 3.7

Flask version: 1.0.2

uWSGI version: 2.0.18

app name: lottery

## 描述

双色球彩票生成器



## 部署

### Docker

镜像地址： https://cloud.docker.com/repository/docker/sunnywalden/shuangse-lottery

获取镜像: docker pull sunnywalden/shuangse-lottery:latest

创建容器：
	
	docker run --name lottery -p 8080:8080 -itd sunnywalden/shuangse-lottery:latest /bin/bash
	
## 使用

接口类型： GET

接口地址： /lottery/api/v1/doublecolor

实例：

```

curl http://127.0.0.1:8080/lottery/api/v1/doublecolor/1
```

返回：

```

{"lotteries":[[2,4,5,15,21,32,15]],"msg":"","status":"success"}

```
