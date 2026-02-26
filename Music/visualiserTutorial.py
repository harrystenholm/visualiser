import tkinter as tk
from tkinter import filedialog
import numpy as np
import pygame
import librosa

# getting information from the file
time_series, sample_rate = librosa.load(librosa.ex('trumpet'))
# getting a matrix which contains amplitude values according to frequency and time indexes
stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
# converting the matrix to decibel matrix
spectrogram = librosa.amplitude_to_db(stft, ref=np.max)


# Choose value by time and frequency
frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies

#Getting an array of time periodic
times = librosa.frames_to_time(np.arange(spectrogram.shape[1]),
                       sr = sample_rate, hop_length=512, n_fft=2048*4)
time_index_ratio = len(times)/times[len(times) - 1]
