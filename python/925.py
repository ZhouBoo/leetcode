# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        length = len(name) - 1
        typed_length = len(typed) - 1
        name_index = 0
        typed_index = 0
        result = True
        if length > typed_length:
            return False

        while True:
            if typed_index > typed_length:
                if name_index <= length:
                    result = False
                print("end")
                break
            if name[name_index] == typed[typed_index]:
                print("当前字符匹配 name_index=%d, typed_index=%d", (name_index, typed_index))
                while typed_index <= typed_length and name_index <= length:
                    if name_index + 1 <= length and \
                        typed_index + 1 <= typed_length and \
                        name[name_index + 1] == name[name_index] and \
                        name[name_index + 1] == typed[typed_index + 1]:
                        print("name string 重复 name_index=%d, typed_index=%d", (name_index, typed_index))
                        name_index += 1
                        typed_index += 1
                    elif typed_index + 1 <= typed_length and \
                        name[name_index] == typed[typed_index + 1]:
                        typed_index += 1
                        print("typed string 重复 name_index=%d, typed_index=%d", (name_index, typed_index))
                    else:
                        name_index += 1
                        typed_index += 1
                        break
            else:
                result = False
                break

        return result

name = "saeed"
typed = "ssaaedd"

# name = "alex"
# typed = "aaleex"

# name = "leelee"
# typed = "lleeelee"

# name = "laiden"
# typed = "laiden"

# name = "saeed"
# typed = "ssaaedd"

# name = "saeed"
# typed = "saed"

# name = "plpkoh"
# typed = "plppkkh" # False

# name = "pyplrz"
# typed = "ppyypllr" # False

# name = "vtkgn"
# typed = "vttkgnn" # True

print(Solution().isLongPressedName(name, typed))