class Word:
    def __init__(self, line):
        elements = line.replace("\n","").split("\t")

        self.__surface = elements[0]
        self.__POS     = elements[1]
        self.__meaning = elements[2].split(",")
        if len(elements) > 3:
            self.__supplement = elements[3]
        else:
            self.__supplement = ""

    def getSurface(self):
        return self.__surface

    def getPOS(self):
        return self.__POS

    def getMeaning(self):
        return self.__meaning

    def getSupplement(self):
        if self.__supplement == "":
            return "この単語に対する補足はありません．"
        else:
            return self.__supplement
