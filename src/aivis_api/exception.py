class AivisSpeechGenerationError(Exception):
    """Aivis Speechの音声生成に関するエラー"""
    pass

class AivisSpeechPlaybackError(Exception):
    """Aivis Speechの音声再生に関するエラー"""
    pass

class AivisSpeechModelGetError(Exception):
    """Aivis Speechのモデル取得に関するエラー"""
    pass