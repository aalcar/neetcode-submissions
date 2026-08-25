class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # create groups by decrementing their counts from a freq hashmap
        counts = Counter(hand)
        sorted_hand = sorted(hand)

        # we'll only use the smallest cards
        # in a sequence if we update
        # counts while iterating
        for card in sorted_hand:
            if card not in counts:
                continue

            for next_card in range(card, card + groupSize):
                if next_card not in counts:
                    return False

                counts[next_card] -= 1

                if counts[next_card] == 0:
                    del counts[next_card]
        
        return True


