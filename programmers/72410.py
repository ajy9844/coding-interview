import re

def solution(new_id):
    st = new_id.lower()
    st = re.sub('[^a-z0-9-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if not st else st
    if len(st) >= 16: 
        st = st[:15]
        if st.endswith('.'): 
            st = st[:-1]
    while len(st) <= 2: 
        st += st[-1]
    
    return st
