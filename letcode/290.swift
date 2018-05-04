//
//  290.swift
//  letcode
//
//  Created by zhoubo on 2018/5/2.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
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
            // 如果之前没有出现过
            if let c = dict[char] {
                if c.elementsEqual(splitStr[index]) {
                    continue
                } else {
                    return false
                }
            } else if set.index(of: splitStr[index]) != nil {
                
                return false
            } else {
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
