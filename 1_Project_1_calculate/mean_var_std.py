import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    di = {}
    arr = np.array(list).reshape(3,3)
    print(arr)
    di['mean'] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
    di['variance'] = [np.var(arr,axis=0).tolist(), np.var(arr,axis=1).tolist(), np.var(arr)]
    di['standard deviation'] = [np.std(arr,axis=0).tolist(), np.std(arr,axis=1).tolist(), np.std(arr)]
    di['max'] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
    di['min'] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
    di['sum'] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
    return di