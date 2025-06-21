class App(object):
    def __init__(self, appid, appsettings):
        self.appid = appid
        self.appsettings = appsettings


    def getAppId(self):
        return self.appid

    def getSettings(self):
        return self.appsettings