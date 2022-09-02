import os
import time

__DEBUG__ = 0


def DEBUG_PRINT(a):
    if __DEBUG__:
        print(a)
    return


def isAvailablePunch():
    currentInt = ((time.localtime().tm_hour) * 100) + (time.localtime().tm_min)
    DEBUG_PRINT(currentInt)

    if currentInt <= 1200 and currentInt >= 830:
        return True

    return False


def isWeekday():
    dayInt = time.localtime().tm_wday  # 0 means Monday

    if (dayInt == 5) or (dayInt == 6):
        return False

    return True


def writePunchInTime():
    dayStructStr = ["(一)", "(二)", "(三)", "(四)", "(五)"]
    writeLinesStr = (
        ("%02d" % time.localtime().tm_mon)
        + "/"
        + ("%02d" % time.localtime().tm_mday)
        + dayStructStr[time.localtime().tm_wday]
        + " "
        + ("%02d" % time.localtime().tm_hour)
        + ":"
        + ("%02d" % time.localtime().tm_min)
        + "\n"
    )
    pyScriptDirStr = str(os.path.abspath(os.path.dirname(__file__)))
    logFileNameStr = (
        pyScriptDirStr + "/" + str(time.localtime().tm_year) + "_" + ("%02d" % time.localtime().tm_mon) + ".txt"
    )

    DEBUG_PRINT(writeLinesStr)
    DEBUG_PRINT(pyScriptDirStr)
    DEBUG_PRINT(logFileNameStr)

    # if Friday, add a new blank below to make 7 days a section
    if time.localtime().tm_wday == 4:
        writeLinesStr += "\n"

    open(logFileNameStr, "a+", encoding="utf8").writelines(writeLinesStr)

    return


def main():
    # if the time is not between 08:30~11:00 then not record
    if isAvailablePunch() == False:
        return

    # if the day is Saturday or Sunday then not record
    if isWeekday() == False:
        return

    writePunchInTime()

    return


if __name__ == "__main__":
    main()
