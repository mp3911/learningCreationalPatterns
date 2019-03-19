import sys
sys.tracebacklimit = 0

import logging
log = logging.getLogger('application logs')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler('person.log', mode = "w")
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
log.addHandler(fh)
log.addHandler(ch)

log.debug("added log")

class interfacePerson:
    def __init__(self):
        self.name = ""
        self.age = 0
    def ouput(self):
        raise NotImplementedError

class funkyPerson(interfacePerson):
    def __init__(self):
        log.info("Created funky person!")
        super().__init__()
        self.funk = 0
    def output(self):
        print(self.name + ": " + str(self.age) + " & FUNK: " + str(self.funk))

class personFactory:
    def __init__(self, type):
        if (type == "funkyPerson"):
            self.p = funkyPerson()
            self.p.name = "Michael Price"
            self.p.age = 25
            self.p.funk = 10000
        else:
            log.error("Incorrect person type, crash")
            raise Exception("Please use a valid person type")

    def get(self):
        return self.p


#personType = input("Give me a person type: ")
#michael = personFactory(personType).get()
#michael.output()