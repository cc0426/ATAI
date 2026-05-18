import numpy as np
import os

# 定义指标名称和显示格式
metrics = ['r2', 'r', 'rmse', 'urmse', 'bias', 'KGE']
# 标签和预测的名称（应与之前一致）
obs_names = ['colm', 'era5', 'smci']
pred_names = ['colm', 'era5', 'smci','stage2_colm','stage2_era5','stage2_smci','ablationA_era5','ablationA_colm','ablationA_smci','ablationB_era5','ablationB_colm','ablationB_smci','ablationC_era5','ablationC_colm','ablationC_smci','ablationD_era5','ablationD_colm','ablationD_smci','ablationE_era5','ablationE_colm','ablationE_smci']


def summarize_metrics(obs, pred, metric_list=metrics, days=7):
    """
    读取并统计指定观测与预测组合的指标，按天输出平均值。
    """
    print(f"\nMetrics for obs_{obs} vs pred_{pred}:")
    header = "Day\t" + "\t".join(metric.upper() for metric in metric_list)
    print(header)

    # 对每一天（1到days）进行统计
    for day in range(1, days + 1):
        row = f"{day}\t"
        for metric in metric_list:
            filename = f"{metric}_{obs}_{pred}.npy"
            if not os.path.exists(filename):
                row += "NA\t"
                continue
            data = np.load(filename)  # 形状: (lat, lon, day_index)
            # 注意：原代码中第三个维度是预报天数，索引从0开始对应第1天
            day_data = data[:, :, day - 1]  # 取对应天的空间切片
            # 计算平均值（忽略NaN）
            mean_val = np.nanmedian(day_data)
            row += f"{mean_val:.4f}\t"
        print(row)


def main():
    # 可以选择对特定组合统计，或遍历所有组合
    for obs in obs_names:
        for pred in pred_names:
            summarize_metrics(obs, pred, days=7)


if __name__ == "__main__":
    main()
# import numpy as np
# import os
# import matplotlib.pyplot as plt
#
# # 定义指标名称和显示格式（保持原顺序）
# metrics = ['r2', 'r', 'rmse', 'urmse', 'bias', 'KGE']
# # 标签和预测的名称
# obs_names = ['colm', 'era5', 'smci']
# pred_names = ['colm', 'era5', 'smci','stage2_colm','stage2_era5','stage2_smci']
# days = 7
#
# def collect_metrics():
#     """
#     收集所有组合的指标数据，返回一个嵌套字典：
#     results[metric][(obs, pred)] = list of length days (中位数值)
#     """
#     results = {metric: {} for metric in metrics}
#     for obs in obs_names:
#         for pred in pred_names:
#             key = (obs, pred)
#             for metric in metrics:
#                 filename = f"{metric}_{obs}_{pred}.npy"
#                 if not os.path.exists(filename):
#                     # 文件缺失则填充 NaN
#                     results[metric][key] = [np.nan] * days
#                     continue
#                 data = np.load(filename)  # 形状: (lat, lon, day_index)
#                 day_medians = []
#                 for day in range(1, days + 1):
#                     day_data = data[:, :, day - 1]  # 对应天的空间切片
#                     median_val = np.nanmedian(day_data)
#                     day_medians.append(median_val)
#                 results[metric][key] = day_medians
#     return results
#
# def plot_metrics(results):
#     """
#     绘制所有指标的折线图
#     """
#     fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # 2行3列
#     axes = axes.flatten()
#
#     # 为每个组合分配一种颜色（共9种）
#     colors = plt.cm.tab10(np.linspace(0, 1, 9))
#     color_idx = 0
#     linestyles = ['-', '--', '-.', ':']  # 备用线型，但只用颜色区分即可
#
#     # 存储图例句柄和标签
#     legend_handles = []
#     legend_labels = []
#
#     # 对每个指标绘制子图
#     for idx, metric in enumerate(metrics):
#         ax = axes[idx]
#         # 遍历所有观测-预测组合
#         for i, obs in enumerate(obs_names):
#             for j, pred in enumerate(pred_names):
#                 key = (obs, pred)
#                 values = results[metric][key]
#                 # 绘制折线
#                 line, = ax.plot(range(1, days+1), values,
#                                 color=colors[color_idx],
#                                 marker='o', markersize=4,
#                                 label=f'{obs}→{pred}')
#                 color_idx += 1
#                 # 记录第一个子图的图例句柄（所有子图图例相同）
#                 if idx == 0:
#                     legend_handles.append(line)
#                     legend_labels.append(f'{obs}→{pred}')
#         # 设置子图标题和标签
#         ax.set_title(metric.upper())
#         ax.set_xlabel('Day')
#         ax.set_ylabel(metric.upper())
#         ax.grid(True, linestyle='--', alpha=0.6)
#         # 重置颜色索引，确保每个子图颜色一致
#         color_idx = 0
#
#     # 统一图例放在图外
#     fig.legend(legend_handles, legend_labels, loc='lower center',
#                ncol=3, bbox_to_anchor=(0.5, -0.05))
#     plt.tight_layout(rect=[0, 0, 1, 0.95])  # 为图例留出空间
#     plt.savefig('metrics_summary.png', dpi=150, bbox_inches='tight')
#     plt.show()
#
# def main():
#     results = collect_metrics()
#     plot_metrics(results)
#
# if __name__ == "__main__":
#     main()