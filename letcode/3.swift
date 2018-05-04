//
// Created by zhoubo on 2018/5/3.
// Copyright (c) 2018 zhoubo. All rights reserved.
//

import Foundation

class Solution3: SolutionDelegate {
    
    /**
     给定一个字符串，找出不含有重复字符的最长子串的长度。
     
     示例：
     ````
     给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
     
     给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
     
     给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
     ````
     
     */
    func soluction(s: String) -> Int {
        guard s.count > 1 else {
            return s.count
        }
        var begin = s.startIndex
        var search = s.index(begin, offsetBy: 1)
        
        var maxlength = 0
        
        var subString: String = String(s[begin..<search])
        var looplength = 1
        
        while search < s.endIndex {
            
            // 有重复
            if let _ = subString.index(of: s[search]) {
                maxlength = max(maxlength, looplength)
               // 首地址和重复字符地址不同就跳过
                while (s[begin] != s[search] && begin <= search) {
                    begin = s.index(begin, offsetBy: 1)
                    subString = String(s[begin..<search])
                }
                
                if (begin != search) {
                    begin = s.index(begin, offsetBy: 1)
                    subString = String(s[begin..<search])
                }
                looplength = search.encodedOffset - begin.encodedOffset
                
            } else {
                // 没有重复
                looplength += 1
                search = s.index(search, offsetBy: 1)
                subString = String(s[begin..<search])
            }
        }
        
        return max(maxlength, looplength)
    }
    
    func runSolution() {
        print(soluction(s: text))
    }
    
    let text = "au"
}
