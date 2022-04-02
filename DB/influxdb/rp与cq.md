1. 查询rp
show retention policies
2. 查询cq
show continuous queries
3. 创建不同的数据库，对数据库建cq
修改默认rp
create database crawl 
create database crawl_1h 
create database crawl_1d 
alter retention policy autogen on crawl duration 30d replication 1 default
crawl_1h与crawl_1d为默认永久存储
创建cq
从数据库crawl查询所有数据，存储到crawl_1h，每小时查一次
CREATE CONTINUOUS QUERY "cq_crawl_1h" ON "crawl" BEGIN   SELECT mean(*) INTO "crawl_1h"."autogen".:MEASUREMENT FROM /.*/ GROUP BY time(1h),* END
从数据库crawl_1h查询所有数据，存储到crawl_1d，每天查一次
CREATE CONTINUOUS QUERY "cq_crawl_1d" ON "crawl_1h" BEGIN   SELECT mean(*) INTO "crawl_1d"."autogen".:MEASUREMENT FROM /.*/ GROUP BY time(1d),* END
4. 对一个数据库建多个rp，对每个rp建cq
create database crawl 
alter retention policy autogen on crawl duration 30d replication 1 default
create retention policy "1h" on "crawl" duration 0s replication 1
create retention policy "24h" on "crawl" duration 0s replication 1
CREATE CONTINUOUS QUERY "cq_crawl_1h" ON "crawl" BEGIN   SELECT mean(*) INTO "crawl"."1h".:MEASUREMENT FROM "crawl"."autogen"./.*/ GROUP BY time(1h),* END
CREATE CONTINUOUS QUERY "cq_crawl_1d" ON "crawl" BEGIN   SELECT mean(*) INTO "crawl"."1d"."autogen".:MEASUREMENT FROM "crawl"."1h"./.*/ GROUP BY time(1d),* END