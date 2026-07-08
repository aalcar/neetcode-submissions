class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos1 + speed1 > pos2 + speed2
        # target - pos = distanceLeft
        # distanceLeft / speed = howLong
        # car1 catches up to car2 if:
        #    howLong is shorter?
        # (target - pos) / speed 

        # (13-1)/2=6, (13-2)/2=5.5, (13-3)/4=2.5, (13-5)/1=8, 
        # (13-4)/3=3, (13-10)/1=3
        
        # go through and create arrival times for all
        # 6, 5.5, 2.5, 8, 3, 3
        # -> 2.5, 3, 3, 5.5, 6, 8
        # (6,1) (5.5,2) (2.5,3) (8,5) (3,4) (3,10)
        # (2.5,3) (3,4) (3,10) (5.5,2) (6,1) (8,5)
        # OR -- sort the positions themselves
        #10, 5, 4, 3, 2, 1
        # 10 (3) -- starts a new fleet1
        # 5 (8) -- starts a new fleet2
        # 4 (3->8) -- gets eaten by fleet2
        # 3 (2.5->8) -- gets eaten by fleet2
        # 2 (5.5->8) -- gets eaten by fleet2
        # 1 (6->8) -- gets eaten by fleet2

        # if closer than most recent fleet,
        #   dont create new fleet
        # else:
        #   create new fleet
        # its just a stack

        # sort in descending order
        # create a fleets stack
        # for pos in position:
        #   timeTaken = (target - pos) / speed
        #   if no fleet, add to fleets
        #   else if time of fleet ahead >= your time, get consumed
        #   else, start a new fleet -- add to stack
        # return length of stack

        # (4, 2) time_taken = 3 
        # (1, 3) time_taken = 3

        count = max_time = 0

        cars = list(zip(position, speed))
        descending = sorted(cars, reverse=True)
        for car in descending:
            car_pos, car_speed = car
            time_taken = (target - car_pos) / car_speed

            if max_time < time_taken:
                max_time = max(max_time, time_taken)
                count += 1

        return count
        