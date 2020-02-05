from shimiEmotionalResponse import *
from audio_analysis import *
import time



def audio_response_demo(inputText, audio, samplerate):
    # shimi's Emotion
    valence = 0.5

    t = time.time()
    valence = shimi_emotion(inputText, valence)
    # print("Time for valence detection: %f" % (time.time() - t))

    t = time.time()
    arousal = audio_analysis(audio)
    # print("Time for arousal detection: %f" % (time.time() - t))

    t = time.time()
    midi_path, audio_path = shimi_response(inputText, valence, arousal)
    # print("Time for shimi_response() call: %f" % (time.time() - t))

    print("!! Valence: %f, Arousal: %f !!" % (valence, arousal))

    return audio_path, midi_path, valence, arousal # audio to playback
