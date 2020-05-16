#   复原IP地址
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

# 示例:

# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s: str):
        total_list = []
        self.resolve('', s, total_list, 1)
        return total_list

    def resolve(self, resolved: str, remain: str, total_list: [str], count: int):
        if count > 4:
            print('4:', resolved, remain)
            if len(remain) > 0:
                return
            else:
                total_list.append(resolved)

        for read in range(1, 4):
            if len(remain) > read - 1 and int(remain[0: read]) <= 255:
                if read > 1 and remain[0] == '0':
                    return
                r1 = ''
                if resolved:
                    r1 = resolved + '.' + remain[0: read]
                else:
                    r1 += remain[0: read]
            
                # print('r', read, ':', r1, count)
                if len(remain) >= read:
                    self.resolve(r1, remain[read:], total_list, count + 1)
                else:
                    return

        # if len(remain) > 0 and int(remain[0]) <= 255:
        #     r1 = ''
        #     if resolved:
        #         r1 = resolved + '.' + remain[0]
        #     else:
        #         r1 += remain[0]
            
        #     print('r1:', r1, count)
        #     if len(remain) > 1:
        #         self.resolve(r1, remain[1:], total_list, count + 1)
        #     else:
        #         if count == 5:
        #             total_list.append(resolved)
        #         return
                
        # if len(remain) > 1 and int(remain[0:2]) <= 255:
        #     r2 = ''
        #     if resolved:
        #         r2 = resolved + '.' + remain[0:2]
        #     else:
        #         r2 += remain[0:2]
        #     print('r2:', r2, count)
        #     if len(remain) > 2:
        #         self.resolve(r2, remain[2:], total_list, count + 1)
        #     else:
        #         if count == 5:
        #             total_list.append(resolved)
        #         return
            
        # if len(remain) > 2 and int(remain[0:3]) <= 255:
        #     r3 = ''
        #     if resolved:
        #         r3 = resolved + '.' + remain[0:3]
        #     else:
        #         r3 += remain[0:3]
        #     print('r3:', r3, count)
        #     if len(remain) > 3:
        #         self.resolve(r3, remain[3:], total_list, count + 1)
        #     else:
        #         if count == 5:
        #             total_list.append(resolved)
        #         return


# print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("010010"))