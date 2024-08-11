from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        ...
        
    @abstractmethod
    def attend_meeting(self):
        ...
        
    @abstractmethod
    def write_report(self):
        ...
        
        
class Manager(Worker):
    def work(self):
        print('Managing team...')
        
    def attend_meeting(self):
        print('Attending a meeting...')
        
    def write_report(self):
        print('writing a report')
        

class Developer(Worker):
    def work(self):
        print('Writing code...')
        
    def attend_meeting(self):
        print('Attending a meeting...')
        
    def write_report(self):
        pass
    

class Intern(Worker):
    def work(self):
        print("Assisting with tasks...")

    def attend_meeting(self):
        pass

    def write_report(self):
        pass
    
