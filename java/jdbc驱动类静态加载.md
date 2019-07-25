多线程，不同线程加载不同驱动类时，可能会产生死锁。这个问题出现在并发的数据采集时
用静态加载解决该问题，即只加载一次

    static {
            try {
                Class.forName("oracle.jdbc.driver.OracleDriver");
                Class.forName("com.mysql.cj.jdbc.Driver");
                Class.forName("net.sourceforge.jtds.jdbc.Driver");
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
        }