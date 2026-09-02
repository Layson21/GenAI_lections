# main.py

from llm_agent.core_v2 import LLMAgent

def main():
    """Основная функция для запуска агента."""
    print("Простой LLM-агент с инструментами ('Калькулятор', 'Поиск в DuckDuckGo')")
    print("-" * 70)

    #agent = LLMAgent(model = "qwen/qwen3-next-80b-a3b-instruct:free")

    agent = LLMAgent(local = True, ollama_model = "hf.co/unsloth/Qwen3.5-4B-GGUF:Q4_K_S") #ollama_base_url = "10.10.34.24:5678"

    query = "Узнай информацию о аудиофайле по пути 'F:/Documents/Учеба/Университет/7 семестр/parallel/lab1/music/sample.mp3'"

    print(f"Ваш запрос: {query}")
    print("-" * 70)

    response = agent.process_query(query)

    print("\n" + "=" * 70)
    print("Финальный ответ агента:\n")
    print(response)
    print("=" * 70)

if __name__ == "__main__":
    main()
