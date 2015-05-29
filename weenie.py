import re
import time


def get_name_and_major():
    with open('info.txt') as info:
        name = info.readline().strip().lower()
        major = info.readline().strip().lower()
        return (name, major)

def execute_test(match_name, match_major):
    print '--------- Weenie Test ---------'
    print 'Copyright 2015, Benjamin Attal\n'
    name = raw_input('Please enter your name: ')
    major = raw_input('Please enter your major: ')

    weenie_status = bool(re.match(match_name, name.lower()) or \
            re.match(match_major, major.lower()))

    for i in range(0, 3):
        time.sleep(1)
        print "Calculating..."

    time.sleep(1)
    print "...."
    time.sleep(1)

    if weenie_status:
        print "Sorry, you're a weenie."
    else:
        print "Congratulations! You're not a weenie."

execute_test(*get_name_and_major())
