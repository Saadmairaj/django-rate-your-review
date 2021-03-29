from tensorflow import keras
# from tf import NUM_WORD

# class ReviewModel(keras.Sequential):
#     def __init__(self, layers=None, name=None, num=10000):
#         super().__init__(layers=layers, name=name)
#         self.add(keras.layers.Embedding(num, 16))
#         self.add(keras.layers.GlobalAveragePooling1D())
#         self.add(keras.layers.Dense(16, activation='relu'))
#         self.add(keras.layers.Dense(1, activation='sigmoid'))
    
#     def fit(self, *args, **kwargs):
#         kwargs['use_multiprocessing'] = kwargs.get(
#             'use_multiprocessing', True)
#         return super().fit(*args, **kwargs)


def ReviewModel(num):
    model = keras.Sequential()
    model.add(keras.layers.Embedding(num, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    return model