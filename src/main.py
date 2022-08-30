"""
    Script to auto reload a webpage by pressing ctrl + r every second.
    Used of external module pyautogui.
     *author: Suraj Kumar Giri.
     *Date: 30-08-2022 (Last Updated)
     *Time: 22:40:20
"""
from pyautogui import hotkey
from time import sleep
# importing timeSpecial.py module present in current directory to perform time related operations.
import include.timeSpecial as myTime


def calculateFinalTime(startTime: tuple, minute: int) -> tuple:
    """_summary_:
    This function will add passed minutes in current time.
    and returns the final calculated time after adding.
    Time format: HH,MM,SS (int 24 hour format as passed in startTime argument)

    Args:
        startTime(tuple): initial time
        minute(int): minutes to be added in current time.
    """
    # startTime[0] is hour, startTime[1] is minute, startTime[2] is second
    if startTime[1] + minute < 59:
        return startTime[0], startTime[1] + minute, startTime[2]
    else:
        addHours = (startTime[1] + minute)/60
        addMinutes = (startTime[1] + minute) % 60

        newHours = startTime[0] + addHours
        newMinutes = startTime[1] + addMinutes
        # but we have check the new hours are within 24h format or it crossed 23:59:59.
        if newHours > 23:
            # e.g, if newHours will 24 then newHours = 0 and if newHours will 25 then newHours = 1.
            newHours = newHours - 24
        return newHours, newMinutes, startTime[2]


def autoReloadPage(timeSpan: int | None, timeInterval: float | None = 0.8) -> None:
    """
    _summary_:
    This function is used to auto reload a webpage by pressing ctrl + r.
    Auto pressing of 'ctrl+r' will repeated in given time interval.
    The process will continue till time span provided.
    By default: timeSpan = Infinite
                timeInterval = 0.8 sec

    _args_(_int_, _float_):
    Take arguments of timeSpan till which the program will continue to reload the webpage and also take timeInterval in which 'ctrl+r' will be pressed.
    """
    # to sleep for 5 seconds for switching to respective webpage to implement the script
    print("\033[1;37mSwitch to webpage in 10 seconds...\033[0m")
    sleep(10)

    if type(timeSpan) is None:
        while(True):
            hotkey("ctrl", "r")
            # sleep can take floatTyped value. 0.8 sec is best for reloading the webpage.
            sleep(timeInterval)

    else:  # means timeSpan is given
        currentTimeStr = myTime.TimeSpecial.timeInString()
        # initialTime is tuple of hour, minute, second (starting time of the script)
        initialTime = myTime.TimeSpecial.currentTime(currentTimeStr)
        finalTime = calculateFinalTime(initialTime, timeSpan)

        while(True):
            timeNowStr = myTime.TimeSpecial.timeInString()
            timeNow = myTime.TimeSpecial.currentTime(timeNowStr)
            if timeNow[0] >= finalTime[0] and timeNow[1] >= finalTime[1] and timeNow[2] >= finalTime[2]:
                break
            hotkey("ctrl", "r")
            sleep(timeInterval)


def main():
    print(
        "\033[1;36m\033[2J\033[HDo you want to add time span for auto reloading the webpage?")
    print("\033[1;32mIf yes then write time (in minutes) else press enter or anything else for auto reloading page for infinite duration..")
    try:
        timeSpan = int(
            input("\033[1;35mEnter time span (in minutes): \033[0m"))
        print("\033[1;32mSelected Time Span is ", timeSpan, " minutes.\033[0m")
    except ValueError:  # either user press enter or written any value other than integer.
        print("\033[1;31mSelected Time Span is Infinite.\033[0m")
        timeSpan = None

    try:
        timeInterval = float(input(
            "\033[1;36mWrite time interval for auto reloading the webpage (press enter or anything else for default 0.8 sec) in sec: "))
    except ValueError:  # either user press enter or written any string value
        print("\033[4;32mSelected Time Interval is 0.8 sec.\033[0m")
        timeInterval = None
    else:
        print("\033[1;32mSelected Time Interval is ",
              timeInterval, " sec.\033[0m")
    finally:
        if timeInterval is None:
            autoReloadPage(timeSpan)
        else:
            autoReloadPage(timeSpan, timeInterval)


if __name__ == "__main__":
    main()
