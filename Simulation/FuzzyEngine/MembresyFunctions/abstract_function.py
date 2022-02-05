from abc import ABC,abstractproperty

class membresy_function(ABC):
    @abstractproperty
    def function(self):
        raise NotImplementedError
    
    @abstractproperty
    def limits(self):
        raise NotImplementedError()
        
    