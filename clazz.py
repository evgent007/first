class Counter:
    value = 0
    def inc(self,delta=1):
        self.value += delta
         
    def dec(self,delta=1):
        self.value = max(self.value - delta,0)
        


c = Counter()
c.inc()
c.inc()
c.inc(40)
print(c.value)

c.dec()
c.dec(30)
print(c.value)

c.dec(delta=10)
print(c.value)
