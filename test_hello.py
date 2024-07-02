import unittest
from hello import main

class TestHello(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main())  # Assuming main() returns None

if __name__ == '__main__':
    unittest.main()
