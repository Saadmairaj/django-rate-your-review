from tensorflow import keras
from utils import (add_padding, decode_review,
                   encode_review, modify_word_index, filter_text)


def test():
    model = keras.models.load_model("tf/model.h5")
    word_index = modify_word_index()

    with open('tf/test_review.txt', encoding='utf-8 ') as file:
        review = filter_text(file.read())
        print(review)
        encode = add_padding([encode_review(review, word_index)],
                             value=word_index['<PAD>'], maxlen=250)
        print(decode_review(encode_review(review, word_index), word_index))
        predict = model.predict(encode)
        print("\n\n")
        print("Original Review link:  "
              "https://timesofindia.indiatimes.com/"
              "entertainment/marathi/movie-reviews/"
              "basta/movie-review/80670252.cms")
        print("Rating on Site: 2.5/5")
        print("Prediction: ", predict[0])


if __name__ == '__main__':
    test()
