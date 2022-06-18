import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

def AnomalyData(epsilon, minsamples, nocluster):
    driver = pd.read_csv('main/data/go_track_tracks.csv')

    driver_x = driver.drop(["id","id_android","time","rating","rating_bus","rating_weather","car_or_bus","linha"],axis=1) 
    
    x_array = np.array(driver_x)
    
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(x_array)
    
    db = DBSCAN(eps=epsilon, min_samples=minsamples)
    db.fit(x_scaled)
    
    labels = db.labels_
    n_raw = len(labels)
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print("Terdapat " + str(n_clusters_) + " cluster yang terbentuk")

    pd.array = []
    for i in range(0, n_raw):
        if(db.labels_[i] == nocluster):
            a = "id record: " + str(driver.values[i,0]) + ", id android: " + str(driver.values[i,1]) + ", Cluster: " + str(db.labels_[i])
            pd.array.append(a)
            b = "--------------------------------------------------------------"
            pd.array.append(b)
    
    return pd.array
    