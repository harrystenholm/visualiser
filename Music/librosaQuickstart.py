import matplotlib.pyplot as plt
import numpy as np
import librosa


filename = "Music/lonelyGirl.wav"
# getting information from the file
time_series, sample_rate = librosa.load(filename, duration=5)

def plot_spectrogram(time_series):
    # getting a matrix which contains amplitude values according to frequency and time indexes
    stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
    # converting the matrix to decibel matrix
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

    librosa.display.specshow(spectrogram,
                            y_axis='log', x_axis='time')
    plt.title('Your title')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()

def beatTracker(time_series, sample_rate):
    tempo, beat_frames = librosa.beat.beat_track(y=time_series, sr=sample_rate)
    beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
    print(tempo)
    print(beat_times)

# plot_spectrogram(time_series)

#return tempo and beat times
beatTracker(time_series, sample_rate)