from cog import BasePredictor, Input
from generator.gpt2.gpt2_generator import GPT2Generator

class Predictor(BasePredictor):
    def setup(self):
        self.generator = GPT2Generator()

    # /n is a hack to get multi line input
    def predict(self, prompt: str = Input(default="\n")) -> str:
        return self.generator.generate(prompt)
