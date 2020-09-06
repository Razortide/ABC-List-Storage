import os, datetime, time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ABCList:
    """Stores a single ABC list"""
    total_count = 0
    topicsDict = {}

    def saveList(self):
        # TODO: Implement saving list to filesystem
        pass

    def exportList(self):
        # TODO: Implement exporting list to filesystem
        pass

    def importList(self):
        # TODO: Implement importing list from filesystem
        pass

    def displayList(self) -> None:
        print("Thema: {}   Nummer: {}   Datum: {}   Zeit: {}"
              .format(self.topic, self.number, self.date, self.time))
        for key, value in self.content_list.items():
            print("{} - {}".format(key, value))

    def enterValue(self, entry) -> None:
        if entry[0].upper() not in self.content_list.keys():
            self.content_list.update({entry[0]: []})
        if entry not in self.content_list[entry[0].upper()]:
            self.content_list[entry[0].upper()].append(entry)

    def __init__(self) -> None:
        self.topic = input("Thema der ABC Liste: ")
        date = input("Datum der ABC Liste (DD.MM.JJJJ): ")
        if date == "":
            self.date = "{}.{}.{}".format(datetime.date.today().day, datetime.date.today().month,
                                          datetime.date.today().year)
        else:
            self.date = date
        print("Setze den {} als Datum.".format(self.date))
        ABCList.total_count += 1
        if self.topic not in ABCList.topicsDict:
            print("Erstelle {} als neues Thema".format(self.topic))
            ABCList.topicsDict[self.topic] = 1
        else:
            ABCList.topicsDict[self.topic] += 1
            print("Erstelle die {}. Liste zum Thema '{}'".format(ABCList.topicsDict[self.topic], self.topic))

        self.content_list = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [],
                             'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [],
                             'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

        self.number = ABCList.topicsDict[self.topic]
        self.time = "00:00"
        self.consolidated = False  # Is used to determine if list was already consolidated before
        start_time = time.time()
        while True:
            self.displayList()
            entry = input("Begriff: ")
            if entry != "":
                self.enterValue(entry)
                self.time = time.time() - start_time
                cls()
            else:
                break

    def editABCList(self) -> None:
        # Nur Änderungen möglich
        while True:
            self.displayList()
            entry = input("Begriff: ")
            if entry != "":
                if entry in self.content_list[entry[0].upper()]:
                    self.content_list[entry[0].upper()].remove(entry)
                    print("{} ausgewählt.".format(entry))
                    self.enterValue(input("Neuen Begriff eingeben: "))
                else:
                    print("Begriff '{}' nicht in ABC-Liste vorhanden. Bitte auf Groß- und Kleinschreibung achten."
                          .format(entry))
                cls()
            else:
                break

    @classmethod
    def displayTopics(cls):
        for key in cls.topicsDict:
            print("{} ({})".format(key, cls.topicsDict[key]))
        # TODO: Ausgabe aufhübschen

    def consolidateTopic(cls, topic):
        pass
        # Todo: Konsolidiert ABC-Listen eines Topics
