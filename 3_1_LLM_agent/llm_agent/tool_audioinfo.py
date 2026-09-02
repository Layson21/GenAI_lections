# llm_agent/tool_audioinfo.py

from mutagen import File


class AudioInfoTool:
    """Инструмент для получения метаданных аудиофайла."""

    name = "audio_info"
    description = "Возвращает длительность, битрейт, количество каналов и частоту дискретизации аудиофайла."

    def use(self, file_path: str) -> str:
        """
        Принимает путь к аудиофайлу и возвращает его основные параметры.

        Args:
            file_path (str): Путь к аудиофайлу, например "music.mp3".

        Returns:
            str: Строка с информацией об аудиофайле или сообщением об ошибке.
        """
        try:
            audio = File(file_path)

            if audio is None or audio.info is None:
                return f"Ошибка: не удалось открыть аудиофайл '{file_path}'."

            info = audio.info

            return (
                f"Файл: {file_path}\n"
                f"Длительность: {info.length:.2f} сек.\n"
                f"Битрейт: {getattr(info, 'bitrate', 'неизвестно')} бит/с\n"
                f"Каналы: {getattr(info, 'channels', 'неизвестно')}\n"
                f"Частота дискретизации: {getattr(info, 'sample_rate', 'неизвестно')} Гц"
            )

        except Exception as e:
            return f"Ошибка при чтении аудиофайла '{file_path}': {e}"