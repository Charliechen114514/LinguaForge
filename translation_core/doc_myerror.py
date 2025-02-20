class NoneDriverSpecified(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Error Occurs, No Translation Driver Specified!:{}\n".format(self.__msg)
    
class NoneSpliterSpecified(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Error Occurs, No Spliter Specified!:{}\n".format(self.__msg)
     