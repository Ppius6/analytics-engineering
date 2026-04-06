from typing import List, Optional


class Invitation:
    def __init__(self, guest: "Guest") -> None:
        self.guest = guest
        self.status = "pending"  # default - guest has not responded yet

    def __str__(self) -> str:
        return f"Invitation for {self.guest.name} - status: {self.status}"

    def accept(self) -> None:
        self.status = "accepted"

    def decline(self) -> None:
        self.status = "declined"


class Wedding:
    def __init__(self, bride_name: str, groom_name: str) -> None:
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.confirmed_guest_list: List["Guest"] = []
        self.invitation_list: List["Invitation"] = []
        
    def __str__(self) -> str:
        return f"{self.bride_name} & {self.groom_name}'s Wedding."
    
    def send_invitation(self, name: str, email: str, is_special: bool = False) -> None:
        if self.get_guest_by_email(email):
            return
        if is_special:
            guest = SpecialGuest(name, email, self)
        else:
            guest = Guest(name, email, self)

        invitation = Invitation(guest)
        self.invitation_list.append(invitation)

    def retrieve_invitation(self, email: str) -> Optional["Invitation"]:
        for invitation in self.invitation_list:
            if invitation.guest.email == email:  # clarify
                return invitation
        return None

    def get_guest_by_email(self, email: str) -> Optional["Guest"]:
        for invitation in self.invitation_list:
            if invitation.guest.email == email:
                return invitation.guest

        return None


class Guest:
    def __init__(
        self,
        name: str,
        email: str,
        wedding: Wedding,
        inviting_guest_email: Optional[str] = None,
    ) -> None:
        self.name = name
        self.email = email
        self.wedding = wedding
        self.inviting_guest_email = inviting_guest_email

    def __str__(self) -> str:
        return f"Guest: {self.name} ({self.email})"

    def accept_invitation(self) -> None:
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:
            invitation.accept()
            if self not in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.append(self)

    def decline_invitation(self) -> None:
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:
            invitation.decline()
            if self in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self)


class SpecialGuest(Guest):
    def __init__(self, name: str, email: str, wedding: Wedding) -> None:
        super().__init__(name, email, wedding)
        self.plus_one: Optional[Guest] = None  # clarify

    def __str__(self) -> str:
        return f"Special Guest: {self.name} ({self.email})"

    def invite_plus_one(self, name: str, email: str) -> None:
        if self.plus_one:
            print("Already invited a plus one")
            return

        if not self.wedding.get_guest_by_email(email):
            self.wedding.send_invitation(name, email)
            invitation = self.wedding.retrieve_invitation(email)
            self.plus_one = invitation.guest
            self.plus_one.inviting_guest_email = self.email
            print(f"Plus one invitation sent to {email}")

    def uninvite_plus_one(self) -> None:
        if self.plus_one:
            invitation = self.wedding.retrieve_invitation(self.plus_one.email)
            self.wedding.invitation_list.remove(invitation)

            if self.plus_one in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self.plus_one)

            self.plus_one = None
            print(f"{self.name} has been uninvited to {self.wedding}")


# if __name__ == "__main__":
#     # 1. Create the wedding
#     wedding = Wedding("Alice", "Bob")

#     # 2. Invite a special guest
#     wedding.send_invitation("Jane", "jane@email.com", is_special=True)

#     # 3. Jane invites a plus one
#     jane = wedding.get_guest_by_email("jane@email.com")
#     jane.invite_plus_one("Mark", "mark@email.com")

#     # 4. Mark accepts
#     mark = wedding.get_guest_by_email("mark@email.com")
#     mark.accept_invitation()

#     # 5. Jane uninvites Mark
#     jane.uninvite_plus_one()
