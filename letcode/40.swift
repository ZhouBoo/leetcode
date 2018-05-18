//
//  40.swift
//  letcode
//
//  Created by zhoubo on 2018/5/17.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Medium**
 
 Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
 
 Each number in candidates may only be used once in the combination.
 
 Note:
 
 All numbers (including target) will be positive integers.
 The solution set must not contain duplicate combinations.
 
 
 Example 1:
 ````
 Input: candidates = [10,1,2,7,6,1,5], target = 8,
 A solution set is:
 [
 [1, 7],
 [1, 2, 5],
 [2, 6],
 [1, 1, 6]
 ]
 ````
 Example 2:
 ````
 Input: candidates = [2,5,2,1,2], target = 5,
 A solution set is:
 [
 [1,2,2],
 [5]
 ]
 ````
 */
class Solution40: SolutionDelegate {
    
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var sortNums = candidates.filter({ (value) -> Bool in
            return value <= target
        }).sorted()
        print(sortNums.count)
        
        var temp = Array<Int>()
        var result = Array<[Int]>()
        var set = Set<Int>()
        
        generate(index: 0, nums: &sortNums, results: &result,
                 temp: &temp, set: &set, sum: 0, target: target)
        
        return result
    }
    
    private func generate(index: Int, nums: inout [Int],
                          results: inout [[Int]], temp: inout [Int],
                          set: inout Set<Int>, sum: Int, target: Int) {
        
        if sum > target || index >= nums.count { return }
        var newSum = sum + nums[index]
        temp.append(nums[index])
        let hash = self.myHash(array: temp)
        if newSum == target && !set.contains(hash) {
            results.append(temp)
            set.insert(hash)
        }
        //        print(temp)
        generate(index: index + 1, nums: &nums,
                 results: &results, temp: &temp,
                 set: &set, sum: newSum, target: target)
        //        print(temp)
        newSum -= nums[index]
        let _ = temp.popLast()
        //        print(temp)
        generate(index: index + 1, nums: &nums,
                 results: &results, temp: &temp,
                 set: &set, sum: newSum, target: target)
        //        print(temp)
    }
    
    private func myHash(array: [Int]) -> Int {
        return array.reduce(5381) {
            ($0 << 5) &+ $0 &+ $1
        }
    }
    
    func runSolution() {
//        let candidates = [10,1,2,7,6,1,5], target = 8
//        let candidates = [2,5,2,1,2], target = 5
        let candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], target = 27
        print(combinationSum2(candidates, target))
    }
}

extension Array: Hashable where Element == Int {
    
    public var hashValue: Int {
        get {
            return self.reduce(5381) {
                ($0 << 5) &+ $0 &+ $1
            }
        }
    }
    
}
