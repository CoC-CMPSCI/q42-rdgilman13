import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_weight_le2_dist_le500():
    # weight=1.5, distance=300 -> rate=1.10, dist<=500 -> charge=1.10
    content = open('result1.txt').read()
    print(content)
    regex_test([r'1\.10'], content)


@pytest.mark.T2
def test_weight_le6_dist_gt500():
    # weight=5, distance=1000 -> rate=2.20, dist>500 -> charge=(1000/500)*2.20=4.40
    content = open('result2.txt').read()
    print(content)
    regex_test([r'4\.40'], content)


@pytest.mark.T3
def test_weight_le20_dist_gt500():
    # weight=15, distance=2500 -> rate=4.80, dist>500 -> charge=(2500/500)*4.80=24.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'24\.0[0-9]'], content)


@pytest.mark.T4
def test_invalid_weight():
    # weight=25 -> invalid weight
    content = open('result4.txt').read()
    print(content)
    regex_test([r'[Ii]nvalid'], content)
