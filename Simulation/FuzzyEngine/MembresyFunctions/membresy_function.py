from abc import ABC,abstractproperty, abstractmethod

class MembresyFunction(ABC):
    @abstractproperty
    def function(self):
        '''
        Returns an instance of the membership function defined by the class instance
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_extended_function(self, extended):
        raise NotImplementedError()

    @abstractproperty
    def limits(self):
        raise NotImplementedError()
