def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond

def get_start_time(time, proc_time):
    int_proc_time = int(float(proc_time) * 1000)
    return get_time(time) - int_proc_time + 1

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for line in lines:
        time = line.split(' ')
        start_time.append(get_start_time(time[1], time[2][:-1]))
        end_time.append(get_time(time[1]))

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i 번째는 현재 자신의 시작 시간이고, i 이하는 그 이전의 시작 시간이므로 카운트할 필요가 없다.
        for j in range(i, len(lines)):
            if start_time[j] < cur_end_time + 1000:
                cnt += 1
        answer = max(answer, cnt)
    
    return answer
