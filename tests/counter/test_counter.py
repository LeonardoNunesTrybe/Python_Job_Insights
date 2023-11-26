from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word_to_count_1 = 'Python'
    word_to_count_2 = 'Javascript'
    assert count_ocurrences(path, word_to_count_1) == 1
    assert count_ocurrences(path, word_to_count_2) == 1
