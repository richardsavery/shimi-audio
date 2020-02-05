import parselmouth
import numpy as np


def audio_analysis(audio):
    pmaudio = parselmouth.Sound(audio)

    intensity = pmaudio.to_intensity()
    intensity_np = np.array(intensity.values.T)

    intense_min = 13
    intense_max = 19
    intensity_norm = (((intensity_np.std() - intense_min) * 2) / (intense_max - intense_min)) - 1

    pitch = pmaudio.to_pitch()
    pitch_values = np.array(pitch.selected_array['frequency'])

    pitch_min = 150
    pitch_max = 222
    pitch_norm = (((pitch_values.std() - pitch_min) * 2) / (pitch_max - pitch_min)) - 1

    intense_agg_min = 72
    intense_agg_max = 81
    intense_agg = pmaudio.get_intensity()
    intense_agg_norm = (((intense_agg - intense_agg_min ) * 2) / (intense_agg_max - intense_agg_min )) - 1

    energy_agg_min = 0.008
    energy_agg_max= 0.055
    energy_agg = pmaudio.get_energy()
    energy_agg_norm = (((energy_agg  - energy_agg_min) * 2) / (energy_agg_max - energy_agg_min)) - 1

    arousal = (intensity_norm + pitch_norm + intense_agg_norm + energy_agg_norm )/ 4
    arousal = np.clip(arousal, -1, 1)

    print('Values pre norm:','pitch',pitch_values.std(), 'intense',intensity_np.std(),'intense agg', intense_agg,'energy agg',energy_agg)
    print('normalized', 'pitch', pitch_norm, 'intense', intensity_norm, 'intense agg', intense_agg_norm,'energy agg', energy_agg_norm)
    return arousal
