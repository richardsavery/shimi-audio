import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from nltk.corpus import cmudict
import pickle
import os.path as op
dir_path = op.dirname(op.realpath(__file__))


# must run these on first use
# nltk.download('vader_lexicon')
# nltk.download('wordnet')
# nltk.download('nps_chat')
# nltk.download('cmudict')


# created with synonyms - no need with NLTK for now greetings = ['hello', 'hullo', 'hi', 'howdy', 'how-do-you-do',
# 'greeting', 'salutation', 'greet', 'recognize', 'recognise', 'greet', 'greet', 'greet'] farewell = ['adieu',
# 'adios', 'arrivederci', 'auf_wiedersehen', 'au_revoir', 'bye', 'bye-bye', 'cheerio', 'good-by', 'goodby',
# 'good-bye', 'goodbye', 'good_day', 'sayonara', 'so_long']

# this could be useful later on for finding synonyms, but not in use now
def synonyms(word):
    synonymList = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonymList.append(lemma.name())
    return synonymList


# TEXT CLASSIFIER
posts = nltk.corpus.nps_chat.xml_posts()[:10000]


def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


trained_model_path = op.join(dir_path, "models", "text_classifier.p")

if not op.exists(trained_model_path):
    print("Training text classifier...")
    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    trained = nltk.NaiveBayesClassifier.train(train_set)
    pickle.dump(trained, open(trained_model_path, "wb"))
else:
    print("Loading text classifier...")
    trained = pickle.load(open(trained_model_path, "rb"))


def text_classifier(text):
    return trained.classify(dialogue_act_features(text))


analyzer = SentimentIntensityAnalyzer()


def valence_arousal(text):
    # currently just sentiment
    sentiment = analyzer.polarity_scores(text)
    return sentiment


# get number of syllables
syllablesDictionary = cmudict.dict()


def nltkSyllables(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in syllablesDictionary[word.lower()]]


def numberSyllables(text):
    words = text.split()
    syllables = 0
    for word in words:
        try:
            sumSyll = sum(nltkSyllables(word))
        except:
            print("Error: a word is not in dictionary - no syllables added for word")
            sumSyll = 0
        syllables = syllables + sumSyll
    return syllables
