class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_map = Counter(hand)
        cards = list(card_map.keys())
        heapq.heapify(cards)
        print(cards)
        while cards:
            current_card = cards[0]
            for i in range(groupSize):
                if card_map[current_card + i] == 0:
                    return False
                
                card_map[current_card + i] -=1
                if card_map[current_card + i] == 0:
                    if current_card + i != heapq.heappop(cards):
                        return False
        return True



        