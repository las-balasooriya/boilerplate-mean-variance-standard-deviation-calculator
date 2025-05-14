import numpy as np

def calculate(list):
    if len(list) == 9:
        array_1 = np.array(list)
        array_2 = array_1.reshape(3, 3)
        print(array_2)
        calculations = {
            'mean': [np.mean(array_2,axis=0).tolist(), np.mean(array_2,axis=1).tolist(), np.mean(array_2.flatten())],
            'variance': [np.var(array_2,axis=0).tolist(), np.var(array_2,axis=1).tolist(), np.var(array_2.flatten())],
            'standard deviation': [np.std(array_2,axis=0).tolist(), np.std(array_2,axis=1).tolist(), np.std(array_2.flatten())],
            'max': [np.max(array_2,axis=0).tolist(), np.max(array_2,axis=1).tolist(), np.max(array_2.flatten())],
            'min': [np.min(array_2,axis=0).tolist(), np.min(array_2,axis=1).tolist(), np.min(array_2.flatten())],
            'sum': [np.sum(array_2,axis=0).tolist(), np.sum(array_2,axis=1).tolist(), np.sum(array_2.flatten())]
            }
        print(calculations)
    else:
        raise ValueError('List must contain nine numbers.')


    return calculations