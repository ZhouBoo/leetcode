//
//  30.swift
//  letcode
//
//  Created by zhoubo on 2018/3/29.
//  Copyright © 2018年 zhoubo. All rights reserved.
//
import Foundation

/**
 给定一个字符串 s 和一些长度相同的单词 words，找出 s 与 words 中所有单词（words 每个单词只出现一次）串联一起（words中组成串联串的单词的顺序随意）的字符串匹配的所有起始索引，子串要与串联串完全匹配，中间不能有其他字符。
 
 举个例子，给定：
 ````
 s："barfoothefoobarman"
 words：["foo", "bar"]
 ````
 你应该返回的索引: [0,9]。（任意顺序）
 */
class Solution30 {
    
    func findSubstring(_ s: String, _ words: [String]) -> [Int] {
        let wordLength = words[0].count
        let lenth = wordLength * words.count
        
        // 如果小于总长度 return
        guard lenth <= s.count else { return [] }

        var indexs: [Int] = []
        for index in 0...(s.count - lenth) {
            var contains = true
            // 统计出现了多少个
            var tmpWords = Array(words)
            for subindex in 0..<(words.count) {
                let substringStart =
                    s.index(s.startIndex, offsetBy: index + subindex * wordLength)
                let substringEnd = s.index(substringStart, offsetBy: wordLength)
                let range = substringStart..<substringEnd
                let substring = String(s[range])
                print(substring)
                if let find = tmpWords.index(of: substring) {
                    tmpWords.remove(at: find)
                    continue
                } else {
                    contains = false
                    break
                }
            }

            if contains {
                indexs.append(index)
            }
        }
        
        return indexs
    }
    
    
//    func repeatedSubstringPattern(str: String) -> (Bool, Int) {
//        let length = str.count
//        var next = Array<Int>(repeating: 0, count: length)
//        next[0] = -1
//        var j = -1
//        for index in 1..<length {
//            let iIndex = str.index(str.startIndex, offsetBy: index)
//            let jIndex = str.index(str.startIndex, offsetBy: j + 1)
//            while j >= 0 && str[iIndex] != str[jIndex] {
//                j = next[j]
//            }
//
//            if str[iIndex] == str[jIndex] {
//                j += 1
//            }
//
//            next[index] = j
//        }
//        let lenSub = length - 1 - next[length - 1]
//        return (lenSub != length && length % lenSub == 0, lenSub)
//
//    }

}
