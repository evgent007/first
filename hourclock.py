class HourClock:
    def __init__(self,h = 0):
        self.h = h

    @property
    def hours(self):
        return self.h

    @hours.setter
    def hours(self,n):
                
        self.h = (n % 12) 
        
        
clock = HourClock()
print(clock.hours)
clock.hours += 6
print(clock.hours)
clock.hours += 5
print(clock.hours)
clock.hours += 4
print(clock.hours)
clock.hours -= 14
print(clock.hours)
clock.hours = 123
print(clock.hours)
