from fuzzywuzzy import fuzz
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))


def common_words(q1, q2):

    w1 = set(str(q1).lower().split())
    w2 = set(str(q2).lower().split())

    return len(w1.intersection(w2))


def word_share(q1, q2):

    w1 = set(str(q1).lower().split())
    w2 = set(str(q2).lower().split())

    if len(w1) + len(w2) == 0:
        return 0

    return len(w1.intersection(w2)) / (len(w1) + len(w2))


def jaccard_similarity(q1, q2):

    s1 = set(str(q1).lower().split())
    s2 = set(str(q2).lower().split())

    union = s1.union(s2)

    if len(union) == 0:
        return 0

    return len(s1.intersection(s2)) / len(union)


def token_features_fetch(q1, q2):

    q1_tokens = str(q1).split()
    q2_tokens = str(q2).split()

    if len(q1_tokens) == 0 or len(q2_tokens) == 0:
        return [0.0] * 8

    q1_words = set(
        [word for word in q1_tokens if word not in STOP_WORDS]
    )

    q2_words = set(
        [word for word in q2_tokens if word not in STOP_WORDS]
    )

    q1_stops = set(
        [word for word in q1_tokens if word in STOP_WORDS]
    )

    q2_stops = set(
        [word for word in q2_tokens if word in STOP_WORDS]
    )

    common_word_count = len(q1_words & q2_words)
    common_stop_count = len(q1_stops & q2_stops)
    common_token_count = len(set(q1_tokens) & set(q2_tokens))

    features = []

    # common word features
    features.append(
        common_word_count /
        (min(len(q1_words), len(q2_words)) + 0.0001)
    )

    features.append(
        common_word_count /
        (max(len(q1_words), len(q2_words)) + 0.0001)
    )

    # stop word features
    features.append(
        common_stop_count /
        (min(len(q1_stops), len(q2_stops)) + 0.0001)
    )

    features.append(
        common_stop_count /
        (max(len(q1_stops), len(q2_stops)) + 0.0001)
    )

    # token features
    features.append(
        common_token_count /
        (min(len(q1_tokens), len(q2_tokens)) + 0.0001)
    )

    features.append(
        common_token_count /
        (max(len(q1_tokens), len(q2_tokens)) + 0.0001)
    )

    # first word same?
    features.append(
        int(q1_tokens[0] == q2_tokens[0])
    )

    # last word same?
    features.append(
        int(q1_tokens[-1] == q2_tokens[-1])
    )

    return features


def build_features(q1, q2):

    features = {}

    # length features
    features['q1_len'] = len(q1)
    features['q2_len'] = len(q2)

    features['len_diff'] = abs(
        len(q1) - len(q2)
    )


    features['word_count_diff'] = abs(
        len(q1.split()) -
        len(q2.split())
    )

    s1 = set(q1.lower().split())
    s2 = set(q2.lower().split())

    features['jaccard'] = (
        len(s1.intersection(s2))
        /
        (len(s1.union(s2)) + 0.0001)
    )

    # word count features
    features['q1_num_words'] = len(q1.split())
    features['q2_num_words'] = len(q2.split())


    # overlap features
    features['common_words'] = common_words(q1, q2)
    features['word_share'] = word_share(q1, q2)

    features['jaccard'] = jaccard_similarity(
        q1,
        q2
    )

    # token features
    token_features = token_features_fetch(q1, q2)

    features['cwc_min'] = token_features[0]
    features['cwc_max'] = token_features[1]

    features['csc_min'] = token_features[2]
    features['csc_max'] = token_features[3]

    features['ctc_min'] = token_features[4]
    features['ctc_max'] = token_features[5]

    features['first_word_eq'] = token_features[6]
    features['last_word_eq'] = token_features[7]

    # fuzzy features
    features['fuzz_ratio'] = fuzz.ratio(
        q1,
        q2
    )

    features['fuzz_partial_ratio'] = fuzz.partial_ratio(
        q1,
        q2
    )

    features['token_sort_ratio'] = fuzz.token_sort_ratio(
        q1,
        q2
    )

    features['token_set_ratio'] = fuzz.token_set_ratio(
        q1,
        q2
    )

    return features