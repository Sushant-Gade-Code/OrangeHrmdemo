import configparser

from selenium import webdriver

config=configparser.RawConfigParser()
config.read('C:\\Users\\Admin\\PycharmProjects\\paramaterize\\Configuration\\config.ini')

class Readproperties:

    @staticmethod
    def getUrl():
        url=config.get("Log Info","Url")
        return url

    @staticmethod
    def username():
        Usernmae=config.get("Log Info","Username")
        return Usernmae

    @staticmethod
    def password():
        Password=config.get("Log Info","Password")
        return Password