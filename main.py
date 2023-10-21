from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path, language):
    """
    Функция принимает путь к файлу и язык звуковой дорожки,
    сохраняет аудиофайл, возвращает сообщение.
    """
    if not Path(file_path).is_file():
        raise FileNotFoundError('Указан неверный путь к файлу!')
    if Path(file_path).suffix != '.pdf':
        raise Exception('Файл имеет неверный тип!')
    print(f'[+] Original file: {Path(file_path).name}')
    print('[+] Processing ...')
    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        # Пробегаемся по страницам, извлекая текст из каждой
        pages = [page.extract_text() for page in pdf.pages]
    # Объединяем страницы, удаляя переносы строки
    text = ''.join(pages)
    text = text.replace('\n', '')
    # Формируем аудиофайл
    my_audio = gTTS(text=text, lang=language, slow=False)
    file_name = Path(file_path).stem
    my_audio.save(f"{file_name}.mp3")
    return f'[+] {file_name}.mp3 успешно сохранён!\n---Хорошего дня!---'

def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input('\nВведите путь к файлу: ')
    language = input('Выбирите язык, пример "en" или "ru": ')
    try:
        print(pdf_to_mp3(file_path=file_path, language=language))
    except Exception as err:
        print(f'Возникло искючение с сообщением: "{err}"')

if __name__ == '__main__':
    main()
