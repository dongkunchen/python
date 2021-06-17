from win32com.client import constants
import os
import win32com.client
import pythoncom

class SpeechRecognition:
    def __init__(self,wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammer()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add()