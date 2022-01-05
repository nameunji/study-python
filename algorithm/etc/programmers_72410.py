"""
programmers : 신규 아이디 추천
문제 링크 https://programmers.co.kr/learn/courses/30/lessons/72410
"""
from re

import re


def solution(new_id):
    # 1 - 소문자로 치환
    new_id = new_id.lower()

    # 2 - 소문자, 숫자, -, _, . 를 제외한 모든 문자 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3 - 마침표(.)가 2번이상 연속된 부분 1개로 치환
    new_id = re.sub('\.{2,}', '.', new_id)

    # 4 - 마침표(.)가 처음, 끝에 위치할 시 제거
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]

    # 5 - 빈문자열 시, 'a' 대입
    if new_id == '':
        new_id = 'a'

    # 6 - 16자 이상 시, 첫 15개 제외한 나머지 문자 제거, 만약 제거 후 마침표가 끝에 위치할 시 마침표 문자 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7 - 2자 이하 시, 마지막 문자를 길이가 3이 될 때까지 반복
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id