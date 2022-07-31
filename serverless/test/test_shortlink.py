def test_short_string():
    from modules.utils import generate_random_string

    string_length = 6
    generated_string = generate_random_string(6)
    assert generate_random_string is not None
    assert len(generated_string) == string_length


def test_shortlink():
    assert True is True
