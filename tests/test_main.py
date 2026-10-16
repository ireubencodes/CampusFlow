import unittest
from unittest.mock import patch

from main import create_new_ticket


class TestCreateNewTicket(unittest.TestCase):

    @patch("main.save_tickets")
    @patch("builtins.input", side_effect=["Network outage", "Network", "high", "12"])
    def test_created_ticket_is_added_before_saving(self, _input, save):
        tickets = []

        create_new_ticket(tickets)

        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0]["id"], "T001")
        save.assert_called_once_with(tickets)

    @patch("main.save_tickets", side_effect=OSError("disk full"))
    @patch("builtins.input", side_effect=["Network outage", "Network", "high", "12"])
    def test_failed_save_removes_ticket_from_collection(self, _input, _save):
        tickets = []

        create_new_ticket(tickets)

        self.assertEqual(tickets, [])


if __name__ == "__main__":
    unittest.main()
