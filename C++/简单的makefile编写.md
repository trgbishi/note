1.新建文件夹 hello
2.进入hello文件夹
3.创建hello.c
4.在hello.c内写入 int main(int argc, char** argv) { printf("Hello, Linux World!\n"); return 0; }
5.autoscan
6.mv configure.scan configure.in
7.修改configure.in 参考:
    ============================configure.in内容开始=========================================   
    # -*- Autoconf -*-   
    # Process this file with autoconf to produce a configure script.   
    AC_INIT(helloworld.c)   
    AM_INIT_AUTOMAKE(helloworld, 1.0)   
    # Checks for programs.   
    AC_PROG_CC   
    # Checks for libraries.   
    # Checks for header files.   
    # Checks for typedefs, structures, and compiler characteristics.   
    # Checks for library functions.   
    AC_OUTPUT(Makefile)   
    ============================configure.in内容结束=========================================   
8.aclocal autoconf  autoheader
9. ./configure
10. make







 2017年08月22日