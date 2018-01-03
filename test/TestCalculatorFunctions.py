# TestDrivenDevelopment/TestCalculatorFunctions.py

# import statements
import unittest
import CalculatorFunctions

class KnownValues(unittest.TestCase):
  # Formula for untitest method names is...
  # test_functionName_testDescription

  def test_calculateBMI_forLowerBoundary(self):
    print("Starting test_calculateBMI_forLowerBoundary...")
    result = CalculatorFunctions.calculateBMI(58, 91)
    
    expected = 19
    
    self.assertEqual(expected, result)
    print("...Ending test_calculateBMI_forLowerBoundary.")    

    