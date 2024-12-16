from aivis_api import *

if __name__ == "__main__":
    
    text = "こんにちは、私のチャンネルへようこそ！"
    speaker_id = 888753760

    try:
        audio_data = generate_speech(text, speaker_id)
        play_speech(audio_data)

    except Exception as e:
        raise e

    print("処理終了")