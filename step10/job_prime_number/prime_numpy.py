#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import math
np.set_printoptions(threshold='nan')


# 소수 판정 함수 
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


# 배열에 1부터 차례대로 숫자를 배치
nstart = eval(os.environ.get("A_START_NUM"))
nsize  = eval(os.environ.get("A_SIZE_NUM"))
nend   = nstart + nsize
ay     = np.arange(nstart, nend)

# 소수 판정 함수를 벡터화
pvec = np.vectorize(is_prime)

# 배열 요소에 적용
primes_tf = pvec(ay)

# 소수만 추출하여 표시
primes = np.extract(primes_tf, ay)
print primes


