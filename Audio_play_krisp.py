import pandas as pd
from os import listdir
from os.path import isfile, join
from pygame import mixer
import json

class audio_check:
    def __init__(self, path):
        self.path = path

    def inputvalue(self, labels):

        print('Write n if audio is noisy and write c if audio is clear')
        inp = input()
        if inp == "n" or inp == "N":
            labels.append("n")
        elif inp == "c" or inp == "C":
            labels.append("c")
        else:
            self.inputvalue(labels)
        return labels

    def main_func(self):
        self.file_names = [f for f in listdir(self.path + "music/") if isfile(join(self.path + "music/", f))]
        label = list()
        for i in self.file_names:
            mixer.init()

            mixer.music.load(path + "music/" + i)
            mixer.music.play()
            label = self.inputvalue(label)
            mixer.music.stop()
        self.label = label

    def create_data(self):
        self.data = pd.DataFrame(
            {'path': self.file_names,
             'label': self.label
             })

    def to_json(self):
        self.data.to_json(path + "data_json/" + "data.json")

#path = "C:/Users/chilinga/Desktop/Audio/"
path = "Enter your path /Audio/"

obj = audio_check(path)
obj.main_func()
obj.create_data()
obj.to_json()