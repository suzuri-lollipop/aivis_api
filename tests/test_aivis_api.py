from aivis_api import exception

def test_normal_get_list():
    from aivis_api import get_speakers
    try:
        speakers = get_speakers()
    except Exception as e:
        raise e

def test_normal_list_to_yaml():
    from aivis_api import get_speakers, output_to_yaml
    import os
    try:
        speakers = get_speakers()
        output_to_yaml(speakers)
        os.remove('./speakers.yaml')
    except Exception as e:
        raise e

def test_normal_generate_speech():
    from aivis_api import get_speakers, generate_speech
    try:
        speakers = get_speakers()
        voice = generate_speech("unit test中です", speakers[0]["styles"][0]["id"])
    except Exception as e:
        raise e

def test_normal_play_voice():
    from aivis_api import get_speakers, generate_speech, play_speech
    try:
        speakers = get_speakers()
        voice = generate_speech("unit test中です", speakers[0]["styles"][0]["id"])
        play_speech(voice)
    except Exception as e:
        raise e