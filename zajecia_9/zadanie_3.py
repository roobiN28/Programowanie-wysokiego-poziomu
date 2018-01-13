def calculateMeeting(meetings, day):
    currentDay = 1
    result = ''
    while currentDay <= day:
        result = result + '\n' + calculateMeetingForDay(meetings, day)
        currentDay += 1

    if result.startswith('\n'):
        result = result[1:]
    return result


def calculateMeetingForDay(meetings, day):
    candidate = 0
    current = None
    i = 0
    while i < len(meetings):
        if meetings[i][2] == day:
            result = checkFor(meetings, day, i)
            if result > 0:
                return 'TAK ' + str(i+1) + ' ' + str(result+1)
            elif result == 0:
                candidate = i
            else:
                candidate = 0
        i += 1
    if candidate > 0:
        return 'TAK ' + str(candidate+1)
    else:
        return 'NIE'


def checkFor(meetings, day, i):
    candidate = 0
    j = i + 1
    while j < len(meetings):
        if meetings[j][2] == day:
            erlier = meetings[i]
            later = meetings[j]
            if meetings[j][0] < meetings[i][0]:
                erlier = meetings[j]
                later = meetings[i]

            if later[0] < erlier[1]:
                return -1
            else:
                candidate = j
        j += 1
    return candidate
