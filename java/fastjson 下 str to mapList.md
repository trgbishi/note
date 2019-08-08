```java
    List<Map> mapList;
    try {
            mapList = JSONObject.parseArray(resp, Map.class);
    } catch (JSONException e) {
        System.out.println("resp cannot cast to json");
        return;
    }
```