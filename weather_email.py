
def git_emails():
   emails ={}
   try:
        email_file = open('email.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
return emails

def get_schedule():

    try:
        schedule_file = open('schedule.txt','r')

        schedule = schedule_file.read()
    except FileNotFoundError as err :
        print(err)

    return schedule
    
def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)
    
     
main()
