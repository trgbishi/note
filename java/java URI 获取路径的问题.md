>仅将完整的URL地址做构造参数，实例化URI对象后,URL对象获取的路径不完整

测试代码：
```java
    public static void main(String[] args) throws URISyntaxException {
        URI uri = new URI("http://127.0.0.1/test?test");
        System.out.println("uri " + uri);
        System.out.println("uri.getRawPath " + uri.getRawPath());
        System.out.println("uri.getPath " + uri.getPath());
    }
```    

测试结果：
* uri -> http://127.0.0.1/test?test
* uri.getRawPath -> /test
* uri.getPath -> /test
    