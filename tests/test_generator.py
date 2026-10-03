from buzz.generator import sample, generate_buzz


def test_sample_single_word():
    words = ["a", "b"]
    assert sample(words) in words


def test_sample_multiple_words():
    words = ["a", "b", "c"]
    for _ in range(10):
        assert sample(words) in words


def test_generate_buzz_of_at_least_five_words():
    phrase = generate_buzz()
    assert len(phrase) >= 5
