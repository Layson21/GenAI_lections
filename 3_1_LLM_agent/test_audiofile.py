# test_audioinfo.py

import unittest
from llm_agent.tool_audioinfo import AudioInfoTool
from llm_agent.core_v2 import LLMAgent


class TestAudioInfoTool(unittest.TestCase):

    def setUp(self):
        self.tool = AudioInfoTool()

    def test_valid_file(self):
        result = self.tool.use("F:/Documents/Учеба/Университет/7 семестр/parallel/lab1/music/sample.mp3")
        self.assertIsInstance(result, str)

    def test_invalid_file(self):
        result = self.tool.use("not_found.mp3")
        self.assertIn("Ошибка", result)

    def test_empty_path(self):
        result = self.tool.use("")
        self.assertIn("Ошибка", result)

    def test_agent(self):
        agent = LLMAgent(
            local=True,
            ollama_model="hf.co/unsloth/Qwen3.5-4B-GGUF:Q4_K_S"
        )

        query = "Узнай информацию о аудиофайле по пути './music/sample.mp3'"

        response = agent.process_query(query)

        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")


def run_tests():
    unittest.main()


if __name__ == "__main__":
    run_tests()