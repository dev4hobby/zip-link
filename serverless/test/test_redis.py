from modules.redis import get_redis

redis = get_redis()


def test_redis_connection():
    """
    Redis 연결 테스트
    """
    assert redis.get_ping() is True


def test_redis_set_get():
    """
    Redis set/get 테스트
    """
    key = "test_redis_set"
    value = "test_redis_set_value"
    response = redis._set(key, value)
    assert response == {"key": key, "value": value}
    assert redis.get(key) == value


def test_redis_setex_get():
    """
    Redis setex/get 테스트
    """
    import time

    key = "test_redis_setex"
    value = "test_redis_setex_value"
    response = redis.setex(key, value, 2)
    assert response == {"key": key, "value": value}
    assert redis.get(key) == value
    time.sleep(3)
    assert redis.get(key) is ""
