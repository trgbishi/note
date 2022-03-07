package org.example;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

/***
* @Description 资料来自于https://blog.csdn.net/dwj901125/article/details/9176747
* @Description 将原代码中单次替换单个字符改成了扫描替换多个
* @InitDate 18:43 2022/3/7
* @Version 1.0
**/
public class TextReplace {
	
	public static void main(String[] args) {
		String filePath = "C:\\Users\\kdgz\\Downloads\\cc"; //给我你要读取的文件夹路径
		File outPath = new File("C:\\Users\\kdgz\\Downloads\\out"); //随便给一个输出文件夹的路径(不存在也可以)
		readFolder(filePath,outPath);
	}
	
	public static void readFolder(String filePath,File outPath){
		try {
			//读取指定文件夹下的所有文件
			File file = new File(filePath);
			if (!file.isDirectory()) {
				System.out.println("---------- 该文件不是一个目录文件 ----------");
			} else if (file.isDirectory()) {
				System.out.println("---------- 很好，这是一个目录文件夹 ----------");
				String[] filelist = file.list();
				for (int i = 0; i < filelist.length; i++) {
					File readfile = new File(filePath + "\\" + filelist[i]);
					//String path = readfile.getPath();//文件路径
					String absolutepath = readfile.getAbsolutePath();//文件的绝对路径
					String filename = readfile.getName();//读到的文件名
					readFile(absolutepath,filename,i,outPath);//调用 readFile 方法读取文件夹下所有文件
				}
				System.out.println("---------- 所有文件操作完毕 ----------");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static Map<String,String> map = new HashMap<String, String>(){{
		put("<type>STR_REPLACE</type>","<type>25</type>");
		put("<type>REGEX</type>","<type>5</type>");
	}};
	
	public static void readFile(String absolutepath,String filename,int index,File outPath){
		try{
			BufferedReader bufReader = new BufferedReader(new InputStreamReader(new FileInputStream(absolutepath)));//数据流读取文件
			StringBuffer strBuffer = new StringBuffer();
			for (String temp = null; (temp = bufReader.readLine()) != null; temp = null) {
				for(Map.Entry<String,String> entry:map.entrySet()){
					String oldStr = entry.getKey();
					String newStr = entry.getValue();
					if(temp.contains(oldStr)){
						temp = temp.replace(oldStr, newStr);
						continue;
					}
				}
				strBuffer.append(temp);
				strBuffer.append(System.getProperty("line.separator"));//行与行之间的分割

			}
			bufReader.close();
			if(outPath.exists() == false){ //检查输出文件夹是否存在，若不存在先创建
				outPath.mkdirs();
				System.out.println("已成功创建输出文件夹：" + outPath);
			}
			PrintWriter printWriter = new PrintWriter(outPath+"\\"+filename);//替换后输出的文件位置（切记这里的E:/ttt 在你的本地必须有这个文件夹）
			printWriter.write(strBuffer.toString().toCharArray());
			printWriter.flush();
			printWriter.close();
			System.out.println("第 " + (index+1) +" 个文件   "+ absolutepath +"  已成功输出到    " +outPath+"\\"+filename);
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}
