class Ferrari:
  def fuel_type(self):
   print ("Petrol")
  def max_speed(self):
    print("Max speed 350")
class BMW:
  def fuel_type(self):
   print( "Diesel")
   def max_speed(self):
    print("Max speed is 240")
a1 = Ferrari()
b1 = BMW( )
# Iterate objects of same type

for car in (Ferrari,BMW):

# call methods without checking class of object
 a1.Ferrari()
 b1.BMW()