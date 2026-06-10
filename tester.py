import unittest
from unittest.mock import patch
from io import StringIO

from menu_handler import *


class TestCalculatorFunctions(unittest.TestCase):

    def run_with_inputs(self, function, inputs):
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new=StringIO()) as fake_output:
            function()
            return fake_output.getvalue()

    # Algebra
    def test_slope(self):
        output = self.run_with_inputs(handle_algebra_menu, ["1", "1", "3", "2", "6", "0"])
        self.assertIn("The slope of the line is 2.0", output)

    def test_quadratic_formula(self):
        output = self.run_with_inputs(handle_algebra_menu, ["2", "1", "-5", "6", "0"])
        self.assertIn("The roots are 3.0 and 2.0", output)

    def test_linear_equation_solver(self):
        output = self.run_with_inputs(handle_algebra_menu, ["3", "2", "4", "10", "0"])
        self.assertIn("x = 3.0", output)

    def test_logarithm(self):
        output = self.run_with_inputs(handle_algebra_menu, ["4", "100", "10", "0"])
        self.assertIn("The logarithm is 2.0", output)

    def test_natural_log(self):
        output = self.run_with_inputs(handle_algebra_menu, ["5", "1", "0"])
        self.assertIn("The natural log is 0.0", output)

    # Geometry
    def test_distance(self):
        output = self.run_with_inputs(handle_geometry_menu, ["1", "0", "0", "3", "4", "0"])
        self.assertIn("The distance is 5.0", output)

    def test_midpoint(self):
        output = self.run_with_inputs(handle_geometry_menu, ["2", "0", "0", "4", "6", "0"])
        self.assertIn("The midpoint is (2.0, 3.0)", output)

    def test_pythagorean(self):
        output = self.run_with_inputs(handle_geometry_menu, ["3", "3", "4", "0"])
        self.assertIn("The hypotenuse is 5.0", output)

    def test_triangle_area(self):
        output = self.run_with_inputs(handle_shape_area_menu, ["1", "10", "5", "0"])
        self.assertIn("The triangle area is 25.0", output)

    def test_rectangle_area(self):
        output = self.run_with_inputs(handle_shape_area_menu, ["2", "4", "5", "0"])
        self.assertIn("The rectangle area is 20.0", output)

    def test_square_area(self):
        output = self.run_with_inputs(handle_shape_area_menu, ["3", "5", "0"])
        self.assertIn("The square area is 25.0", output)

    def test_circle_area(self):
        output = self.run_with_inputs(handle_shape_area_menu, ["4", "1", "0"])
        self.assertIn("The circle area is", output)

    def test_circle_circumference(self):
        output = self.run_with_inputs(handle_circumference_menu, ["1", "1", "0"])
        self.assertIn("The circle circumference is", output)

    def test_rectangle_perimeter(self):
        output = self.run_with_inputs(handle_circumference_menu, ["2", "4", "5", "0"])
        self.assertIn("The rectangle perimeter is 18.0", output)

    def test_square_perimeter(self):
        output = self.run_with_inputs(handle_circumference_menu, ["3", "5", "0"])
        self.assertIn("The square perimeter is 20.0", output)

    def test_triangle_perimeter(self):
        output = self.run_with_inputs(handle_circumference_menu, ["4", "3", "4", "5", "0"])
        self.assertIn("The triangle perimeter is 12.0", output)

    def test_cube_volume(self):
        output = self.run_with_inputs(handle_shape_volume_menu, ["1", "3", "0"])
        self.assertIn("The cube volume is 27.0", output)

    def test_rectangular_prism_volume(self):
        output = self.run_with_inputs(handle_shape_volume_menu, ["2", "2", "3", "4", "0"])
        self.assertIn("The rectangular prism volume is 24.0", output)

    # Trigonometry
    def test_sin(self):
        output = self.run_with_inputs(handle_trigonometry_menu, ["1", "90", "0"])
        self.assertIn("The sine is 1.0", output)

    def test_cos(self):
        output = self.run_with_inputs(handle_trigonometry_menu, ["2", "0", "0"])
        self.assertIn("The cosine is 1.0", output)

    def test_tan(self):
        output = self.run_with_inputs(handle_trigonometry_menu, ["3", "45", "0"])
        self.assertIn("The tangent is", output)

    def test_degrees_to_radians(self):
        output = self.run_with_inputs(handle_trigonometry_menu, ["7", "1", "180", "0"])
        self.assertIn("The radian value is", output)

    def test_radians_to_degrees(self):
        output = self.run_with_inputs(handle_trigonometry_menu, ["7", "2", "3.141592653589793", "0"])
        self.assertIn("The degree value is 180.0", output)

    # Financial
    def test_compound_interest(self):
        output = self.run_with_inputs(handle_financial_menu, ["1", "1000", "10", "1", "1", "0"])
        self.assertIn("The final amount is 1100.0", output)

    def test_simple_interest(self):
        output = self.run_with_inputs(handle_financial_menu, ["2", "1000", "10", "1", "0"])
        self.assertIn("The simple interest is 100.0", output)

    def test_percentage(self):
        output = self.run_with_inputs(handle_financial_menu, ["4", "200", "10", "0"])
        self.assertIn("10.0% of 200.0 is 20.0", output)

    def test_tip_calculator(self):
        output = self.run_with_inputs(handle_financial_menu, ["5", "100", "20", "0"])
        self.assertIn("The tip is 20.0", output)
        self.assertIn("The total is 120.0", output)

    # Physics / Engineering
    def test_kinetic_energy(self):
        output = self.run_with_inputs(handle_physics_engineering_menu, ["1", "10", "2", "0"])
        self.assertIn("The kinetic energy is 20.0", output)

    def test_ohms_law(self):
        output = self.run_with_inputs(handle_physics_engineering_menu, ["2", "2", "5", "0"])
        self.assertIn("The voltage is 10.0", output)

    def test_vector_magnitude(self):
        output = self.run_with_inputs(handle_physics_engineering_menu, ["3", "3", "4", "0"])
        self.assertIn("The vector magnitude is 5.0", output)

    # Number Theory
    def test_factorial(self):
        output = self.run_with_inputs(handle_number_theory_menu, ["1", "5", "0"])
        self.assertIn("The factorial is 120", output)

    def test_prime_checker_prime(self):
        output = self.run_with_inputs(handle_number_theory_menu, ["2", "7", "0"])
        self.assertIn("The number is prime", output)

    def test_prime_checker_not_prime(self):
        output = self.run_with_inputs(handle_number_theory_menu, ["2", "8", "0"])
        self.assertIn("The number is not prime", output)

    def test_gcd(self):
        output = self.run_with_inputs(handle_number_theory_menu, ["3", "12", "18", "0"])
        self.assertIn("The GCD is 6", output)

    def test_lcm(self):
        output = self.run_with_inputs(handle_number_theory_menu, ["4", "4", "6", "0"])
        self.assertIn("The LCM is 12", output)

    # Conversions
    def test_miles_to_kilometers(self):
        output = self.run_with_inputs(handle_length_conversions_menu, ["1", "1", "1", "0"])
        self.assertIn("The converted value is 1.60934", output)

    def test_pounds_to_kilograms(self):
        output = self.run_with_inputs(handle_weight_conversions_menu, ["1", "1", "1", "0"])
        self.assertIn("The converted value is 0.453592", output)

    def test_gallons_to_liters(self):
        output = self.run_with_inputs(handle_volume_conversions_menu, ["1", "1", "1", "0"])
        self.assertIn("The converted value is 3.78541", output)

    def test_seconds_to_minutes(self):
        output = self.run_with_inputs(handle_time_conversions_menu, ["1", "1", "60", "0"])
        self.assertIn("The converted value is 1.0", output)

    def test_fahrenheit_to_celsius(self):
        output = self.run_with_inputs(handle_temperature_conversions_menu, ["1", "1", "32", "0"])
        self.assertIn("The converted temperature is 0.0", output)

    # Health
    def test_bmi(self):
        output = self.run_with_inputs(handle_health_menu, ["1", "180", "70", "0"])
        self.assertIn("Your BMI is", output)


if __name__ == "__main__":
    unittest.main()