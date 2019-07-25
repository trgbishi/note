http 的post与get方法都是用于请求与获得响应
	resp = await self.session.post(self.url, data = str(msg))
用一个post就可以完成一次请求与响应
单独再起一个get来获取响应是获取不到post的响应的