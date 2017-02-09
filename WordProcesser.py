import WordClass
import subprocess as sp

class WordProcesser:
    def __init__(self):
        self.words_list = []
        lines = sp.check_output(["nkf","-w","dic-ongo.txt"]).decode("utf-8")
        lines = lines.replace("\r","").split("\n")
        for line in lines:
            if line == "" or line == "\n":
                continue
            self.words_list.append(WordClass.Word(line))

    def getSurfaceDict(self):
        surfaces = {}
        for word in self.words_list:
            surfaces[word.getSurface()] = word
        return surfaces

    def getMeaningDict(self):
        meanings = {}
        for word in self.words_list:
            meaning_list = word.getMeaning()
            for meaning in meaning_list:
                meanings[meaning] = word
        return meanings

    def returnMeaning(self, word_surface):
        flg = True
        return_message = "\""+word_surface+"\""
        if word_surface in self.getSurfaceDict().keys():
            for word in self.words_list:
                if word_surface == word.getSurface():
                    if flg:
                        return_message += "の日本語訳として「"
                        return_message += word.getMeaning()[0]
                        return_message += "」が存在し，その品詞は"
                        return_message += word.getPOS()
                        return_message += "です．"
                        if word.hasSupplement():
                            return_message += "補足:"
                            return_message += word.getSupplement()
                        flg = False
                    else:
                        return_message += "また，別の日本語訳として「"
                        return_message += word.getMeaning()[0]
                        return_message += "」が存在し，その品詞は"
                        return_message += word.getPOS()
                        return_message += "です．"
                        if word.hasSupplement():
                            return_message += "補足:"
                            return_message += word.getSupplement()

        else:
            return_message += "に相当する日本語訳が見つかりませんでした．"

        return return_message

    def returnSurface(self, word_meaning):
        flg = True
        return_message = "「"+word_meaning+"」"
        if word_meaning in self.getMeaningDict().keys():
            for word in self.words_list:
                if word_meaning in word.getMeaning():
                    if flg:
                        return_message += "のセラフェノ訳として\""
                        return_message += word.getSurface()
                        return_message += "\"が存在します．"
                        flg = False
                    else:
                        return_message += "また，別のセラフェノ訳として\""
                        return_message += word.getSurface()
                        return_message += "\"が存在します．"

        else:
            return_message += "に相当するセラフェノ訳が見つかりませんでした．"
            
        return return_message
