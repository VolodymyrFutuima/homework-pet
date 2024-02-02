class Pet:

    def __init__(self, name, species):

        self.name = name

        self.species = species

        self.hungry = True

        self.tired = True

        self.happy = False

    def feed(self):

        if self.hungry:

            print(f"{self.name} уже кормлен.")

            self.hungry = False

        else:

            print(f"{self.name} не голоден.")



    def sleep(self):

        if self.tired:

            print(f"{self.name} заснул.")

            self.tired = False

        else:

            print(f"{self.name} не устал.")



    def play(self):

       if self.happy:

        print(f"{self.name} уже играет.")

       else:

        print(f"{self.name} сейчас играет.")

       self.happy = True


cat = Pet("Амулет", "кот")
