def shap2lower(string):
    return string.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def str2int(string):
    return int(string[:2]) * 60 + int(string[3:])

def solution(m, musicinfos):
    answer = ''
    plays = []
    
    for info in musicinfos:
        info = info.split(',')
        
        time = str2int(info[1]) - str2int(info[0])
        title = info[2]
        score = shap2lower(info[3])
        
        if time >= len(score):
            q, r = divmod(time, len(score))
            score = score * q + score[:r]
        else:
            score = score[:time]
        
        plays.append([time, title, score])
    
    m = shap2lower(m)
    
    for play in sorted(plays, key=lambda x: -x[0]):
        if m in play[2]:
            answer = play[1]
            break
    
    return answer if answer else '(None)'
