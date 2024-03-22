'''
1~n 수 적힌 카드 뭉치 n개, 중복 없고 순서 무작위.
동전 coin 개

시작
동전은 카드와 교환 가능
카드 1/3 뽑아서 손에 가지기

종료
카드 뭉치에 카드가 없으면
# 카드 뭉치에 카드가 한 장만 남는 경우는 없음. 2의 배수.
라운드 끝날 때 손에서 카드를 못 내면
마지막 라운드는 해당 라운드도 포함됨. 즉, 최소 1라운드는 진행됨.

라운드마다
카드 두 장 뽑기
한 장당 동전 하나로 가지거나, 버리기
카드에 적힌 수 합이 n + 1이 되도록 카드 두 장을 내야 함.


return: 최대로 도달 가능한 라운드 수

알고리즘: 단순 구현 문제
시간 복잡도: 카드 1000개
관건# 
카드는 최상단에서만 뽑을 수 있나? yes


구현 사항
손에 카드 추가하기(initialize)
라운드 진행하기
1. 카드 두 장 뽑기
2. 뽑은 카드 중 동전으로 선택하기
3. 두 카드 합이 n + 1이 되도록 내기
    카드 제출 가능한지 확인하는 함수

    
def submit_card_from_(hand): # 손에서 낼 수 있는 카드 경우의 수가 여러 개인 경우 분기점 발생. dfs 필요.
    # list(map(sum,combinations(hand,2))) # 단순 합으로 최적해 계산 불가.
    return out, hand

'''
from itertools import combinations
def solution(coin, cards):
    round_max = 0
    n = len(cards)
    
    def initialize(cards):
        return cards[:len(cards) // 3], cards[len(cards) // 3:]
    
    def pick_(cards, hand):
        '''
        코인이 1개일 때 어떤 코인을 가져가느냐에 따라 분기점 발생.
        코인은 카드를 사용할 때 감소되는 것으로 하자.
        하지만 어차피 다음턴에 카드 부족으로 종료.
        '''
        if cards:
            hand.extend(cards[:2])
            return hand, cards[2:] # cards가 0이 될 수도 있음.
        return [], []
    
    
    def submit_candidate(hand):
        return [c for c in list(combinations(hand,2)) if sum(c) == n + 1]
    
    def submit_from_(hand, cand):
        # return list(set(hand) - set(cand)) # 순서가 바뀌어 오답 출력. 1시간 소요.
        return [h for h in hand if h not in cand]
            
    def dfs(hand, cards, round_, coin):
        nonlocal round_max, n, coin_stack
        round_ += 1
        hand, cards = pick_(cards, hand) # hand가 0일 수는 없음.
        coin_stack.extend(hand[-2:])
        # print(n + 1, hand, cards, round_, coin_stack, coin)
        if round_max < round_:
            round_max = round_
        if not hand:
            return round_max

        for n_ in submit_candidate(hand):
            used_coin = len((set(n_) & set(coin_stack)))
            if coin < used_coin:
                continue
            coin -= used_coin
            coin_stack = list(set(coin_stack) - set(n_))
            hand = submit_from_(hand, n_)
            round_max = max(round_max, dfs(hand, cards, round_, coin))
            hand = hand[:2]
            coin += used_coin
            coin_stack.extend(list(set(n_) - set(coin_stack)))
        return round_max
            
    hand, cards = initialize(cards)
    coin_stack = []
    out, round_ = n + 1, 0 # 제출한 카드, 진행한 라운드
    answer = dfs(hand, cards, round_, coin)
    return answer