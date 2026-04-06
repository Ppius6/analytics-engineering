import unittest
from wedding import Wedding, Invitation, Guest, SpecialGuest


class TestWedding(unittest.TestCase):

    def setUp(self):
        self.wedding = Wedding("Alice", "Bob")
        self.wedding.send_invitation("Jane", "Jane@email.com", is_special=True)
        self.wedding.send_invitation("John", "John@email.com")
        self.jane = self.wedding.get_guest_by_email("Jane@email.com")
        self.john = self.wedding.get_guest_by_email("John@email.com")

    def test_wedding_initialises_correctly(self):
        self.assertEqual(self.wedding.bride_name, "Alice")
        self.assertEqual(self.wedding.groom_name, "Bob")
        self.assertEqual(len(self.wedding.confirmed_guest_list), 0)

    def test_send_invitation_adds_to_list(self):
        self.assertEqual(len(self.wedding.invitation_list), 2)

    def test_send_invitation_creates_correct_guest_type(self):
        self.assertIsInstance(self.jane, SpecialGuest)
        self.assertIsInstance(self.john, Guest)

    def test_duplicate_invitation_not_added(self):
        self.wedding.send_invitation("Jane Again", "Jane@email.com")
        self.assertEqual(len(self.wedding.invitation_list), 2)

    def test_retrieve_invitation_returns_correct_invitation(self):
        invitation = self.wedding.retrieve_invitation("John@email.com")
        self.assertEqual(invitation.guest.email, "John@email.com")

    def test_retrieve_invitation_returns_none_for_unknown_email(self):
        invitation = self.wedding.retrieve_invitation("unknown@email.com")
        self.assertIsNone(invitation)

    def test_get_guest_by_email_returns_correct_guest(self):
        guest = self.wedding.get_guest_by_email("John@email.com")
        self.assertEqual(guest.name, "John")

    def test_get_guest_by_email_returns_none_for_unknown(self):
        guest = self.wedding.get_guest_by_email("nobody@email.com")
        self.assertIsNone(guest)


class TestInvitation(unittest.TestCase):

    def setUp(self):
        self.wedding = Wedding("Alice", "Bob")
        self.wedding.send_invitation("John", "John@email.com")
        self.invitation = self.wedding.retrieve_invitation("John@email.com")

    def test_invitation_default_status_is_pending(self):
        self.assertEqual(self.invitation.status, "pending")

    def test_accept_updates_status(self):
        self.invitation.accept()
        self.assertEqual(self.invitation.status, "accepted")

    def test_decline_updates_status(self):
        self.invitation.decline()
        self.assertEqual(self.invitation.status, "declined")


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.wedding = Wedding("Alice", "Bob")
        self.wedding.send_invitation("John", "John@email.com")
        self.john = self.wedding.get_guest_by_email("John@email.com")

    def test_accept_invitation_updates_status(self):
        self.john.accept_invitation()
        invitation = self.wedding.retrieve_invitation("John@email.com")
        self.assertEqual(invitation.status, "accepted")

    def test_accept_invitation_no_duplicates_in_confirmed_list(self):
        self.john.accept_invitation()
        self.john.accept_invitation()
        self.assertEqual(self.wedding.confirmed_guest_list.count(self.john), 1)

    def test_decline_invitation_updates_status(self):
        self.john.decline_invitation()
        invitation = self.wedding.retrieve_invitation("John@email.com")
        self.assertEqual(invitation.status, "declined")

    def test_decline_removes_from_confirmed_list(self):
        self.john.accept_invitation()
        self.john.decline_invitation()
        self.assertNotIn(self.john, self.wedding.confirmed_guest_list)


class TestSpecialGuest(unittest.TestCase):

    def setUp(self):
        self.wedding = Wedding("Alice", "Bob")
        self.wedding.send_invitation("Jane", "Jane@email.com", is_special=True)
        self.jane = self.wedding.get_guest_by_email("Jane@email.com")

    def test_invite_plus_one_adds_to_invitation_list(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.assertEqual(len(self.wedding.invitation_list), 2)  # Jane + Mark

    def test_invite_plus_one_sets_plus_one_reference(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.assertIsNotNone(self.jane.plus_one)
        self.assertEqual(self.jane.plus_one.email, "mark@email.com")

    def test_invite_plus_one_sets_inviting_guest_email(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.assertEqual(self.jane.plus_one.inviting_guest_email, "Jane@email.com")

    def test_cannot_invite_second_plus_one(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.jane.invite_plus_one("Sam", "sam@email.com")  # second attempt
        self.assertEqual(len(self.wedding.invitation_list), 2)  # still only Jane + Mark

    def test_uninvite_plus_one_removes_invitation(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.jane.uninvite_plus_one()
        self.assertEqual(len(self.wedding.invitation_list), 1)  # only Jane remains

    def test_uninvite_plus_one_resets_reference(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        self.jane.uninvite_plus_one()
        self.assertIsNone(self.jane.plus_one)

    def test_uninvite_plus_one_removes_from_confirmed_list(self):
        self.jane.invite_plus_one("Mark", "mark@email.com")
        mark = self.wedding.get_guest_by_email("mark@email.com")
        mark.accept_invitation()  # Mark confirms
        self.jane.uninvite_plus_one()  # then gets uninvited
        self.assertNotIn(mark, self.wedding.confirmed_guest_list)


if __name__ == "__main__":
    unittest.main()
