import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\hp\\PycharmProjects\\FramePractnight\\Configuration\\config.ini')


class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get("login data", 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get("login data", "password")
        return Password
