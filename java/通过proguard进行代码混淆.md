## maven插件实现
### 说明
1. 在pom.xml里添加插件
2. 对应目录下proguard.cfg
3. pluginManagement用于子模块继承，子模块声明插件的groupId,artifactId继承。
### pom.xml
```xml
<pluginManagement>
			<plugins>
				<!-- 代码混淆插件 -->
				<plugin>
					<dependencies>
						<dependency>
							<groupId>net.sf.proguard</groupId>
							<artifactId>proguard-base</artifactId>
							<!-- 2019年7月15日    jdk1.8  兼容性还可以 -->
							<version>6.0.2</version>
							<scope>runtime</scope>
						</dependency>
					</dependencies>
					<groupId>com.github.wvengen</groupId>
					<artifactId>proguard-maven-plugin</artifactId>
					<version>2.0.14</version>
					<executions>
						<execution>
							<!-- 混淆时刻，这里是打包的时候混淆 -->
							<phase>package</phase>
							<goals>
								<!-- 使用插件的什么功能，当然是混淆 -->
								<goal>proguard</goal>
							</goals>
						</execution>
					</executions>
					<configuration>
						<!-- 是否将生成的PG文件安装部署 -->
						<attach>true</attach>
						<attachArtifactClassifier>pg</attachArtifactClassifier>
                        <!-- 指定需要混淆的jar包 -->
						<injar>${project.artifactId}-${project.version}-${maven.build.timestamp}.jar</injar>
						<!-- 是否混淆 -->
						<obfuscate>true</obfuscate>
                        <!-- 配置文件 -->
						<proguardInclude>proguard.cfg</proguardInclude>
					</configuration>
				</plugin>
			</plugins>
</pluginManagement>
```
### proguacd.cfg
```conf
#声明jdk路径，必需
-libraryjars <java.home>\lib\

# JDK目标版本1.8
-target 1.8

#解决找不到配置文件路径的问题
-keepdirectories

# 不做收缩（删除注释、未被引用代码）
#理论上xml配置文件引用的类都被保留，不会遗漏有用却被删除的代码
#-dontshrink

# 不做优化（变更代码实现逻辑）
#优化后会出现不明报错，我认为优化算法不够完善
-dontoptimize

# 解决netty引发的报错，引发原因不明
-keepattributes Signature,InnerClasses,*Annotation*

#加上dontwarn后会使某些情况下的混淆失败 变成 成功
-dontwarn **
#主要是为了少些日志输出，节省时间
-dontnote

# 不混淆main方法，因为main是程序入口
-keep class main.Main {
public static void main(java.lang.String[]);
}

# 指定混淆的路径，即本项目模块路径
-keep class !com.xxx.**,!com.xx.** {*;}
-keep interface !com.xxx.**,!com.xx.** {*;}

# 指定保留的类，主要是配置文件里引用的类
#1.有属性的要加 <fields>;void set*(***);
#2.配置文件里有方法引用的，需要保留该方法声明
-keep class com.xxxx.** {<fields>;void set*(***);}

#保留model
-keep class com.xx.model.** {*;}

#不区分大小写，即同一个目录下不会同时存在A与a
-dontusemixedcaseclassnames
```
