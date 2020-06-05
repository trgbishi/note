**现象**
```
<dependencies>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-netty</artifactId>
      <version>${grpc.version}</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-protobuf</artifactId>
      <version>${grpc.version}</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-stub</artifactId>
      <version>${grpc.version}</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.google.protobuf</groupId>
      <artifactId>protobuf-java</artifactId>
      <version>${protobuf.version}</version>
    </dependency>
  </dependencies>
```
**问题**<br>
运行时报错，classNotFound

**原因**<br>
当maven pom.xml->dependencied->dependency->scope值为provided时，意为注明该依赖包只在编译和测试时使用<br>
所以运行时不会引用到

**拓展：**
* compile<br>
默认scope为compile，表示为当前依赖参与项目的编译、测试和运行阶段，属于强依赖。打包之时，会达到包里去。
* test<br>
该依赖仅仅参与测试相关的内容，包括测试用例的编译和执行，比如定性的Junit。
* runtime<br>
依赖仅参与运行周期中的使用。一般这种类库都是接口与实现相分离的类库，比如JDBC类库，在编译之时仅依赖相关的接口，在具体的运行之时，才需要具体的mysql、oracle等等数据的驱动程序。
此类的驱动都是为runtime的类库。
* provided<br>
该依赖在打包过程中，不需要打进去，这个由运行的环境来提供，比如tomcat或者基础类库等等，事实上，该依赖可以参与编译、测试和运行等周期，与compile等同。区别在于打包阶段进行了exclude操作。
* system<br>
使用上与provided相同，不同之处在于该依赖不从maven仓库中提取，而是从本地文件系统中提取，其会参照systemPath的属性进行提取依赖。
* import<br>
这个是maven2.0.9版本后出的属性，import只能在dependencyManagement的中使用，能解决maven单继承问题，import依赖关系实际上并不参与限制依赖关系的传递性。