import unittest
import Batteri

class TestBatteri(unittest.TestCase):
    def test_ladOpp(self):
        batteri = Batteri("B1", 0.0, 100.0)
        batteri.ladOpp(50.0)
        self.assertEqual(batteri.visEnerginivå(), 50.0)

    def test_brukEnergi(self):
        batteri = Batteri("B1", 50.0, 100.0)
        batteri.brukEnergi(30.0)
        self.assertEqual(batteri.visEnerginivå(), 20.0)

    def test_brukEnergi_too_much(self):
        batteri = Batteri("B1", 50.0, 100.0)
        with self.assertRaises(ValueError):
            batteri.brukEnergi(60.0)

    def test_negative_energy(self):
        batteri = Batteri("B1", 50.0, 100.0)
        with self.assertRaises(ValueError):
            batteri.ladOpp(-5.0)

    def test_negative_energy_bruk(self):
        batteri = Batteri("B1", 50.0, 100.0)
        with self.assertRaises(ValueError):
            batteri.brukEnergi(-10.0)

if __name__ == '__main__':
    unittest.main()
