class StockSpanner:

    def __init__(self):
        self.price_walls = []
        self.stocks = 0

    def next(self, price: int) -> int:
        # adding price and returning span
        # iterating right, looking left for nearest greatest element
        # [100] -> 1
        # [100, 80] -> 1
        # [100, 80, 60] -> 1
        # [100, 80, 60, 70] -> 2
        # [100, 80, 60, 70, 60] -> 1
        # [100, 80, 60, 70, 60, 75] -> 4
        # [100, 80, 60, 70, 60, 75, 85] -> 6

        # [100, 80, 75
        #  makes sense but we need some way to track the count
        # its not BASED on pops. just keep tuples of index?
        # 1 + the amount of stuff popped?
        # [1, 2, 3, 4, 5, 6, 7]
        self.stocks += 1
        if not self.price_walls or self.price_walls[-1][0] > price:
            self.price_walls.append((price, self.stocks))
            return 1
        else:
            while self.price_walls and self.price_walls[-1][0] <= price:
                print("Popping ", self.price_walls, " Stock#: ", self.stocks)
                self.price_walls.pop()
            
            if self.price_walls:
                ans = self.stocks - self.price_walls[-1][1]
            else:
                ans = self.stocks
                
            self.price_walls.append((price, self.stocks))
            return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)