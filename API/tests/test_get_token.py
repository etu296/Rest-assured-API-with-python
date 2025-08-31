import unittest
import requests
import json
#configuration
BASE_URL = "https://restful-booker.herokuapp.com"
USERNAME = "admin"
PASSWORD = "password123"

class BookingTests(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        """Run once before all tests"""
        cls.token = None
        cls.booking_id = None
        cls.booking_data = {
             "firstname" : "Etu",
                "lastname" : "Mahmuda",
                "totalprice" : 2100,
                "depositpaid" : True,
                "bookingdates" : {
                    "checkin" : "2025-08-08",
                    "checkout" : "2025-08-30"
                },
                "additionalneeds" : "Breakfast"
        }
    def test_01_authentication(self):
        """get token by authentication"""
        print("\n[Getting authentication token]")
        auth_url = f"{BASE_URL}/auth"
        auth_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        print(f"Auth URL: {auth_url}")
        print(f"Auth Data: {auth_data}")
        try:
            response = requests.post(auth_url, json = auth_data, timeout = 5)
            print(f"Response status code: {response.status_code}")
            print(f"Response body : {response.text}")
            self.assertEqual(response.status_code, 200, f"Authentication failed:{response.status_code}")
            token = response.json().get("token")
            self.assertIsNotNone(token, "Token not found in response")
            self.__class__.token = token
            print(f"Authentication successful. Token: {token[:5]}") # Print only first 5 characters of token for security
        except Exception as e:
            self.fail(f"Authentication failed: {e}")

       

if __name__ == '__main__':
    unittest.main()
       