import numpy as np
import pandas as pd

# 源码逻辑
n_samples = len(df)
n_treatment = sum(df[treatment_col] == 1)
n_control = sum(df[treatment_col] == 0)

# 计算整体转化率
overall_conv_treatment = df[df[treatment_col]==1][outcome_col].mean()
overall_conv_control = df[df[treatment_col]==0][outcome_col].mean()
overall_uplift = overall_conv_treatment - overall_conv_control

# 默认分位数数量（通常为100）
n_quantiles = min(100, n_samples) 

uplift_values = []
random_values = []
for q in np.linspace(0, 1, n_quantiles):
    # 截取前q%样本
    cutoff = int(q * n_samples)
    subset = df.iloc[:cutoff]
    
    # 计算当前分位内的uplift
    if len(subset) > 0:
        conv_t = subset[subset[treatment_col]==1][outcome_col].mean()
        conv_c = subset[subset[treatment_col]==0][outcome_col].mean()
        uplift = (conv_t - conv_c) * cutoff  # 累积效应
    else:
        uplift = 0
    
    uplift_values.append(uplift)
    random_values.append(q * overall_uplift * n_samples)  # 随机模型的线性增长
   
 # 梯形法计算曲线下面积
auuc = np.trapz(uplift_values, dx=1/n_quantiles) - np.trapz(random_values, dx=1/n_quantiles)

# 标准化（可选）
max_possible_area = np.trapz([overall_uplift * n_samples * q for q in np.linspace(0,1,n_quantiles)], dx=1/n_quantiles)
normalized_auuc = auuc / max_possible_area  # 您的0.849734属于此类