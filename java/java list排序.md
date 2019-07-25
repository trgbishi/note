###先用第一种排序方式，编译器提示我可以用lambda简化
    Collections.sort(viMetrics, new Comparator<MetricBean>() {
        public int compare(MetricBean metricBean0, MetricBean metricBean1){
            return metricBean0.getMatchtype().compareTo(metricBean1.getMatchtype());
        }
    });
###lambda简化后，编译器提示我可以用Comparator.comparing代替中间的比较长串
    viMetrics.sort((MetricBean metricBean0, MetricBean metricBean1)->metricBean0.getMatchtype().compareTo(metricBean1.getMatchtype()));

###然后就出来了这样一行代码
    viMetrics.sort(Comparator.comparing(MetricBean::getMatchtype));
        
第三种方式最好记