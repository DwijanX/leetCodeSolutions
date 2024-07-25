from collections import Counter
class FrequencyTracker(object):

    counter=None
    freqs=None
    def __init__(self):
        self.counter=Counter()
        self.freqs=Counter()

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.counter[number]+=1
        self.freqs[self.counter[number]-1]-=1
        self.freqs[self.counter[number]]+=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if(self.counter[number]>0):
            self.freqs[self.counter[number]]-=1
            self.freqs[self.counter[number]-1]+=1
            self.counter[number]-=1
        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if(self.freqs[frequency]>0):
            return True
        return False
    
obj = FrequencyTracker()
obj.deleteOne(2)
obj.deleteOne(1)
obj.add(1)
param_3 = obj.hasFrequency(1)
param_3 = obj.hasFrequency(1)
param_3 = obj.hasFrequency(1)


