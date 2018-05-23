//
//  290.swift
//  letcode
//
//  Created by zhoubo on 2018/5/2.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Easy**
 
 * **单词模式**
 * - pattern = "abba", str = "dog cat cat dog", 返回true
 * - pattern = "abba", str = "dog cat cat fish", 返回false.
 * - pattern = "aaaa", str = "dog cat cat dog" , 返回false.
 * - pattern = "abba", str = "dog dog dog dog" , 返回false.
 */
class Solution290: SolutionDelegate {
    
    let pattern = "abba"
//    let str = "dog cat cat dog"
//    let str = "dog cat cat fish"
    let str = "dog dog dog dog"
    
    func wordPattern(pattern: String, str: String) -> Bool {
        let splitStr = str.components(separatedBy: " ")
        guard splitStr.count == pattern.count else { return false }
        
        var dict = Dictionary<Character, String>()
        var set = Set<String>()
        
        for (index, char) in pattern.enumerated() {
            // 如果之前出现过
            if let c = dict[char] {
                // 是不是相等的
                if c.elementsEqual(splitStr[index]) {
                    continue
                } else {
                    return false
                }
            } else if set.index(of: splitStr[index]) != nil {
                // 没出现过也要看是不是对应关系是否是一对一的，不是也返回
                return false
            } else {
                //没出现过的直接添加 dict 和 set 中
                dict[char] = splitStr[index]
                set.insert(splitStr[index])
            }
        }
        
        return true
    }
    
    func runSolution() {
        print(self.wordPattern(pattern: pattern, str: str))
    }
    
}
