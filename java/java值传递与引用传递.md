**先说一下值传递与引用传递的概念**

* 值传递：`基本数据类型`与`基本数据类型的包装类`传值，对形参的修改不会影响实参
* 引用传递：引用类型传引用，形参和实参指向同一个内存地址（即同一个对象），所以对参数的修改会影响到实际的对象

举例：
```java
    import java.util.ArrayList;
    import java.util.List;

	 public class Test {
        public static void main(String args[]) {
            /**
             * 基本数据类型及其包装类的传递均为值传递
             */
            //基本数据类型的值传递示例
            int a = 0;
            changeValue(a,1);
            System.out.println("a="+a);//a=0
            //基本数据类型包装类的值传递示例
            String b = "before";
            changeValue(b,"after");
            System.out.println("b="+b);//b=before
    
            /**
             * 对引用本身的改变，为值传递
             * 如下直接修改了arrry与list本身，并非修改是修改其内部元素
             */
            //引用类型的值传递示例，数组
            int[] arrayInt = {1,2,3};
            changeValue(arrayInt,new int[]{4,5,6});
            System.out.println("arrayInt="+arrayInt[0]+arrayInt[1]+arrayInt[2]);//arrayInt=123
            //引用类型的值示例，list
            List<Integer> listInt = new ArrayList<Integer>(){{add(1);add(2);add(3);}};
            changeValue(listInt,new ArrayList<Integer>(){{add(4);add(5);add(6);}});
            System.out.println(listInt.toString());//[1, 2, 3]
    
    
            /**
             * 对引用内部元素的修改，但是以下array和list传递的参数并非是其本身的引用，
             * 而是传递了具体的值，所以仍为值传递
             */
            //引用类型的值示例：数组内的基本数据类型-int
            int[] arrayInt2 = {1,2,3};
            changeValue(arrayInt2[0],9);
            System.out.println("arrayInt2[0]="+arrayInt2[0]);//arrayInt2[0]=1
            //引用类型的值传递示例：list内的基本数据类型包装类-Integer
            List<Integer> listInt2 = new ArrayList<Integer>(){{add(1);add(2);add(3);}};
            changeValue(listInt.get(0),7);
            System.out.println("listInt2"+listInt2.toString());//listInt2[1, 2, 3]
    
    
            /**
             * 引用类型的引用传递,传递引用然后对引用内部的元素进行修改
             */
            //举例list，对list进行添加
            List<Integer> listInt3 = new ArrayList<Integer>(){{add(1);add(2);add(3);}};
            changeList(listInt3,5);
            System.out.println(listInt3.toString());//[1, 2, 3, 5, 5, 5]
            //举例array，对array内元素进行修改
            int[] arrayInt3 = new int[]{1,2,3};
            changeArray(arrayInt3,5);
            System.out.println("arrayInt3="+arrayInt3[0]+arrayInt3[1]+arrayInt3[2]);//arrayInt3=555
    
        }
        private static void changeValue(Object src,Object des){
            src=des;
        }
    
        private static void changeList(List<Integer> src,int des){
            src.add(des);
            src.add(des);
            src.add(des);
        }
    
        private static void changeArray(int[] src,int des){
            src[0]=des;
            src[1]=des;
            src[2]=des;
    
        }
    }
```

>再举个其它的例子吧

>* 基本数据类型的值传递：我有一块砖头，现在拿给你，你把砖头换成了一个手机，这时候砖头已经不是那个砖头了，这是值传递
>* 引用类型的值传递：我有一个房子，现在把地址给你，然后你顺着地址找到我家，把房子搬走了，在上面留下了一块砖头。我晚上回家的时候就找不到我的房子了，因为你把整个房子都换了，这是值传递
>* 引用类型的引用传递：我有一个房子，现在把地址给你，然后你顺着地址找到我家，住了进去，我晚上回家的时候依然能找到我的房子，只不过多了一个你，这是引用传递