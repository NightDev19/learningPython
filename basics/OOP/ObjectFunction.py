class Animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice
    def speak(self):
        print(f"{self.type} says {self.voice}")

dog = Animal("Dog", "Bark")
dog.speak()
