## 第一种方案
```java
    Set<String> set = new HashSet<>();
    set.add("aa");
    sout(set.iterator.next());
``` 
## 第二种方案
```java
    Set<String> set = new HashSet<>();
    set.add("aa");
    System.out.println(new ArrayList<>(set).get(0));
```