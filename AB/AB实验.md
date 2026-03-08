# AB实验

## 1 业务对接&问题拆解
## 2 实验设计
- 策略设计
   - 策略是否能达到理想效果
   - 确定*处理(treatment)*，可能为多个不同的处理
- 实验变量($X$)以及实验指标(parameters)
   - 实验变量以及指标会被用来构建假设
   - 护栏指标
      - 护栏指标通常为处理(treatment)可能影响的指标，并且不希望处理对此类指标产生某种类型的影响
   - 卫星指标/过程指标
      - 用来更好的理解处理带来的效果

### 2.1 假设检验 
见[hypothesis testing](../statistics/statistical_inference.md#hypothesis-testing)

#### 3.1 确定先决条件
- 基于$X$以及实验指标确定假设($H_0, H_a$)
- 确定最小可探测效应(Minimal Detetable Effect) ($MDE$)
   - 通常需要与业务共同决定
- 确定显著性水平 ($\alpha$)
- 确定统计功效(Power of Test) ($1-\beta$)
- 基于假设推导统计检验量(Test Statistic)
   - 这里统计检验量为随机变量($T$), 而根据数据计算出的统计检验量为常数($t_obs$)

#### 3.2 构建数据集
##### 3.2.1 最小样本量
##### 3.2.2 抽样/分流

#### 3.3 实验上线/停止条件

##### AA 实验

##### 实验运行时间
- 累计最小样本量所需时间
- 周期效应
- 新奇效应


### 3 实验分析

#### 3.1 决策方法
- 临界值方法
   1. 根据 $\alpha$ 和假设从 $H_0$ 下的 $T$ 分布计算临界值 $c_\alpha$
   2. 若 $t_{obs}$ 落在拒绝域内，则拒绝 $H_0$
   - **无需计算 p 值**
- P 值方法
   1. 根据假设从 $H_0$ 下的 $T$ 分布计算 p 值 $p$
   2. 若 $p \lt \alpha$，则拒绝 $H_0$
   - **无需使用临界值**
  
#### 3.2 多重检验问题&修正方法 (Multiple Testing & Corrections)
多重检验
Bonferroni correction
False Discovery Rate (FDR)
Family-wise error rate (FWER)

#### 3.3 CUPED (Controlled Using Pre-Experiment Data)

---

## 常见问题


