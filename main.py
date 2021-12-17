import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()


def audio_transcription(path):
    sound = AudioSegment.from_wav(path)
    chunks = split_on_silence(sound,
                               min_silence_len=1000,
                               silence_thresh=sound.dBFS - 20,
                               keep_silence=300, )

    folder = "voicetotext/audio-chunks"

    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in the 'folder_name' directory.
        chunk_filename = os.path.join(folder, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. \n"
                print(text)
                whole_text += text
    file = open(f"{mp3}.html", "w+")
    file.write("<html><p>" + whole_text + "</p></html>")
    file.close()
    return whole_text


if __name__ == '__main__':
    mp3 = input("Which mp3 do you want to transcribe:\n")
    audio = AudioSegment.from_mp3(f"voicetotext/{mp3}")
    path = audio.export("../voicetotext/transcript.wav", format="wav")
    audio_transcription(path)
