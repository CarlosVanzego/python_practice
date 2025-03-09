# Problem: Manager of a mid-sized company wants to create a daily report that tracks the use of machines (Specifically, she wants to know which users are currently connected to which machines).
# So the solution is to 




def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "Login":
            machines[event.machine].add(event.user) 
        elif event.type == "Logout":
            machines[event.machine].remove
    return machines     

def generate_report(machines):
    for machine, users in machines.items():
      # this line ensures that I don't print any machines where nobody is currently logged in.
        if len (users) > 0: 
          # this line combines each logged-in user attribute into one variable.
          user_list = " , ".join(users)
          print("{}: {}".format(machine, user_list))




class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'carlos'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'harry'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'james'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

