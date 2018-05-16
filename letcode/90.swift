//
//  90.swift
//  letcode
//
//  Created by zhoubo on 2018/5/16.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Medium**
 
 Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
 
 Note: The solution set must not contain duplicate subsets.
 
 Example:
 
 Input: [1,2,2]
 Output:
 [
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
 ]
 */
class Solution90: SolutionDelegate {
    
    func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
        //        let total = pow(Decimal(2), nums.count) // shiting leetcode cant compile
        let sortNums = nums.sorted()
        let count = nums.count
        let total = Int(pow(Double(2), Double(count)))
        var result = Array<Array<Int>>()
        var distinctSet = Set<String>()
        
        let char1 = Character("1")
        for i in 0..<total {
            var temp = [Int]()
            let s = String(fullBinary: i)
            
            let length = s.count
            for j in 0..<count {
                if j < length {
                    let end = s.index(s.endIndex, offsetBy: -j - 1)
                    if s[end] == char1 {
                        temp.append(sortNums[count - 1 - j])
                    }
                }
            }
            
            let ds = temp.reduce("") { (str, value) -> String in
                return "\(str)-\(value)"
            }
            
            print(ds)
            if distinctSet.contains(ds){
                continue
            } else {
                distinctSet.insert(ds)
                result.append(temp)
            }
        }
        
        return result
    }
    
    
    func runSolution() {
        let nums = [1,2,2]
//        let nums = [1,2,3,4,5,6,7,8,10,0]
        let r = self.subsetsWithDup(nums)
        debugPrint(r)
        debugPrint(r.count)
    }
}

extension String {
    init<B: FixedWidthInteger>(fullBinary value: B) {
        self = value.words.reduce(into: "") {
            $0.append(String($1, radix: 2))
        }
    }
}
