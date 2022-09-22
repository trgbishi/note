## 字段类型
 字段类型举例两种，keyword与text

## keyword类型
无论什么查询方式，keyword都是全匹配，查询条件与被查询的字段，必须是全字段相同才能查询到
## text类型
### term
则查询条件必须匹配text字段分词后中的某一个字段
        如查询条件为aa，字段为aa bb cc，分词为三个[aa,bb,cc]，则能匹配到
### match
则查询条件与text字段都进行分词，存在能匹配上的字段就匹配成功
        如"aa bb cc"与"aa bb dd"
### match_phrase
则查询条件的分词结果必须在text字段分词中都包含，且顺序相同，且连续。phrase是短语，所以要求的是多个词，很好理解
### query_string
则查询条件的分词结果必须在text字段分词中都包含，但顺序不要求，也不要求连续
## 补充
    wildcard是模糊查询，可以加通配符，类似于mysql的like
    prefix是前缀查询，等同于like 'xxx%' 或 wildcard 'xxx*'
    fuzzy没测明白，意思是可以输入不完整的或者错误的内容，去匹配，然后参数里有编辑次数，即编辑多少个字符（增删改）能查询到
    range只针对数值类型，做范围查询
    regexp，正则匹配