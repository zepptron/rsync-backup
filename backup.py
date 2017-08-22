#!/usr/bin/env python
"""Rsync Backupscript."""
import time
import os

logfile = "/var/log/cron_backup"


def write_log(file, text):
    """Write to logfile."""
    act_time = str(time.localtime().tm_year) + "." + str(time.localtime().tm_mon) + "." + str(time.localtime().tm_mday) + " " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)
    try:
        configfile = open(file, "a")
        configfile.write(str(act_time) + " " + text + "\n")
        configfile.close()
        return 0    # no errors
    except:
        return 1    # errors


write_log(logfile, "starting backup...")

attempts = 3
while attempts > 0:
    returnvalue = os.system('rsync -auv --log-file=/var/log/cron_backup --delete /mnt/shari/ /mnt/backuphdd/')

    # if no errors > write to log
    if returnvalue == 0:
        write_log(logfile, "backup successfull.")
        break

    # if error > write to log and wait 10min
    if returnvalue > 0:
        write_log(logfile, "backup fucked up, wait 10mins!")
        time.sleep(600)

    # decrease attempts
    attempts = attempts - 1

# if error > write to log
if returnvalue > 0:
    write_log(logfile, "fuck it. errors... goodbye.")
