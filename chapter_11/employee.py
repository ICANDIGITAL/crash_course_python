import unittest
class Employee(unittest.TestCase):
    """Models a virtual employee."""
    def __int__(self, first_name, last_name, annual_salary):
        """Initializing attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        """Gives raise to an employee's salary."""
        prompt = 'Would you like to give the default raise of $5,000? Enter y for yes or n for no.'
        prompt2 = 'What is the amount you would like to raise the salary by?'
        question = input(prompt)
        if question == 'y':
            self.raise_given = 5000
            self.annual_salary += self.raise_given
        else:
            self.raise_given = int(input(prompt2))
            self.annual_salary += self.raise_given

    def setUp(self):
        """Creates a raise and responses for use in all test methods."""
        self.first_name = 'Chris'
        self.last_name = 'Leader'
        self.annual_salary = 100000
    def test_give_default_raise(self):
        """Tests the default raise amount."""
        self.give_raise()
        self.assertEqual(105000, self.annual_salary)

    def test_give_custom_raise(self):
        self.give_raise()
        self.assertEqual(109000, self.annual_salary)
        return self.annual_salary





