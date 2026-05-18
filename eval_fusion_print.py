import numpy as np
import os


metrics = ['r2', 'r', 'rmse', 'urmse', 'bias', 'KGE']

obs_names = ['colm', 'era5', 'smci']
pred_names = ['colm', 'era5', 'smci','stage2_colm','stage2_era5','stage2_smci','ablationA_era5','ablationA_colm','ablationA_smci','ablationB_era5','ablationB_colm','ablationB_smci','ablationC_era5','ablationC_colm','ablationC_smci','ablationD_era5','ablationD_colm','ablationD_smci','ablationE_era5','ablationE_colm','ablationE_smci']


def summarize_metrics(obs, pred, metric_list=metrics, days=7):

    print(f"\nMetrics for obs_{obs} vs pred_{pred}:")
    header = "Day\t" + "\t".join(metric.upper() for metric in metric_list)
    print(header)


    for day in range(1, days + 1):
        row = f"{day}\t"
        for metric in metric_list:
            filename = f"{metric}_{obs}_{pred}.npy"
            if not os.path.exists(filename):
                row += "NA\t"
                continue
            data = np.load(filename)  #(lat, lon, day_index)

            day_data = data[:, :, day - 1]  

            mean_val = np.nanmedian(day_data)
            row += f"{mean_val:.4f}\t"
        print(row)


def main():
    for obs in obs_names:
        for pred in pred_names:
            summarize_metrics(obs, pred, days=7)


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     main()
