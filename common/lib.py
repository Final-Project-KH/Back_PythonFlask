import random
import string


# 기타 유틸 함수
def validate_required_fields(json_data: dict) -> bool:
    """
    요청 JSON 데이터에서 필수 필드가 모두 존재하는지 검증합니다.
    :param json_data: 요청 JSON 데이터
    :return: 필수 필드가 모두 존재하면 True, 아니면 False
    """
    required_fields = ["code", "codeLanguage", "questionId", "memberId"]
    if not json_data:
        return False

    missing_fields = [field for field in required_fields if json_data.get(field) is None]
    return not missing_fields


def get_random_string(length: int = 8) -> str:
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))