import WordClass
import subprocess as sp
import Synonym
import random

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

    def getMeaning(self, word_surface):
        flg = True
        return_message = "\""+word_surface+"\""
        if word_surface in self.getSurfaceDict().keys():
            for word in self.words_list:
                if word_surface == word.getSurface():
                    if flg:
                        return_message += "の日本語訳として「"
                        for meaning in word.getMeaning():
                            return_message += meaning
                        return_message += "」が存在し，その品詞は"
                        return_message += word.getPOS()
                        return_message += "です．"
                        if word.hasSupplement():
                            return_message += "補足:"
                            return_message += word.getSupplement()
                        flg = False
                    else:
                        return_message += "また，別の日本語訳として「"
                        for meaning in word.getMeaning():
                            return_message += meaning
                        return_message += "」が存在し，その品詞は"
                        return_message += word.getPOS()
                        return_message += "です．"
                        if word.hasSupplement():
                            return_message += "補足:"
                            return_message += word.getSupplement()

        else:
            return_message += "に相当する日本語訳が見つかりませんでした．"

        return return_message

    def hasMeaning(self, word_surface):
        return (word_surface in self.getSurfaceDict().keys())

    def getSurface(self, word_meaning):
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

    def hasSurface(self, word_meaning):
        return (word_meaning in self.getMeaningDict().keys())

    def getSynonymMeaning(self, word_surface):
        flg = True
        return_message = "\""+word_surface+"\""
        if word_surface in self.getSurfaceDict().keys():
            for word in self.words_list:
                if word_surface == word.getSurface():
                    if flg:
                        return_message += "の日本語訳として「"
                        for meaning in word.getMeaning():
                            return_message += meaning
                        return_message += "」が存在します．"
                        flg = False
                        return_message += "さらに，その類義語として"
                        synonym_list = Synonym.getSynonymList(word.getMeaning()[0])
                        for i in range(5):
                            s = random.choice(synonym_list)
                            if s == word.getMeaning()[0]:
                                continue
                            return_message += "「"
                            return_message += s
                            return_message += "」"
                        return_message += "が考えられます．"
                    else:
                        return_message += "また，別の日本語訳として「"
                        for meaning in word.getMeaning():
                            return_message += meaning
                        return_message += "」が存在します．"
                        return_message += "さらに，その類義語として"
                        synonym_list = Synonym.getSynonymList(word.getMeaning()[0])
                        for i in range(5):
                            s = random.choice(synonym_list)
                            if s == word.getMeaning()[0]:
                                continue
                            return_message += "「"
                            return_message += s
                            return_message += "」"
                        return_message += "が考えられます．"

        else:
            return_message += "に相当する日本語訳が見つかりませんでした．"

        return return_message
    
    def getSynonymSurface(self, word_meaning):
        flg = True
        return_message = "「"+word_meaning+"」に相当するセラフェノ訳が見つかりませんでした．"
        synonym_list = Synonym.getSynonymList(word_meaning)

        for synonym in synonym_list:
            if synonym in self.getMeaningDict().keys():
                return_message += "「"+word_meaning+"」の類義語「"
                return_message += synonym+"」のセラフェノ訳として"
                for word in self.words_list:
                    if synonym in word.getMeaning():
                        return_message += "\""
                        return_message += word.getSurface()
                        return_message += "\"が存在します．"
                flg = False

        if flg:
            return_message += "類義語に対するセラフェノ訳が見つかりませんでした．"
            
        return return_message
