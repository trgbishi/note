1. 查询rp
show retention policies
2. 查询cq
show continuous queries
3. 修改默认rp
create database crawl 
create database crawl_1h 
create database crawl_1d 
alter retention policy autogen on crawl duration 30d replication 1 default
crawl_1h与crawl_1d为默认永久存储
4. 创建cq
从数据库crawl查询所有数据，存储到crawl_1h，每小时查一次
CREATE CONTINUOUS QUERY "cq_crawl_1h" ON "crawl" BEGIN   SELECT mean(*) INTO "crawl_1h"."autogen".:MEASUREMENT FROM /.*/ GROUP BY time(1h),* END
从数据库crawl_1h查询所有数据，存储到crawl_1d，每天查一次
CREATE CONTINUOUS QUERY "cq_crawl_1d" ON "crawl_1h" BEGIN   SELECT mean(*) INTO "crawl_1d"."autogen".:MEASUREMENT FROM /.*/ GROUP BY time(1d),* END