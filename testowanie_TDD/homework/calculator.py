

class Calculator:
    def add(self, *args):
        """Functions adds multiple arguments and returns their sum.

        Parameters:
        arguments (float): Array of numbers

        Returns:
        float: Sum of arguments

       """
        return sum(args)

    def subtract(self, a, b):
        """Functions subtract subtrahend from minuend and returns results of that operation.

        Parameters:
        minuend (float)
        subtrahend (float)

        Returns:
        float: Result of subtract

       """
        return a - b

    def multiply(self, a, b):
        """Functions multiplies arguments and returns results of that operation.

          Parameters:
          multiplicand (float)
          multiplier (float)

          Returns:
          float: Result of multiplication

         """
        return a * b

    def divide(self, a, b):
        """Functions divides dividend by divider and returns results of that operation.

          Parameters:
          dividend (float)
          divider (float)

          Returns:
          float: Result of dividing parameters

         """
        try:
            return a / b
        except TypeError:
            raise ValueError

