import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
import tkinter

RATE = 44100
BPM = 100
L1 = (60/BPM*4)
L2, L3, L8 , L16= (L1/2, L1/3, L1/8, L1/16)

# 音階と周波数の対応表
A3_Ra = 220.000
B3_Shi = 246.942
C4_Do = 261.626
D4_Re = 293.665
E4_Mi = 329.628
F4_Fa = 349.228
G4_So = 391.995
A4_Ra = 440.000
B4_Shi = 493.883
C5_Do = 523.251
C5_Do2 = 554.365
D5_Re = 587.330
E5_Mi = 659.255
F5_Fa = 698.456
G5_So = 783.991
A5_Ra = 880.000




def tone(freq, length):
    slen = int(length * RATE)

    t = float(freq) * np.pi * 2 / RATE

    return np.sin(np.arange(slen) * t)


def play_wave(stream, chunks):
    chunk = np.concatenate([chunks]) * 0.25
    fade = 200
    fade_in = np.arange(0., 1., 1/fade)
    fade_out = np.arange(1., 0., -1/fade)
    chunk[:fade] = np.multiply(chunk[:fade], fade_in)
    chunk[-fade:] = np.multiply(chunk[-fade:], fade_out)
    stream.write(chunk.astype(np.float32).tostring())


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                frames_per_buffer=1024,
                output=True)
                

print("play")
play_wave(stream, tone(E4_Mi, L3) )
play_wave(stream, tone(C5_Do2, L3))
play_wave(stream, tone(A4_Ra, L3))

play_wave(stream, tone(E4_Mi, L3))
play_wave(stream, tone(C5_Do2, L3))
play_wave(stream, tone(A4_Ra, L3))

play_wave(stream, tone(E4_Mi, L3))
play_wave(stream, tone(C5_Do2, L3))
play_wave(stream, tone(E4_Mi, L3))
play_wave(stream, tone(A4_Ra, L1))

time.sleep(0.5)

play_wave(stream, tone(A4_Ra, L3))
play_wave(stream, tone(E4_Mi, L3))
play_wave(stream, tone(C5_Do2, L3))
play_wave(stream, tone(A4_Ra, L3))

play_wave(stream, tone(E4_Mi, L3))
play_wave(stream, tone(C5_Do2, L3))
play_wave(stream, tone(A4_Ra, L1))

stream.close()