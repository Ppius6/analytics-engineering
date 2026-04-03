class Wedding:
    def __init__(self, bride_name: str, groom_name: str) -> None:
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.confirmed_guest_list: List["Guest"] = []
        self.invitation_list: List["Invitation"] = []

    def send_invitation(self, name: str, email: str, is_special: bool = False) -> None:

        # Check if this email already has an invitation
        for invitation in self.invitation_list:
            if invitation.guest.email == email:
                print(f"Guest with {email} already exists")
                return

        # Create the right type of guest based on is_special flag
        if is_special:
            guest = SpecialGuest(name, email, self)
        else:
            guest = Guest(name, email, self)

        # Wrap the guest in an invitation and add to the list
        new_invitation = Invitation(guest)
        self.invitation_list.append(new_invitation)

    def retrieve_invitation(self, email: str) -> Optional["Invitation"]:
        # Method to retrieve an invitation using the guest's email address.
        # Parameters:
        # - email: The email address of the guest.
        # Returns: The Invitation object if found, otherwise None.
        for invitation in self.invitation_list:  # Iterate through all invitations.
            if invitation.guest.email == email:  # Check if the email matches.
                return invitation  # Return the matching invitation.
        return None  # Return None if no matching invitation is found.

    def get_guest_by_email(self, email: str) -> Optional["Guest"]:
        # Search invitations and return the guest object if found
        for invitation in self.invitation_list:
            if invitation.guest.email == email:
                return invitation.guest
        return None


class Invitation:
    def __init__(self, guest: "Guest") -> None:
        self.guest = guest
        self.status: str = "pending"

    def accept(self) -> None:
        self.status = "accepted"

    def decline(self) -> None:
        self.status = "declined"


class Guest:
    # Complete the implementation of the Guest Class here
    def __init__(
        self,
        name: str,
        email: str,
        wedding: Wedding,
        inviting_guest_email: Optional[str] = None,
    ) -> None:
        # The __init__ method initializes a new instance of the Guest class.
        # Parameters:
        # - name: The name of the guest.
        # - email: The email address of the guest.
        # - wedding: The Wedding object to which the guest is invited.
        # - inviting_guest_email: The email address of the guest who invited this guest (for plus-ones, default is None).
        self.name: str = name  # Instance variable to store the guest's name.
        self.email: str = email  # Instance variable to store the guest's email address.
        self.wedding: Wedding = (
            wedding  # Instance variable to store the associated Wedding object.
        )
        self.inviting_guest_email: Optional[str] = (
            inviting_guest_email  # Email of the guest who invited this guest, if any.
        )

    def accept_invitation(self) -> None:
        # Method for the guest to accept their invitation.
        invitation = self.wedding.retrieve_invitation(
            self.email
        )  # Retrieve the guest's invitation.
        if invitation:  # Check if an invitation exists.
            invitation.accept()  # Mark the invitation as accepted.
            if (
                self not in self.wedding.confirmed_guest_list
            ):  # If the guest is not already confirmed:
                self.wedding.confirmed_guest_list.append(
                    self
                )  # Add the guest to the confirmed guest list.

    def decline_invitation(self) -> None:
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:  # Check if an invitation exists.
            invitation.decline()
            if self in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self)


class SpecialGuest(Guest):
    def __init__(self, name: str, email: str, wedding: "Wedding") -> None:
        super().__init__(name, email, wedding)
        self.plus_one: Optional[Guest] = None

    def invite_plus_one(self, name: str, email: str) -> None:
        if self.plus_one:
            print("Already invited a plus one")
            return

        if not self.wedding.get_guest_by_email(email):
            plus_one_guest = Guest(name, email, self.wedding, self.email)  # one Guest object
            invitation = Invitation(plus_one_guest)                        # wrap it manually
            self.wedding.invitation_list.append(invitation)                # add to wedding
            self.plus_one = plus_one_guest                                 # same object referenced
            print(f"Plus one invitation sent to {email}")

    def uninvite_plus_one(self) -> None:
        # Method to uninvite the special guest's plus-one.
        # Parameters:
        # - self: The SpecialGuest instance.
        if self.plus_one:  # Check if a plus-one exists.
            invitation = self.wedding.retrieve_invitation(
                self.plus_one.email
            )  # Retrieve plus-one's invitation.
            self.wedding.invitation_list.remove(
                invitation
            )  # Remove invitation from wedding list.

            if (
                self.plus_one in self.wedding.confirmed_guest_list
            ):  # If plus-one is in confirmed list.
                self.wedding.confirmed_guest_list.remove(
                    self.plus_one
                )  # Remove plus-one from confirmed list.

            self.plus_one = None  # Reset plus-one reference to None.
