class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1,len(coordinates)-1):
            prev_point = coordinates[i-1]
            curr_point = coordinates[i]
            next_point = coordinates[i+1]

            if (curr_point[1]-prev_point[1])*(curr_point[0]-next_point[0] )!= (curr_point[1]-next_point[1])*(curr_point[0]-prev_point[0]):
                return False
        return True
