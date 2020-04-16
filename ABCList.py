import os
import datetime
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ABCList:
    """Stores a single ABC list"""
    topicsCount = {"total": 0}

    def __init__(self):
        self.topic = input("Thema der ABC Liste: ")
        date = input("Datum der ABC Liste (DD. MM. JJJJ): ")
        if date == "":
            self.date = "{}. {}. {}".format(datetime.date.today().day, datetime.date.today().month,
                                            datetime.date.today().year)
        else:
            self.date = date
        print("Setting date to {}".format(self.date))
        ABCList.topicsCount["total"] += 1
        if self.topic not in ABCList.topicsCount:
            print("Creating {} as new topic".format(self.topic))
            ABCList.topicsCount[self.topic] = 1
        else:
            ABCList.topicsCount[self.topic] += 1
            print("Creating the {}. list regarding the topic {}".format(ABCList.topicsCount[self.topic], self.topic))

        self.content_list = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [],
                             'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [],
                             'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

        self.number = ABCList.topicsCount[self.topic]
        self.time = "00:00"
        self.consolidated = False  # Is used to determine if list was already consolidated before
        start_time = time.time()
        while True:
            print("Thema: {}   Nummer: {}   Datum: {}   Zeit: {}".format(self.topic, self.number, self.date, self.time))
            for key in self.content_list:
                print("{} - {}".format(key, self.content_list[key]))
            entry = input("Begriff: ")
            if entry != "":
                if entry[0] not in self.content_list.keys():
                    self.content_list.update({entry[0]: []})
                if entry not in self.content_list[entry[0].upper()]:
                    self.content_list[entry[0].upper()].append(entry)
                self.time = time.time() - start_time
                cls()
            else:
                break

    def editABCList(self):
        # Nur Änderungen möglich
        while True:
            print("Thema: {}   Nummer: {}   Datum: {}   Zeit: {}".format(self.topic, self.number, self.date, self.time))
            for key in self.content_list:
                print("{} - {}".format(key, self.content_list[key]))
            entry = input("Begriff (oder EXIT): ")
            if entry != "EXIT":
                if entry in self.content_list[entry[0].upper()]:
                    pass
                    # TODO: Änderung implementieren
                cls()
            else:
                break

    @classmethod
    def consolidateTopic(cls, topic):
        pass
        # Todo: Konsolidiert ABC-Listen eines Topics