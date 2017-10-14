class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(24,42)
print(a.sum())
