//
//  78.swift
//  letcode
//
//  Created by zhoubo on 2018/5/16.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation
/**
 **Medium**
 
 Given a set of distinct integers, nums, return all possible subsets (the power set).
 
 Note: The solution set must not contain duplicate subsets.
 
 Example:
 ````
 Input: nums = [1,2,3]
 Output:
 [
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
 ]
 ````
 */

class Solution78: SolutionDelegate {
    
    func subsets(_ nums: [Int]) -> [[Int]] {
//        let total = pow(Decimal(2), nums.count) // shiting leetcode cant compile
        let total = Int(pow(Double(2), Double(nums.count)))
        var result = Array<Array<Int>>()
        let char1 = Character("1")
        for i in 0..<total {
            var temp = [Int]()
            let s = String(fullBinary: i)
            print(s)
            let length = s.count
            for j in 0..<nums.count {
                if j < length {
                    let end = s.index(s.endIndex, offsetBy: -j - 1)
                    if s[end] == char1 {
                        temp.append(nums[nums.count - 1 - j])
                    }
                }
            }
            
            result.append(temp)
        }
        return result
    }
    
    
    
    func runSolution() {
        let nums = [1,2,3,4]
        print(self.subsets(nums))
    }
}
