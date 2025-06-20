class SystemInstruction:
    def __init__(self, role="tech blogger"):
        self.role = role
        self.content = "You are a tech blogger writing informative and engaging content about cutting-edge technologies."

    def get_system_message(self):
        return {"role": "system", "content": self.content}

    def get_data_payload(self, user_prompt, model="deepseek/deepseek-chat:free"):
        system_message = self.get_system_message()
        data = {
            "model": model,
            "messages": [
                system_message,
                {"role": "user", "content": user_prompt}
            ]
        }
        return data
