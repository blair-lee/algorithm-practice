def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당한 경우
    for i in range(n+1):
        if (i in lost) and (i in reserve):
            lost.remove(i)
            reserve.remove(i)
            
    for i in range(n+1):
        if i in lost:
            # 앞번호의 학생이 여벌을 가지고 있는 경우
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            # 뒷번호의 학생이 여벌을 가지고 있는 경우
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)
                
    answer = n - len(lost)
    
    return answer