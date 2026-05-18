import numpy as np

def _rmse(y_true, y_pred):
    predanom = y_pred
    targetanom = y_true
    return np.sqrt(np.nanmean((predanom - targetanom) ** 2))


def _bias(y_true, y_pred):
    bias = np.nanmean(np.abs(y_pred - y_true))
    return bias


def unbiased_rmse(y_true, y_pred):
    predmean = np.nanmean(y_pred)
    targetmean = np.nanmean(y_true)
    predanom = y_pred - predmean
    targetanom = y_true - targetmean
    return np.sqrt(np.nanmean((predanom - targetanom) ** 2))


def GetKGE(Qs, Qo):
    if len(Qs) == len(Qo):
        mask = Qo != 0
        Qo = Qo[mask]
        Qs = Qs[mask]
        QsAve = np.mean(Qs)
        QoAve = np.mean(Qo)
        CC = np.corrcoef(Qo, Qs)[0, 1]
        BR = QsAve / QoAve
        RV = (np.std(Qs) / QsAve) / (np.std(Qo) / QoAve)
        KGE = 1 - np.sqrt((CC - 1) ** 2 + (BR - 1) ** 2 + (RV - 1) ** 2)
        return KGE
    else:
        return np.nan


def r2_score_corrcoef(y_true, y_pred):
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    y_true_clean = y_true[mask]
    y_pred_clean = y_pred[mask]
    if len(y_true_clean) < 2:
        return 0.0
    corr_matrix = np.corrcoef(y_true_clean, y_pred_clean)
    corr = corr_matrix[0, 1]
    return corr ** 2


def cal_metrics(obs, pred, china_mask):
    r2 = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)
    r = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)
    rmse = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)
    KGE = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)
    bias = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)
    urmse = np.full((pred.shape[1], pred.shape[2], pred.shape[3]), np.nan)

    for t in range(pred.shape[3]):  
        for i in range(pred.shape[1]): 
            for j in range(pred.shape[2]):  
                if china_mask[i, j] == 1:
                    obs_vals = obs[:, i, j, t]
                    pred_vals = pred[:, i, j, t]
                    r2[i, j, t] = r2_score_corrcoef(obs_vals, pred_vals)
                    r[i, j, t] = np.corrcoef(obs_vals, pred_vals)[0, 1]
                    rmse[i, j, t] = _rmse(obs_vals, pred_vals)
                    urmse[i, j, t] = unbiased_rmse(obs_vals, pred_vals)
                    bias[i, j, t] = _bias(obs_vals, pred_vals)
                    KGE[i, j, t] = GetKGE(obs_vals, pred_vals)
    return r2, r, rmse, urmse, bias, KGE


def main():

    obs_names = ['colm', 'era5', 'smci']
    pred_names = ['colm', 'era5', 'smci','stage2_colm','stage2_era5','stage2_smci']

    obs_data = {}
    for name in obs_names:
        filename = f'obs_{name}.npy'  
        obs_data[name] = np.load(filename)
        print(f'Loaded {filename}, shape: {obs_data[name].shape}')

    # 加载所有预测数据
    pred_data = {}
    for name in pred_names:
        filename = f'pred_{name}.npy' 
        pred_data[name] = np.load(filename)
        print(f'Loaded {filename}, shape: {pred_data[name].shape}')


    china_mask = np.load('/home/zhangcheng/Soil_Moisture/CML_FD/dataset/mask_Northeast_China.npy')
    print(f'Mask shape: {china_mask.shape}')


    for obs_name in obs_names:
        for pred_name in pred_names:
            print(f'Calculating metrics for obs_{obs_name} vs pred_{pred_name}')
            obs = obs_data[obs_name]
            pred = pred_data[pred_name]

            if obs.shape != pred.shape:
                print(f'Warning: shape mismatch: obs {obs.shape} vs pred {pred.shape}. Skipping.')
                continue
            r2, r, rmse, urmse, bias, KGE = cal_metrics(obs, pred, china_mask)

            np.save(f'./r2_{obs_name}_{pred_name}.npy', r2)
            np.save(f'./r_{obs_name}_{pred_name}.npy', r)
            np.save(f'./rmse_{obs_name}_{pred_name}.npy', rmse)
            np.save(f'./urmse_{obs_name}_{pred_name}.npy', urmse)
            np.save(f'./bias_{obs_name}_{pred_name}.npy', bias)
            np.save(f'./KGE_{obs_name}_{pred_name}.npy', KGE)
            print(f'Saved results for {obs_name} vs {pred_name}')


if __name__ == "__main__":
    main()
