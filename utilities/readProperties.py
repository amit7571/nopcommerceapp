import configparser

config=configparser.RawConfigParser()
config.read("/Users/apple/PycharmProjects/noocommerceapp/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseURL")
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getEmail():
        email=config.get('search email','email')
        return email

    @staticmethod
    def getFirstName():
        fname=config.get('search email','fname')
        return fname
    @staticmethod
    def getLastName():
        lname = config.get('search email','lname')
        return lname
    @staticmethod
    def getName():
        name=config.get('search email','name')
        return name




