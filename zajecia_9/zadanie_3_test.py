import zadanie_3


class Test(object):
    def test_should_cant_plan_meeting_when_no_meetings(self):
        assert zadanie_3.calculateMeeting([], 1) == 'NIE'

    def test_should_can_plan_meeting_when_only_1_meeting(self):
        meetings = [[1, 4, 1]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'TAK 1'

    def test_should_can_plan_meeting_when_2_meetings_same_day(self):
        meetings = [[1, 4, 1], [5, 6, 1]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'TAK 1 2'

    def test_should_can_plan_meeting_when_2_meetings_same_day_2(self):
        meetings = [[1, 4, 1], [4, 8, 1]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'TAK 1 2'

    def test_should_cant_plan_meeting_when_2_meetings_same_time(self):
        meetings = [[1, 4, 1], [1, 4, 1]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'NIE'

    def test_should_cant_plan_meeting_when_2_meetings_with_covered_time(self):
        meetings = [[2, 4, 1], [3, 5, 1]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'NIE'

    def test_should_can_plan_meeting_when_2_meetings_with_different_days_and_same_time(self):
        meetings = [[1, 4, 2], [1, 4, 1]]
        assert zadanie_3.calculateMeeting(meetings, 2) == 'TAK 2\nTAK 1'

    def test_should_can_plan_meeting_only_second_day(self):
        meetings = [[1, 4, 2], [4, 5, 1], [4, 5, 2], [4, 7, 2]]
        assert zadanie_3.calculateMeeting(meetings, 1) == 'NIE\nTAK 1 3'

    def test_should_cant_plan_meeting_on_two_days(self):
        meetings = [[1, 4, 2], [4, 5, 1], [3, 5, 2], [4, 7, 1]]
        assert zadanie_3.calculateMeeting(meetings, 2) == 'NIE\nNIE'
