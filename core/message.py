class MessageListener:
    def __init__(self, page, on_message):
        self.page = page
        self.on_message = on_message

    def listen_for_messages(self):
        """Listens for new chat messages."""

        # Step 1: Ensure the chat window is open
        try:
            chat_button = self.page.wait_for_selector('button[aria-label="Chat with everyone"]', timeout=10000)
            if chat_button:
                chat_button.click()
                print("Chat window opened.")
            else:
                print("Chat button not found!")
                return
        except Exception as e:
            print(f"Error opening chat window: {e}")
            return

        # Step 2: Now, wait for the chat container to become visible
        try:
            chat_container = self.page.wait_for_selector('div[jsname="xyj4V"]', timeout=10000)
            if not chat_container:
                print("Chat container not found, cannot attach message listener.")
                return

            self.page.evaluate('''
                const getRecentMessage = () => {
                    const chat = document.querySelector('div[jsname="xyj4V"]').lastChild;
                    if (chat) {
                        return {
                            author: chat.querySelector('.author-selector').innerText,
                            content: chat.querySelector('.content-selector').innerText
                        };
                    }
                    return null;
                };

                const messageObserver = new MutationObserver(() => {
                    const message = getRecentMessage();
                    if (message && message.author !== "You") {
                        window.messageListener(message);
                    }
                });

                const chatContainer = document.querySelector('div[jsname="xyj4V"]');
                if (chatContainer) {
                    messageObserver.observe(chatContainer, { subtree: true, childList: true });
                    console.log('Message observer attached.');
                } else {
                    console.log('Chat container not found in evaluate.');
                }
            ''')
        except Exception as e:
            print(f"An error occurred while attaching the message listener: {e}")
            return
