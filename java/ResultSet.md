    ResultSet rs = pstm.executeQuery();

    ResultSet表面看起来是一个结果集，但是其中并没有值。只有当通过next方法并getXXX提取字段内容的时候，才会从数据库中取值
    这也解释了为什么Connection close时，rs就无法取到值了

    另外，rs.getxxxx取的是列值，当rs.next会定位到具体行，用rs.getxxx定位到该行的具体列
