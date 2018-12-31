"""
with every frame that comes in:
    check if it is_speech 
    append to buffer - frame and is_speech
    if 90% of buffer is_speech then:
        get current time (then to be used in filename)
        start saving to separate array

    when 90% not speech:
        save the array to a file with time as filename
        emty the array
        continue
"""
import pyaudio
import collections
import contextlib
import wave
import webrtcvad
import datetime

def write_wave(path, audio, sample_rate):
    with contextlib.closing(wave.open(path, 'wb')) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio)

def main():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 32000
    RECORD_SECONDS = 10
    FRAME_DURATION = 30
    CHUNK = int(RATE*FRAME_DURATION/1000)
    PADDING_DURATION = 300
    num_padding_frames = int(PADDING_DURATION/FRAME_DURATION)
    FILE_PATTERN = '~/audio/%s.wav'

    p = pyaudio.PyAudio()
    ring_buffer = collections.deque(maxlen=num_padding_frames)
    vad = webrtcvad.Vad(3)
    speech = False
    num_speech = 0

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("recording")
    while True:
        data = stream.read(CHUNK)
        is_speech = vad.is_speech(data, RATE)

        if not speech:
            ring_buffer.append((data, is_speech))
            num_speech = len([f for f, speech in ring_buffer if speech])
            if num_speech>0.9*num_padding_frames:
                speech = True
                time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S.%f")
                print("\n" + time + "\n")
                print("you started speaking")
        else:
            ring_buffer.append((data, is_speech))
            num_notspeech = len([f for f, speech in ring_buffer if not speech])
            if num_notspeech>0.9*num_padding_frames:
                speech=False
                time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S.%f")
                print("\n" + time + "\n")
                print("you finished speaking")
            else:
                print("you are speaking")


if __name__ == '__main__':
    main()

