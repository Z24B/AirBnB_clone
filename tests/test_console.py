import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output != "")
            self.assertIsInstance(BaseModel().load(output), BaseModel)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'New Name'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn("New Name", output)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_new_methods(self):
        # Create instances
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            city_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            amenity_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            place_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            review_id = f.getvalue().strip()

        # Update instances with dictionary
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} {'{'}\"first_name\": \"John\", \"last_name\": \"Doe\"{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("John", output)
            self.assertIn("Doe", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id} {'{'}\"name\": \"California\"{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            output = f.getvalue().strip()
            self.assertIn("California", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id} {'{'}\"name\": \"Los Angeles\"{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city_id}")
            output = f.getvalue().strip()
            self.assertIn("Los Angeles", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id} {'{'}\"name\": \"Wifi\"{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            output = f.getvalue().strip()
            self.assertIn("Wifi", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} {'{'}\"name\": \"Cozy House\", \"number_rooms\": 2{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {place_id}")
            output = f.getvalue().strip()
            self.assertIn("Cozy House", output)
            self.assertIn("2", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id} {'{'}\"text\": \"Great place to stay!\"{'}'}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {review_id}")
            output = f.getvalue().strip()
            self.assertIn("Great place to stay!", output)

        # Update instances with attribute name and value
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} first_name 'Alice'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("Alice", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id} name 'New York'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            output = f.getvalue().strip()
            self.assertIn("New York", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id} name 'San Francisco'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city_id}")
            output = f.getvalue().strip()
            self.assertIn("San Francisco", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id} name 'Parking'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            output = f.getvalue().strip()
            self.assertIn("Parking", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} name 'Large House'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {place_id}")
            output = f.getvalue().strip()
            self.assertIn("Large House", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id} text 'Amazing place to stay!'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {review_id}")
            output = f.getvalue().strip()
            self.assertIn("Amazing place to stay!", output)


if __name__ == '__main__':
    unittest.main()
