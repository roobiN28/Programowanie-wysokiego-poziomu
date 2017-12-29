import re

class ListEmails(object):
    emails = []
    def __init__(self, email):
        if re.match('[^@]+@[^@]+\.[^@]+', email):
            self.emails.append(email)
            print 'Dodano poprawny email: ' + email
        else:
            raise ValueError

try:
    ListEmails('robert@gmail.com')
    ListEmails('ania@wp.pl')
    ListEmails('robertbezmalpygmail.com')
except ValueError:
    print 'Podano niepoprawny email'