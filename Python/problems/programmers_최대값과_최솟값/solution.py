# 프로그래머스 - 최댓값과 최솟값
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numbers = list(map(int, s.split()))

    return f"{min(numbers)} {max(numbers)}"
