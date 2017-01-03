# -*- encoding: utf-8

from __future__ import print_function

import itertools
import re
import sys
import time


def human_time(seconds):
    """Returns a human-friendly representation of the number of seconds."""
    assert seconds >= 0
    hours = seconds / (60 * 60)
    minutes = (seconds / 60) % 60
    seconds = seconds % 60
    return '%02d:%02d:%02d' % (hours, minutes, seconds)


def print_time(ts):
    print('\r%s ' % human_time(ts), end='')
    sys.stdout.flush()
    time.sleep(1)


def stopwatch():
    """A stopwatch that counts up from 00:00:00 once per second.

    This definitely isn't accurate and will gradually lose time, but it's
    good enough for basic purposes.
    """
    try:
        for ts in itertools.count():
            print_time(ts)
    except KeyboardInterrupt:
        print('')


def parse_countdown_length(string):
    """Given a countdown length string, return the number of seconds
    to run for.

    Raises a ValueError if the string cannot be parsed.
    """
    match = re.match(
        r'^(?:(?P<hours>[0-9]+)h\s*)?'
        r'(?:(?P<minutes>[0-9]+)m\s*)?'
        r'(?:(?P<seconds>[0-9]+)s)?$',
        string.strip().lower(),
    )
    if not match:
        raise ValueError('Unable to parse countdown length %r' % string)

    seconds = 0
    if match.group('hours'):
        seconds += int(match.group('hours')) * 60 * 60
    if match.group('minutes'):
        seconds += int(match.group('minutes')) * 60
    if match.group('seconds'):
        seconds += int(match.group('seconds'))
    return seconds


def end_countdown():
    """Ends a countdown by repeatedly printing the ASCII bell."""
    while True:
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(0.5)


def countdown():
    """A countdown clock.  Accepts input of the form '1s', '5m1s', '1h2m3s',
    and so on.
    """
    try:
        seconds = parse_countdown_length(' '.join(sys.argv[1:]))
    except ValueError as err:
        sys.exit(err)
    except IndexError:
        print('Usage: countdown <countdown_length>')
        sys.exit(1)

    try:
        for ts in itertools.count(start=seconds, step=-1):
            print_time(ts)
            if ts == 0:
                break
    except KeyboardInterrupt:
        print('\nCountdown aborted early!')
        sys.exit(1)

    try:
        print('\nCountdown finished!')
        end_countdown()
    except KeyboardInterrupt:
        pass
