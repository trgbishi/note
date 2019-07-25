    #用json = msg传json格式，会给"加转义字符成\"，从而与content-length不符，server无法解析
    #比如{}内带10个 " ,就会自动加10个 \ ，content-length+10,但是对方解析数据时，是看不见 \ 的，因此得到的数据和长度不符，无法解析
    #content-length是自动设置的，没找到手动接口
    await self.session.post(self.url, data = str(msg))#选择直接传递str，不用考虑转化的问题
    await self.session.post(self.url, json = msg)#没有解决