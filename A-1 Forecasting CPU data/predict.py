import pandas as pd
import numpy as np
import cPickle
import time
import pyprind
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import Image
#from scipy import polyval, polyfit
import scipy

src_file = "/home/narsi/Documents/CSEE5690_data/VM-CPU-Stats-1-Day.csv"
store_file = file('/home/narsi/Documents/CSEE5690_data/cpu_analysis/cpu_analytics_'+time.strftime("%Y%m%d-%H%M%S")+'.pkl', 'wb')

cpu_data = pd.read_csv(src_file).iloc[::-1]
cpu_freq = np.array(cpu_data['Value'],dtype = np.float32)
E_id_list = cpu_data.Entity.unique()
Entity_list = cpu_data['Entity']
E_select = [0,25,60,110,225,350]

MA = []
bar = pyprind.ProgBar(len(E_id_list), stream=1)
for E_id in E_id_list[E_select]:
    id_list = (len(cpu_data) - np.array(cpu_data[cpu_data['Entity'] == E_id].index.tolist(), dtype=np.int32))-1
    for window in [3, 5, 7, 9, 11, 16, 20, 30]:
        x = np.empty(len(id_list) - window)
        counter = 0
        for i in id_list[window:]:
            X = cpu_freq[i - window:i]
            x[counter] = np.sum(X) * 1.0 / window
            counter += 1

        TS = (np.sum(np.absolute(cpu_freq[id_list[window:]] - x)) / len(x))
        MA.append(window)
        MA.append(cpu_freq[id_list[window:]])
        MA.append(x)
        MA.append(TS)

    bar.update()

print(X)