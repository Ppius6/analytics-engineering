from wedding import *

from typing import Optional, List

wedding = Wedding("Alice", "Bob")

wedding.send_invitation("John", "john@email.com")
wedding.send_invitation("Jane", "jane@email.com", is_special=True)

# Duplicate email check
wedding.send_invitation(
    "John Again", "john@email.com"
)  # Guest with email john@email.com already exists

# Guest accepts
john = wedding.get_guest_by_email("john@email.com")
john.accept_invitation()
print(len(wedding.confirmed_guest_list))  # 1

# SpecialGuest invites a plus-one
jane = wedding.get_guest_by_email("jane@email.com")
jane.invite_plus_one(
    "Mark", "mark@email.com"
)  # Plus one invitation sent to mark@email.com
jane.invite_plus_one("Sam", "sam@email.com")  # Already invited a plus one

# Guest declines and is removed from confirmed list
john.decline_invitation()
print(len(wedding.confirmed_guest_list))  # 0
