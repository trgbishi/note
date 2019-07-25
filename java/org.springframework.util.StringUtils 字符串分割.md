    String test = "";
    String[] splitSpace = StringUtils.split(test, " ");
    System.out.println(splitSpace);//null
    System.out.println(splitSpace==null);//true

    String test = "";
    String[] splitSpace = StringUtils.tokenizeToStringArray(test, " ");
    System.out.println(splitSpace);//[Ljava.lang.String;@17a7cec2
    System.out.println(splitSpace==null);//false