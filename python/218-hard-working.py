class Solution:
    def getSkyline(self, buildings: [[int]]) -> [[int]]:
        sorted_buildings = sorted(buildings, \
            key=lambda x: x[0])
        print(sorted_buildings)
        lastest = {}
        skys = []
        for b in sorted_buildings:
            if lastest is None:
                skys.append([b[0],b[2]])
                # 高度是这个的持续到什么位置
                lastest[b[2]] = b[1]
            else:
                height = b[2]
                if skys[-1:][1] < height:
                    #高楼的情况要记录
                    skys.append([b[0], height])
                    # 清理失效的 lastest
                if lastest[height]:
                    # 如果长度不够就返回
                    if lastest[height] <= b[1]:
                        continue
                lastest[height] = b[1]

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