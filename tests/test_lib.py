from kaprekar.lib import try_me

def test_steps_one_longer_than_count():
    count, steps = try_me(1234)
    assert count + 1 == len(steps)

def test_all_same_fails():
    try_me(2222)[1][-1] != 6174
