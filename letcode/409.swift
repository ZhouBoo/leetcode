//
//  409.swift
//  letcode
//
//  Created by zhoubo on 2018/5/2.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation


/**
 
 Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
 
 This is case sensitive, for example "Aa" is not considered a palindrome here.
 
 Note:
 Assume the length of given string will not exceed 1,010.
 
 Example:
 ````
 Input:
 "abccccdd"
 
 Output:
 7
 ````
 Explanation:
 One longest palindrome that can be built is "dccaccd", whose length is 7.

 */
class Solution409: SolutionDelegate {
    let test1 = "abccccddaa"
    
    func solution(str: String) -> Int {
        var dict = Dictionary<Character, Int>()
        
        var maxLength = 0
        var flag = 0
        for char in str {
            if let dc = dict[char] {
                dict[char] = dc + 1
            } else {
                dict[char] = 1
            }
        }
        
        for value in dict {
            if value.value % 2 == 0 {
                maxLength += value.value
            } else {
                maxLength += (value.value - 1)
                flag = 1
            }
        }
        
        return maxLength + flag
    }
    
    func runSolution() {
        print(solution(str: test1))
    }

}
