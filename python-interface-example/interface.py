from abc import ABC, abstractmethod

# Define the interface using ABC (Abstract Base Class)
class IValami(ABC):
    @abstractmethod
    def area(self, text):
        pass