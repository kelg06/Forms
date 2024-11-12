from django.test import SimpleTestCase
from app import views

class TestFontTimes(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/front?string=Chocolate&number=2")
        self.assertContains(response, "ChoCho")

    def test_near_hundred_90(self):
        response = self.client.get("/front?string=Chocolate&number=3")
        self.assertContains(response, "ChoChoCho")
    
    def test_near_hundred_89(self):
        response = self.client.get("/front?string=Abc&number=3")
        self.assertContains(response, "AbcAbcAbc")

class Testfix_teen(SimpleTestCase):
    def test_string_splosion_code(self):
        response = self.client.get("/teen/?a=1&b=2&c=3")
        self.assertContains(response, 6)

    def test_string_splosion_abc(self):
        response = self.client.get("/teen/?a=2&b=13&c=1")
        self.assertContains(response, 3)

    def test_string_splosion_ab(self):
        response = self.client.get("/teen/?a=2&b=1&c=14")
        self.assertContains(response, 3)


class Testxyz(SimpleTestCase):
    def test_cat_dog_catdog(self):
        response = self.client.get("/xyz/?str=abcxyz")
        self.assertContains(response, True)

    def test_cat_dog_catcat(self):
        response = self.client.get("/cat-dog/?str=abc.xyz")
        self.assertContains(response, False)

    def test_cat_dog_1cat1cadodog(self):
        response = self.client.get("/cat-dog/?str=xyz.abc")
        self.assertContains(response, True)


class Testcentered(SimpleTestCase):
    def test_lone_some_123(self):
        response = self.client.get("/center/?num1=1&num2=2&num3=3&num4=4&num5=100&num6=&num7=")
        self.assertContains(response, 3)

    def test_lone_some_323(self):
        response = self.client.get("/venter/?num1=1&num2=1&num3=5&num4=5&num5=10&num6=8&num7=7")
        self.assertContains(response, 5)

    def test_lone_some_333(self):
        response = self.client.get("/center/?num1=-10&num2=-4&num3=-2&num4=-4&num5=-2&num6=0&num7=")
        self.assertContains(response, -3)
