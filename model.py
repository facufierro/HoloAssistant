import json
import openai

class AssistantManager:
    def __init__(self):
        print("Initializing AssistantManager")
        self.id = self.load()
        print(f"Loaded ID: {self.id}")

    def create(self, name: str, model: str, instructions: str):
        print(f"Creating assistant with name={name}, model={model}")
        self.client = openai.OpenAI()
        self.name = name
        self.model = model
        self.instructions = instructions
        if self.id is None:
            print("No ID found, creating new assistant")
            self.assistant = self.client.beta.assistants.create(
                name=self.name,
                model=self.model,
                instructions=self.instructions
            )
            self.id = self.assistant.id
            print(f"New assistant created with ID: {self.id}")
            self.save()

    def load(self):
        try:
            with open('assistant_data.json', 'r') as file:
                data = json.load(file)
                return data.get('id')
        except FileNotFoundError:
            print("FileNotFoundError: 'assistant_data.json' not found.")
            return None
        except json.JSONDecodeError:
            print("JSONDecodeError: Error decoding JSON from file.")
            return None

    def save(self):
        data = {'id': self.id}
        with open('assistant_data.json', 'w') as file:
            json.dump(data, file)
        print("Assistant ID saved")

    def __repr__(self):
        return f"<AssistantManager name={self.name}>"
