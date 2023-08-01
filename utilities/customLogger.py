import logging

class LogGen:

    @staticmethod
    def loggen():
        logger=logging.getLogger()
        filehandler = logging.FileHandler(filename= "/Users/apple/PycharmProjects/noocommerceapp/Logs/automation.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger