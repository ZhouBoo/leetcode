class Solution:
    def getSkyline(self, buildings: [[int]]) -> [[int]]:
        sorted_buildings = sorted(buildings, \
            key=lambda x: x[0])
        print(sorted_buildings)

        # start, end = sorted_buildings[0][0], sorted_buildings[0][1]
        # skys = [sorted[0]]
        # for building in sorted_buildings[1:]:
        #     if start <= building[0] \
        #         and end >= building[2]:
        #         continue
        #     elif start > building[0]:
        #         skys.append([building[0]])
                


if __name__ == "__main__":
    l = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Solution().getSkyline(l)