#import necessary modules
from abc import ABC, abstractmethod

#Create a base class:
class ABsclass(ABC):

        # Function to print a alue
  def print(self,x):
      print("Passed value: ",x)

        # Abstract method
  @abstractmethod
  def task(self):
     print("We are inside Absclass task")

# Create sub class
class test_class(ABsclass):
   def task(self):
        print("We are inside test_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
