from textAnalysis import *
import os.path as op
import soundfile
import random
import time
import os
dir_path = op.dirname(op.realpath(__file__))

def shimi_emotion(text, speaker_valence):
    # Sets Shimi's Emotion
    s = time.time()

    pos_neg = valence_arousal(text)
    pos_neg.pop('compound', None)
    pos_neg.pop('neu', None)
    dict_key = max(pos_neg, key=pos_neg.get)

    if dict_key == 'neg':
        new_valence = pos_neg[dict_key] * - 1
    else:
        new_valence = pos_neg[dict_key]

    print ("speaker valence", new_valence)
    return new_valence


def shimi_response(text, valence, arousal):
    # HOW SHOULD SHIMI RESPOND
    # recognise greeting or farewell #otherwise look at statement type
    statement = text_classifier(text)

    s = time.time()

    if statement == "Greet":
        # randomly select a greeting

        random_choice = str(random.randrange(1, 4, 1))

        audio_path = op.join(dir_path, "audio", "greet" + random_choice + ".wav")
        midi_path = op.join(dir_path, "audio", "greet" + random_choice + ".mid")

        print("Shimi says hi")

    elif valence >= 0:
        if arousal >= 0:
            # happy
            random_choice = str(random.randrange(1, 10, 1))

            audio_path = op.join(dir_path, "audio", "happy" + random_choice + ".wav")
            midi_path = op.join(dir_path, "audio", "happy" + random_choice + ".mid")

            print("Shimi is happy")
        else:
            # calm
            random_choice = str(random.randrange(1, 10, 1))

            audio_path = op.join(dir_path, "audio", "calm" + random_choice + ".wav")
            midi_path = op.join(dir_path, "audio", "calm" + random_choice + ".mid")

            print("Shimi is calm")

    else:
        if arousal <= 0:
            random_choice = str(random.randrange(1, 10, 1))

            audio_path = op.join(dir_path, "audio", "sad" + random_choice + ".wav")
            midi_path = op.join(dir_path, "audio", "sad" + random_choice + ".mid")

            print("Shimi is sad")
        else:
            # sad
            random_choice = str(random.randrange(1, 10, 1))

            audio_path = op.join(dir_path, "audio", "angry" + random_choice + ".wav")
            midi_path = op.join(dir_path, "audio", "angry" + random_choice + ".mid")

            print("Shimi is angry")


    return midi_path, audio_path
