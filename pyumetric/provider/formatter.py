"""
Metrics Formatters
"""


class Base():

    __response = None

    def __init__(self, response):
        self.__response = response


class NewRelic(Base):

    def __init__(self, response):
        super().__init__(response)

    def parse(self):
        pass
