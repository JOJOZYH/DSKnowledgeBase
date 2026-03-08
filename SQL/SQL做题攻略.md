## 过程
1. 读题
   1. 理解表格，理解每张表的颗粒度、目的，理解每列
   2. 理解输出表格颗粒度，每列，示例
   3. 阅读要求
      1. 筛选
      2. output table排序
   4. 示例解释
2. 构思
   1. think it through
      - consider inverse engineering
   2. inline comments 草稿
      1. 格式：<每个intermediate table的: 描述/目的>; <重点/注意事项>（觉得会忽略就写）
         - 筛选：条件用"、"隔开
         - 排序：条件用"、"隔开，无表示/"升"/"A"/"a"为升序，"倒"/"D"/"d"为倒序
      2. 如果一表搞定可以不写描述/目的
   3. 画图
3. 写

## 题目标签
- P0. 基础查询题 Basic Retrieval
   - P0.1 条件过滤与 NULL 逻辑 Filtering & NULL logic
   - P0.2 多表取数与口径对齐 Multi-table retrieval & metric definition
- P1. 汇总指标类 Aggregation / KPI
   - P1.1 分组汇总 Grouped aggregation
   - P1.2 条件汇总 Conditional aggregation
   - P1.3 占比/渗透率/转化率 Rates (share/penetration/conversion)
- P2. 选择与排序 Selection / Ranking / Bucketing
   - P2.1 去重选代表行（keep latest/earliest）
   - P2.2 每组 Top1 / TopK 
   - P2.3 第 N 高 / percentiles（可选） 
   - P2.4 排名（含并列） 
   - P2.5 分桶/分位（NTILE / percent_rank 等） 
- P3. 时间序列指标 Time-series metrics
   - P3.1 累计 Running total / cumulative
   - P3.2 滚动窗口 Rolling metrics (moving avg/sum)
   - P3.3 环比/同比 MoM/YoY deltas
- P4. 连续问题 Consecutive / Streak problems
   - P4.1 连续段/连续区间识别 Streak / consecutive runs
   - P4.2 间隙与孤岛 Gaps and Islands（孤岛问题）
   - P4.3 会话切分 Sessionization（按时间间隔切 session；很多时候也是 gaps&islands 思维） 
- P5. 用户旅程类 User Journey Analytics
   - P5.1 漏斗 Funnel analysis
   - P5.2 留存/队列 Cohort & retention
   - P5.3 首次/最近一次/复购 First/last repeat purchase, returning user
- P6. 配对/匹配/对比 Pairing & Matching
   - P6.1 “找一对”事件（前后行为、买了 A 又买 B）Pairs of events/items
   - P6.2 同表对比（相邻行/上一笔/下一笔）Row-to-row comparisons
- P7. 区间与有效期 Interval / Validity
   - P7.1 区间重叠/覆盖 Interval overlap/coverage
   - P7.2 有效期匹配（SCD/价格生效区间）As-of / effective-dated joins
- P8. 层级与递归 Hierarchy / Recursion
   - P8.1 树/组织架构 Hierarchy traversal
   - P8.2 路径/层级展开 Path enumeration
- P9. 数据形状变换 Reshaping
   - P9.1 透视/逆透视 Pivot/Unpivot
   - P9.2 拼接展示（行转字符串列表）String/list aggregation

## 解法标签 & 坑点
1. T1. 过滤与表达式 Filtering & Expressions
   1. WHERE/HAVING、CASE WHEN、NULL 处理（COALESCE/IFNULL）、类型转换
2. T2. 连接技巧 Joins
   1. INNER/LEFT/RIGHT/FULL（视方言）
   2. 非等值连接 non-equi join（范围匹配）
   3. 半连接/反连接 EXISTS / NOT EXISTS（semi/anti join）
   4. 自连接 self-join（配对、留存、相邻对比等）
3. T3. 聚合技巧 Aggregation
   1. GROUP BY
   2. 条件聚合 conditional aggregation
   3. DISTINCT 聚合
   4. 分组后过滤 HAVING
4. T4. 子查询与 CTE Subquery & CTE
   1. 派生表 derived table
   2. 相关子查询 correlated subquery
   3. CTE（WITH）
   4. 递归 CTE recursive CTE（层级/序列）
5. T5. 窗口函数 Window functions
   1. 排名：ROW_NUMBER / RANK / DENSE_RANK 
   2. 偏移：LAG / LEAD（相邻行对比、时间序列）
   3. 累计/滚动：SUM/AVG… OVER（running/rolling） 
   4. Frame：ROWS/RANGE（决定滚动窗口边界）
6. T6. 切段/分组标识 Segmenting tricks（常用于连续/孤岛/会话）
   1. value/date - ROW_NUMBER() 差值不变分组
   2. LAG/LEAD 计算断点再累加分组
      -（需要时）日历表/日期维表 calendar table 来补全缺失日期
7. T7. 集合运算 Set operations
   1. UNION / UNION ALL / INTERSECT / EXCEPT（按方言）
8. T8. 日期时间处理 Date/Time
   1. 截断到日/周/月（date truncation）
   2.  生成时间粒度（日期序列/日历表）
   3.  时区/跨年边界处理（坑点）
9.  T9. 形状变换 Reshaping
   1.  Pivot/Unpivot（或 CASE 聚合模拟）
   2.  String aggregation（GROUP_CONCAT/STRING_AGG 等，按方言）
10. T10. 方言增强 Dialect-specific extras（看你面试栈）
   1.  QUALIFY（先算窗口再过滤）
   2.  FILTER（聚合过滤）
   3.  DISTINCT ON / LATERAL / generate_series 等
- K. 边界与坑 Edge Cases（笔试经常卡人）
   1. K1. NULL 与空集聚合（NULL handling, empty set behaviors）
   2. K2. 去重 vs 不去重（DISTINCT placement）
   3. K3. 日期边界（跨月/跨年、时区、月末/周起始）
   4. K4. 重复行/多对多 join 膨胀（join explosion）
   5. K5. 浮点/精度与取整（precision/rounding）
   6. K6. 筛选条件和排序 (WHERE, HAVING, ON, ORDER BY, DESC)
   7. K7. 方言/环境与标识符（Dialect & environment quirks）

## 你可以怎么用它刷题（最有效的套路）
1. 先定主标签：题目关键词命中哪个 P 类（允许 1–2 个）
2. 再挑解法标签：你准备用窗口？聚合？自连接？CTE？
3. 最后扫坑点：尤其是粒度、去重、日期跨年、并列

## 题目模板
1. 题目标签（Problem / 主标签）
2. 解法标签（Method / 技术标签）
3. 坑点标签（Pitfalls / 常见坑）

### 示例
#### 示例1:
1. **题目标签（Problem / 主标签）**
   1. **P4 连续问题 Consecutive / Streak problems**
      1. P4.1 连续段/连续区间识别（streak）：求“最长连续登录天数”
      2. P4.2 间隙与孤岛（Gaps and Islands）：把连续日期切成一个个“岛”，再取岛长度最大值
   2.**P1 汇总指标类 Aggregation / KPI**
      1. P1.1 分组汇总：按 user_id 汇总取 max_consec_days 
2. 解法标签（Method / 技术标签）
   1. **T5 窗口函数 Window functions**：RANK/ROW_NUMBER、COUNT(*) OVER (PARTITION BY ...)
   2. **T6 切段/分组标识 Segmenting tricks**：fdate - ROW_NUMBER()（或 fdate - INTERVAL r DAY）差值不变 → 连续段同组
   3. **T3 聚合技巧 Aggregation**：MAX() + GROUP BY user_id 取最长段
   4. **T4 子查询与 CTE**：用 WITH 分层组织中间表
3. 坑点标签（Pitfalls / 常见坑）
   1. **K2 去重 vs 不去重**：如果同一用户同一天可能多行，先 DISTINCT(user_id,fdate) 再做 streak
   2. **K3 日期边界**：明确限定 2023-01-01～2023-01-31（跨月/跨年时尤其要小心） 

#### 示例2:
1. **题目标签（Problem / 主标签）**
   1. **P1 汇总指标类**
      1. P1.2 条件汇总（Conditional aggregation）：输出是 staff_nums 这种全表汇总 KPI，本质就是聚合统计。 
   2. **P9 数据形状变换（Reshaping）**——因为 course 是“多值字段”（逗号分隔），本质上是在做 explode/un-nest
2. **解法标签（Method / 技术标签）**
   1. **T1 过滤与表达式**
   2. **T3 聚合技巧**
3. **坑点标签（Pitfalls / 常见坑）**
   1. **K1 NULL 与空集聚合（NULL handling, empty set behaviors）**
