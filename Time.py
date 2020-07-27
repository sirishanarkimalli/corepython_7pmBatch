class Time:

    def __init__(self,h,m,s):
        self.h=h
        self.m =m
        self.s = s

    @property
    def hour(self):
        return self.h

    @hour.setter
    def hour(self,value):
        if value >=0 and value<=23:
            self.h=value

    @property
    def total_seconds(self):
        return self.h *3600 + self.m*60 +self.s

    @total_seconds.setter
    def total_seconds(self,value):
        self.total_seconds=value

    #overriding
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __gt__(self,other):
        return self.total_seconds > other.total_seconds

    def __int__(self):
        return self.total_seconds

t1=Time(10,20,30)
t2=Time(10,20,30)
t1.h=29
print(t1)
print(t1==t2)
print(t1>t2)
print(10+int(t1))

