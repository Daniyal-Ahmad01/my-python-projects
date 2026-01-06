# Temperature Class with Fahrenheit-to-Celsius Converter
# ------------------------------------------------------
# This script demonstrates using a classmethod as an alternative
# constructor. The `from_fahrenheight` method takes a temperature in 
# Fahrenheit, converts it to Celsius, and returns a new Temperature 
# object. This provides a clean and reusable way to handle temperature 
# conversions inside a class structure.
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @classmethod
    def from_fahrenheight(cls,f):
        return cls((float(f)-32)*5/9)
temp="98.6"
a=Temperature.from_fahrenheight(temp)
print(a.celsius)