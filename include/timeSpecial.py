"""
_summary_:
    This module is used to perform various operations on time.

Classes:
    1) TimeSpecial
        Methods:
            1) timeInString()
            2) currentTime()
            3) hoursIn12hFormat()

"""

from time import time, asctime, localtime


class TimeSpecial:
    """
    _summary_:
    class for performing various operations on time.
    """

    def timeInString():
        """
        _summary_:
        returns the current time in string format.
        This function uses asctime and asctime() take argument of timeTuple returned by localtime() and returns them in format "Mon Feb 15 09:34:03 2016" as strings.

        Args:
        Takes no any argument.
        """
        return asctime(localtime(time()))  # localtime() returns timeTuple;

    # function to get current time in integer format.
    def currentTime(myTime):
        """
        _summary_:
        returns current time in tuple in three formats like HH, MM, SS. E.g., 12 34 56, here 12 is hour, 34 is minute, 56 is second.
        Time-Format: 24 hour format.

        Args:
        currentTime(_string_):
        Take arguments of time returns by asctime() function (string).
        """
        hours = int(myTime[11:13])
        minute = int(myTime[14:16])
        second = int(myTime[17:19])
        return hours, minute, second

    def hourIn12hFormat(hour):
        """
        _summary_:
        function to convert hour in 24 hour format to 12 hour format.
        returns tuple of hour in 12 hour format and AM or PM. e.g., (2, PM). returns hour in integer and AM or PM in string.

        Args:
        hour(_int_):
        Take argument of hour in 24 hour format.
        """
        if hour == 0:  # in case of 12:00 AM
            return 12, "AM"
        elif hour < 12:  # in case of 1 to 11 AM
            return hour, "AM"
        elif hour == 12:  # in case of 12:00 PM
            return hour, "PM"
        else:  # hour>12 and in case of 12 to 23 i.e, 12 to 11 PM
            return hour - 12, "PM"
