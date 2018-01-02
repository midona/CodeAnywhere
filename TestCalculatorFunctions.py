# TestDrivenDevelopment/TestCalculatorFunctions.py

# import statements
import unittest
import CalculatorFunctions

class KnownValues(unittest.TestCase):
  # Formula for untitest method names is...
  # test_functionName_testDescription

  def test_calculateBMI_forLowerBoundary(self):
    result = CalculatorFunctions.calculateBMI(58, 91)
    
    expected = 19
    
    self.assertEqual(expected, result)
    
    
# Run the test

if __name__ == '__main__':
  print("Starting Tests...")
  unittest.main()

    