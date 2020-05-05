import re, math, nltk
from facts import facts, keys, triple_important, double_important
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download("stopwords")
stopword = stopwords.words("english")

WORD = re.compile(r"\w+")
default_fallback_msg = "I m sorry. Please verify here https://www.who.int/"


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    return Counter(WORD.findall(text))


def get_similarity(a, b):
    a = text_to_vector(a.strip().lower())
    b = text_to_vector(b.strip().lower())

    return get_cosine(a, b)


def to_lower(text):
    return " ".join([w.lower() for w in nltk.word_tokenize(text)])


def strip_punctuation(text):
    return "".join(c for c in text if c not in punctuation)


def replace_key(k):
    for key in keys:
        if to_lower(k) in keys[key]:
            return key
    return k


def replacekeys(text):
    return " ".join([replace_key(w) for w in nltk.word_tokenize(text)])


def remove_non_ascii(text):
    encoded_string = text.encode("ascii", "ignore")
    decoded_string = encoded_string.decode()
    return decoded_string


def remove_stopwords(text):
    clean_text = [word for word in nltk.word_tokenize(text) if word not in stopword]
    return " ".join([w for w in clean_text])


def multiply(w):
    if w in triple_important:
        return w + " " + w + " " + w
    if w in double_important:
        return w + " " + w
    return w


def multiply_important_words(s):
    return " ".join([multiply(w) for w in nltk.word_tokenize(s)])

def preprocess(text):
    text = multiply_important_words(text)

    text = replacekeys(text)
    text = remove_non_ascii(text)
    text = remove_stopwords(text)
    
    return text


def get_response(s):
    s = preprocess(s)

    max_sim = 0
    max_sim_ix = -1

    ix = 0

    while ix < len(facts):
        l_x = to_lower(s)
        r_y = remove_stopwords(to_lower(facts[ix]))
        # print(l_x, r_y)
        cur_sim = get_similarity(l_x, r_y)
        if cur_sim > max_sim:
            max_sim, max_sim_ix = cur_sim, ix
        ix = ix + 1

    if max_sim > 0.5 and max_sim_ix != -1:
        return facts[max_sim_ix]

    return default_fallback_msg


# ================================================================
# Testing
xrr = "younger age people cannot be infected with the coronavirus"
print(get_response(xrr))
