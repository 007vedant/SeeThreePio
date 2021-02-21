import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# get similarity score of two sentences using cosine vector method


def get_similarity_score(s1, s2):
    s1_tokens = word_tokenize(s1)
    s2_tokens = word_tokenize(s2)

    stopw = stopwords.words("english")
    v1, v2 = [], []

    s1_clean = {w for w in s1_tokens if not w in stopw}
    s2_clean = {w for w in s2_tokens if not w in stopw}

    keywords = s1_clean.union(s2_clean)
    for w in keywords:
        if w in s1_clean:
            v1.append(1)
        else:
            v1.append(0)
        if w in s2_clean:
            v2.append(1)
        else:
            v2.append(0)

    c = 0
    for i in range(len(keywords)):
        c += v1[i] * v2[i]

    score = c / float((sum(v1) * sum(v2)) ** 0.5)
    return score


if __name__ == "__main__":
    s1 = sys.argv[0]
    s2 = sys.argv[1]

    print(get_similarity_score(s1, s2))
