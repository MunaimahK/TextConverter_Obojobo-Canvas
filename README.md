# TextConverter_Obojobo-Canvas
Python script that reads in files to convert from the Obojobo question format to Canvas question format and vice versa. Quick conversion operation on strings representing SI units.

## **What it does:** 
- GUI format allows input of two files, converting between one to the other.
- Obojobo SI/metric unit representation: value_of_variable \,\mathrm{unit} 
- Canvas SI/metric unit representation: [variable_name] unit

#### The following examples consider a variable mass_2 = 45 kg
### Obojobo -> Canvas:
    45 \,\mathrm{kg} -> [mass_2] kg
### Canvas -> Obojobo:
    [mass_2] kg -> 45 \,\mathrm{kg}
### How to Run it:
    1. Download Temp_Pg.py and text files in SampleRun (ensure they are in same directory)
    2. run python3 Temp_Pg.py
    3. Follow instructions in ConversionPy_UserGuide.pdf to run sample conversion.
    
## **What I learned:**

 - Usage of Python Tkinter GUI package
 - Usage of lambda functions
 - Usage of FILE operations
    
Created with PyCharm
