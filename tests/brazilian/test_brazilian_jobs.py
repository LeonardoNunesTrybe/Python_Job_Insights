from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert isinstance(path, list)
    assert all(isinstance(item, dict) for item in path)

    keys = path[0].keys() if path else []
    expected_keys = {"title", "salary", "type"}

    assert all(key in expected_keys for key in keys)