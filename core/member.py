from playwright.sync_api import Page

class MemberListener:
    def __init__(self, page: Page, on_member_join, on_member_leave):
        self.page = page
        self.on_member_join = on_member_join
        self.on_member_leave = on_member_leave

    def get_members(self):
        """Retrieve the list of participants in the meeting."""
        try:
            # Wait for the participant list element to be present
            self.page.wait_for_selector('div[role="list"]', timeout=20000)

            # Evaluate the DOM to get participants if the element is found
            return self.page.evaluate('''
                () => {
                    const memberList = document.querySelector('div[role="list"]');
                    if (!memberList) {
                        return null;  // Return null if the element isn't found
                    }
                    const members = {};
                    Array.from(memberList.children).forEach(member => {
                        members[member.innerText] = true;
                    });
                    return members;
                }
            ''')
        except Exception as e:
            print(f"Error finding member list: {e}")
            return {}

    def listen_for_participants(self):
        """Monitors participant join/leave events."""

        # Step 1: Click on the "People" button to open the participant list
        try:
            self.page.get_by_label("People").click()  # Simulates clicking the "People" tab to show participants
            print("Clicked on 'People' to open the participant list.")
        except Exception as e:
            print(f"Error clicking on 'People' button: {e}")
            return

        # Step 2: Get the initial list of participants
        old_members = self.get_members()

        if old_members is None:
            print("Member list is not available.")
            return  # Exit early if no member list is found

        def check_membership():
            new_members = self.get_members()
            if new_members is None:
                return  # Exit early if no member list is found

            # Trigger callback for members who have joined
            for member in new_members:
                if member not in old_members:
                    self.on_member_join(member)
            
            # Trigger callback for members who have left
            for member in old_members:
                if member not in new_members:
                    self.on_member_leave(member)
            
            # Update the old members list
            old_members.update(new_members)

        # Step 3: Attach the MutationObserver to watch for changes in the participant list
        try:
            self.page.evaluate('''
                const memberList = document.querySelector('div[role="list"]');
                if (memberList) {
                    new MutationObserver(() => {
                        window.checkMembership();
                    }).observe(memberList, { subtree: true, childList: true });
                } else {
                    console.log("Participant list not found, cannot attach observer.");
                }
            ''')
            print("Member listener attached.")
        except Exception as e:
            print(f"Error attaching MutationObserver: {e}")
            return
