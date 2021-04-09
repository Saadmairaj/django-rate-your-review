import os
# temporary fix for non-optimise tensorflow installation.
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow import keras

original_word_index = keras.datasets.imdb.get_word_index()


def add_padding(*data, value, maxlen=250, padding="post"):
    """Add padding to the review."""
    return [keras.preprocessing.sequence.pad_sequences(
        d, value=value, padding=padding,
        maxlen=maxlen) for d in data]


def decode_review(text, word_index):
    """Decode the review into readable format."""
    reverse_word_index = dict([(value, key)
                              for (key, value) in word_index.items()])
    return " ".join([reverse_word_index.get(i, "?") for i in text])


def encode_review(text, word_index):
    """Encode the review using word index."""
    encoded = [word_index['<START>']]
    for word in text.split():
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(word_index['<UNK>'])
    return encoded


def filter_text(text: str):
    """Filters text by removing all ",.()':;" from it."""
    for i in (',', '.', '(', ')', ':', ';', '"', '\''):
        text.replace(i, '')
    return text


def modify_word_index(word_index=None):
    """Modify word index of IMDB dataset."""
    if word_index is None:
        word_index = original_word_index
    word_index = {k: (v+4) for k, v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2
    word_index["<UNUSED>"] = 3
    word_index["<BR>"] = 4
    return word_index


def split_validation_data(*data, _divmod=0.5):
    """Split the data into train and validation data from the given `divmod`."""
    n = round((len(data[0]) - 1) * _divmod)
    return [(d[n:], d[:n]) for d in data]
