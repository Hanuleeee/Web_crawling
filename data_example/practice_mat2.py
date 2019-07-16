# 126명 야구선수에 대한 기록 baseball_data.txt
# columns = 안타, 홈런, 볼넷, 삼진, 도루, 타율  // 구분자는 ,사용
# 데이터를 numpy array로 불러온 후, 다음의 계산을 수행하고 plotting할 것
# - 음수값을 0의로 대체
# - 홈런 수가 1 이상인 행만 남기기
# - 세가지 비율을 계산 : '홈런/안타' , '볼넷/안타', '삼진/안타'
# - 두가지 plotting을 수행
    # - x축 좌표 '홈런/안타', y축 좌표 '볼넷/안타'  : 'rx'스타일 사용
    # - x축 좌표 '홈런/안타', y축 좌표 '삼진/안타'  : 'b.'스타일 사용

import numpy as np
from matplotlib import pyplot as plt

baseball = np.loadtxt('baseball_data.txt', delimiter= ",")
baseball[baseball < 0]=0
baseball = baseball[baseball[:,1] > 0]

# hr_per_h = baseball[:,1] /baseball[:,0]
# b_per_h = baseball[:,2]/baseball[:,0]
# tr_per_h = baseball[:,3]/baseball[:,0]
# 이렇게 하면 귀찮으니까 다른방법으로!!

h,hr,b,th,sb, avg = baseball.T #축 바꿈
hr_per_h = hr/h
b_per_h = b/h
th_per_h = th/h

hr_per_h /= np.max(hr_per_h)  ##그래서 이게 뭐라고??
b_per_h /= np.max(b_per_h)
th_per_h /= np.max(th_per_h)

plt.plot(hr_per_h, b_per_h,'rx')
plt.plot(hr_per_h, th_per_h,'b.')

plt.show()

