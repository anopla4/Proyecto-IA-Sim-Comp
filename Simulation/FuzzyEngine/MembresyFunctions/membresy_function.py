from abc import ABC,abstractproperty

class MembresyFunction(ABC):
    @abstractproperty
    def function(self):
        '''
        Returns an instance of the membership function defined by the class instance
        '''
        raise NotImplementedError
    
    @abstractproperty
    def limits(self):
        raise NotImplementedError()
