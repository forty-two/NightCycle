import datetime

import sublime

class ThemeSwitcher():
    def __init__(self):
        self.checkDelay = 2000 # 2 seconds

    def changeScheme(self, desiredScheme):
        sublimeSettings = sublime.load_settings('Preferences.sublime-settings')
        if desiredScheme:
            currentScheme = sublimeSettings.get('color_scheme')

            if currentScheme != desiredScheme:
                print("Switching to new colour scheme: %s" % desiredScheme)
                sublimeSettings.set('color_scheme', desiredScheme)

    def determineScheme(self):
        timePeriods = sublime.load_settings('NightCycle.sublime-settings').get('timePeriods')
        dateNow = datetime.datetime.now()
        currentTime = datetime.time(dateNow.hour, dateNow.minute)

        for timePeriod in timePeriods:
            startTime = self.timeObject(timePeriods.get(timePeriod, {}).get('startTime', '0:00'))
            endTime = self.timeObject(timePeriods.get(timePeriod, {}).get('endTime', '0:00'))
            if self.inTimePeriod(startTime, endTime, currentTime):
                return timePeriods.get(timePeriod, {}).get('colourScheme', None)
        return False

    def inTimePeriod(self, startTime, endTime, currentTime):
        if currentTime >= startTime and currentTime <= endTime:
            return True
        elif endTime < startTime:
            if currentTime >= startTime and currentTime <= datetime.time(23,59): # overnight before midnight
                return True
            elif currentTime <= endTime and currentTime >= datetime.time(0,0): # overnight after midnight
                return True
        return False

    def setCorrectScheme(self):
        correctScheme = self.determineScheme()
        self.changeScheme(correctScheme)

    def timeObject(self, timeString):
        datetimeObject = datetime.datetime.strptime(timeString, '%H:%M')
        return datetime.time(datetimeObject.hour, datetimeObject.minute)

    def run(self):
        sublime.set_timeout(self.run, self.checkDelay)
        self.setCorrectScheme()
        

if 'NightCycle' not in globals():
    NightCycle = True
    switcher = ThemeSwitcher()
    switcher.run()
