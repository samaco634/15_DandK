#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
import math
np.set_printoptions(threshold='nan')

# 소수 판정 함수
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# 소수 생성 함수 
def prime_number_generater(nstart, nsize):
    nend = nstart + nsize
    ay   = np.arange(nstart, nend)
    # 소수 판정 함수 벡터화
    pvec = np.vectorize(is_prime)
    # 배열 요소에 적용
    primes_t = pvec(ay)
    # 소수만 추출하여 표시
    primes = np.extract(primes_t, ay)
    return primes

if __name__ == '__main__':
    p = sys.stdin.read().split(",")
    print p
    print prime_number_generater(int(p[0]),int(p[1]))
    

