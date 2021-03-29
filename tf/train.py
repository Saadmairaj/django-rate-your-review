from model import ReviewModel, keras
from utils import (add_padding, modify_word_index, 
                  split_validation_data)


def train(save=True):
    data = keras.datasets.imdb
    word_index = modify_word_index(data.get_word_index())
    num_words = len(word_index) - 1

    ((train_data, train_labels), (test_data, test_labels)
     ) = data.load_data(
        num_words=num_words)

    (train_data, test_data
     ) = add_padding(
        train_data, test_data, value=word_index["<PAD>"],
        maxlen=250)

    ((x_train, x_val), (y_train, y_val)
     ) = split_validation_data(
        train_data, train_labels, divmod=0.3)

    model = ReviewModel(num=num_words)
    model.summary()
    model.compile(optimizer="adam", loss="binary_crossentropy",
                  metrics=["accuracy"])

    fitModel = model.fit(
        x_train, y_train, epochs=40, batch_size=int(512),
        validation_data=(x_val, y_val), verbose=1)
    results = model.evaluate(test_data, test_labels)

    print(results)

    if save:
        return model.save('tf/model.h5')


if __name__ == '__main__':
    train()
