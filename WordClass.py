class Word:
    def __init__(self, line):
        elements = line.replace("\n","").split("\t")

        self.__surface = elements[0]
        self.__POS     = elements[1]
        self.__meaning = elements[2]
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

    def hasSupplement(self):
        return not(self.__supplement == "")

    def getSupplement(self):
        return self.__supplement
