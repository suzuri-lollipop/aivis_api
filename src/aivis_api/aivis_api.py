from .exception import *

def generate_speech(text, speaker=0):
    import json
    import requests
    """Aivis Speech Engine APIを使って音声を生成する関数"""
    url = "http://127.0.0.1:10101/audio_query"
    params = {"text": text, "speaker": speaker}

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        query = response.json()

        url = "http://127.0.0.1:10101/synthesis"
        params = {"speaker": speaker}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(query), params=params, headers=headers)
        response.raise_for_status()

        return response.content  # 音声データを返す

    except requests.exceptions.RequestException as e:
        raise AivisSpeechGenerationError(f"APIリクエストエラー: {e}")
    except json.JSONDecodeError as e:
        raise AivisSpeechGenerationError(f"JSONデコードエラー: {e}")
    except Exception as e:
        raise AivisSpeechGenerationError(f"音声生成中の予期せぬエラー: {e}")


def play_speech(audio_data):
    """音声データを再生する関数"""
    try:
        import io
        import soundfile as sf
        import sounddevice as sd
        data, samplerate = sf.read(io.BytesIO(audio_data))
        sd.play(data, samplerate)
        sd.wait()
    except sf.SoundFileError as e:
        raise AivisSpeechPlaybackError(f"音声ファイルエラー: {e}")
    except Exception as e:
        raise AivisSpeechPlaybackError(f"音声再生中の予期せぬエラー: {e}")

def get_speakers():
    import os
    import requests
    """Aivis Speech Engineの利用可能な話者リストを取得する"""
    port = int(os.environ.get("AIVIS_SPEECH_PORT", "10101"))
    base_url = f"http://127.0.0.1:{port}"
    speakers_url = f"{base_url}/speakers"

    try:
        response = requests.get(speakers_url)
        response.raise_for_status()
        speakers = response.json()
        return speakers
    except requests.exceptions.RequestException as e:
        print(f"話者リスト取得エラー: {e}")
        return None

def output_to_yaml(speakers, filename="speakers.yaml"):
    """話者リストをYAMLファイルに出力する"""
    import yaml
    if speakers:
        try:
            with open(filename, "w", encoding="utf-8") as f: #encodingを指定
                yaml.dump(speakers, f, indent=4, allow_unicode=True) #allow_unicodeを指定
            print(f"話者リストを{filename}に出力しました。")
        except Exception as e:
            print(f"YAMLファイル出力エラー: {e}")
    else:
        print("出力する話者リストがありません。")