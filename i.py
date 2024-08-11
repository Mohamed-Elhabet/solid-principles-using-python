from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        ...
        

class MeetingAttendable(ABC):
    @abstractmethod
    def attend_meeting(self):
        ...
        
        
class Reportable(ABC):
    @abstractmethod
    def write_report(self):
        pass
    
    

class Manager(Workable, MeetingAttendable, Reportable):
    def work(self):
        print("Managing team...")

    def attend_meeting(self):
        print("Attending a meeting...")

    def write_report(self):
        print("Writing a report...")

class Developer(Workable, MeetingAttendable):
    def work(self):
        print("Writing code...")

    def attend_meeting(self):
        print("Attending a meeting...")

class Intern(Workable):
    def work(self):
        print("Assisting with tasks...")
        
        



def perform_work(worker: Workable):
    worker.work()
    
def attend_meetings(attendee: MeetingAttendable):
    attendee.attend_meeting()
    
def generate_report(reporter: Reportable):
    reporter.write_report()

# Instantiate objects
manager = Manager()
developer = Developer()
intern = Intern()


# Execute methods
perform_work(manager)       # Managing team...
perform_work(developer)     # Writing code...
perform_work(intern)        # Assisting with tasks...

attend_meetings(manager)    # Attending a meeting...
attend_meetings(developer)  # Attending a meeting...

generate_report(manager)    # Writing a report...


