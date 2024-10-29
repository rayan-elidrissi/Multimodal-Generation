from pydub import AudioSegment, effects
import numpy as np
from IPython.display import Audio

# Générer une onde sonore avec des harmoniques et une enveloppe de type piano
def generate_realistic_piano_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = (amplitude * np.sin(2 * np.pi * frequency * t) +
            0.5 * amplitude * np.sin(2 * np.pi * 2 * frequency * t) +  
            0.25 * amplitude * np.sin(2 * np.pi * 3 * frequency * t) +
            0.15 * amplitude * np.sin(2 * np.pi * 4 * frequency * t))
    envelope = np.exp(-4 * t)  # Décroissance rapide pour un effet de piano
    wave = wave * envelope
    audio = (wave * (2**15 - 1)).astype(np.int16)
    sound = AudioSegment(audio.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
    return effects.normalize(sound)

# Dictionnaire complet des fréquences de notes pour le piano
note_frequencies = {
    "C1": 32.70, "C#1": 34.65, "D1": 36.71, "D#1": 38.89, "E1": 41.20, "F1": 43.65, "F#1": 46.25, "G1": 49.00, "G#1": 51.91, "A1": 55.00, "A#1": 58.27, "B1": 61.74,
    "C2": 65.41, "C#2": 69.30, "D2": 73.42, "D#2": 77.78, "E2": 82.41, "F2": 87.31, "F#2": 92.50, "G2": 98.00, "G#2": 103.83, "A2": 110.00, "A#2": 116.54, "B2": 123.47,
    "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56, "E3": 164.81, "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65, "A3": 220.00, "A#3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30, "A4": 440.00, "A#4": 466.16, "B4": 493.88,
    "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25, "E5": 659.26, "F5": 698.46, "F#5": 739.99, "G5": 783.99, "G#5": 830.61, "A5": 880.00, "A#5": 932.33, "B5": 987.77,
    "C6": 1046.50, "C#6": 1108.73, "D6": 1174.66, "D#6": 1244.51, "E6": 1318.51, "F6": 1396.91, "F#6": 1479.98, "G6": 1567.98, "G#6": 1661.22, "A6": 1760.00, "A#6": 1864.66, "B6": 1975.53,
    "C7": 2093.00, "C#7": 2217.46, "D7": 2349.32, "D#7": 2489.02, "E7": 2637.02, "F7": 2793.83, "F#7": 2959.96, "G7": 3135.96, "G#7": 3322.44, "A7": 3520.00, "A#7": 3729.31, "B7": 3951.07,
    "C8": 4186.01
}

# Fonction pour créer le pattern boogie-woogie main gauche avec répétitions
def create_boogie_pattern(filename="boogie_custom.wav", duration_per_note=0.3, repetitions=1):
    # Main gauche ajustée selon les séquences demandées
    left_hand_pattern = [
        ["C2", "C2", "D#2", "E2", "G2", "C2", "A2", "G2"], ["C2", "C2", "D#2", "E2", "G2", "C2", "A2", "G2"],  # do, do, re#, mi, sol, do, la, sol (2 fois)
        ["F3", "F3", "G#3", "A3", "C4", "F3", "D4", "C4"], ["F3", "F3", "G#3", "A3", "C4", "F3", "D4", "C4"],  # F3 F3 G#3 A3 C4 F3 D4 C4 (2 fois)
        ["C2", "C2", "D#2", "E2", "G2", "C2", "A2", "G2"],  # do, do, re#, mi, sol, do, la, sol
        ["F3", "F3", "G#3", "A3", "C4", "F3", "D4", "C4"],  # F3 F3 G#3 A3 C4 F3 D4 C4
        ["G3", "G3", "A#3", "B3", "D4", "G3", "E4", "D4"]   # G3 G3 A#3 B3 D4 G3 E4 D4
    ]

    # Construire la séquence finale avec répétitions
    sequence = []
    for _ in range(repetitions):  # Répéter le pattern complet
        for chord in left_hand_pattern:
            for idx, note in enumerate(chord):
                # Accentuation des 2e et 4e temps pour le groove
                volume = 6 if idx % 2 == 1 else 0  # Accent sur le 2e et 4e temps
                left_wave = generate_realistic_piano_wave(note_frequencies[note], duration_per_note)
                sequence.append(left_wave + volume)

    # Concatenation et exportation
    boogie_track = sum(sequence)
    boogie_track.export(filename, format="wav")
    return Audio(filename, autoplay=True)

# Generate and play the boogie-woogie track
filename="boogie_woogie.wav"
create_boogie_pattern(filename, duration_per_note=0.3, repetitions=3)

Audio(filename, autoplay=True)