//
//  402.swift
//  letcode
//
//  Created by zhoubo on 2018/5/8.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Medium**
 
 Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
 
 Note:
 The length of num is less than 10002 and will be ≥ k.
 The given num does not contain any leading zero.
 Example 1:
 ````
 Input: num = "1432219", k = 3
 Output: "1219"
 Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
 ````
 Example 2:
 ````
 Input: num = "10200", k = 1
 Output: "200"
 Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
 ````
 Example 3:
 ````
 Input: num = "10", k = 2
 Output: "0"
 Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 ````
 */
class Solution402: SolutionDelegate {
    
    //
    func removeKdigits(_ num: String, _ k: Int) -> String {
        guard num.count != k else { return "0" }
        
        let zero = Int("0".unicodeScalars.first!.value)
        let bc = { (c: Character) -> Int in
            return Int(c.unicodeScalars.first!.value) - zero
        }
        
        // 移除右往左起最大的 k 位数
        var removed = 0
        
        var tmpString = num
        var search = tmpString.startIndex
        while removed < k && search != tmpString.endIndex {
            let next = num.index(search, offsetBy: 1)
            if next == tmpString.endIndex {
                break
            }
            
            if bc(tmpString[search]) > bc(tmpString[next]) {
                tmpString.remove(at: search)
                removed += 1
                search = tmpString.startIndex
            } else {
                search = next
            }
        }
        var head = tmpString.startIndex
        // 去 0
        while true {
            if tmpString[head] != "0" || tmpString.count == 1 {
                break
            } else {
                tmpString.remove(at: head)
            }
            head = tmpString.startIndex
        }
        
        // 全重复的时候
        while removed < k {
            tmpString.removeLast()
            removed += 1
        }
        
        return tmpString
    }
    
    func runSolution() {
//        let num = "1432219", k = 3
//        let num = "1111111", k = 3
//        let num = "123456", k = 3
//        let num = "10200", k = 1
//        let num = "10", k = 1
        let num = "112", k = 1
        print(removeKdigits(num, k))
    }
}
