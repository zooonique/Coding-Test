from collections import deque

def solution(enter, leave):
    answer = [0] * len(enter)
    
    room = deque([])
    enter = deque(enter)
    leave = deque(leave)
    
    # 첫 번째 입실
    room.append(enter.popleft())
    empty = 0
    trash = []
    
    # 퇴실객이 모두 나가면 반복문 종료
    while leave:
        # 퇴실객 검색 - 퇴실할 사람이 방에 없으면,
        if leave[0] not in room:
            # 기존에 방에 있던 사람은 trash 리스트에 있던 사람을 만났기에 해당 인원을 더해주고 trash는 0으로 초기화
            for r in room:
                answer[r-1]+=len(trash)
            # enter queue에서 한 명씩 입실
            room.append(enter.popleft())
            empty=0
            trash = []
            
        else:
            # 퇴실할 사람이 방에 있으면, 방에서 퇴실
            room.remove(leave[0])
            # 입실할 때마다 empty를 0으로 초기화하고, 퇴실의 연속일 경우에는 초기의 len(room)이 가장 늦게 나가는 사람의 만났던 사람의 수를 고려한 경우이다.
            if empty == 0:
                empty = len(room)
            
            # 퇴실할 때, 방에 있었던 사람들의 수는 만났던 사람
            answer[leave[0]-1] += empty
            
            # 완전히 퇴실한 사람을 trash list에 저장
            trash.append(leave.popleft())   
    
    return answer
