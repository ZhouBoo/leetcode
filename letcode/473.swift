//
//  473.swift
//  letcode
//
//  Created by zhoubo on 2018/5/24.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Difficulty:Medium**
 
 Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
 
 Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.
 
 Example 1:
 Input: [1,1,2,2,2]
 Output: true
 
 Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
 Example 2:
 Input: [3,3,3,3,4]
 Output: false
 
 Explanation: You cannot find a way to form a square with all the matchsticks.
 Note:
 The length sum of the given matchsticks is in the range of 0 to 10^9.
 The length of the given matchstick array will not exceed 15.
 */
class Solution473: SolutionDelegate {

    func makesquare(_ nums: [Int]) -> Bool {
        let n = nums.count
        if(n < 4) {
            return false
        }
        let sum = nums.reduce(0) { (r, v) -> Int in
            return r + v
        }
        if(sum % 4 != 0) {
          return false
        }
        let target = sum / 4
        let visited = Array<Bool>(repeating: false, count: n)
        let count = 0
        
        return canfind(target: target, left: target,
                       visitied: visited, nums: nums, start: 0, count: count)
    }
    
    func canfind(target: Int, left: Int, visitied: [Bool],
                 nums: [Int], start: Int, count: Int) -> Bool {
        if start == nums.count || left < 0 {
            return false
        }
        
        if left == 0 {
            let newCount = 1 + count
            
            if newCount == 3 {
                return true
            } else {
                return canfind(target: target, left: target,
                               visitied: visitied, nums: nums, start: 0, count: newCount)
            }
        }
        
        
        for i in start..<nums.count {
            var v = visitied
            if v[i] {
                continue
            }
            
            v[i] = true
            if canfind(target: target, left: left - nums[i],
                       visitied: v, nums: nums, start: i + 1, count: count) {
                return true
            }
            
            v[i] = false
            
        }
        
        return false
    }
    
//    public boolean canfind(int target,int left,boolean [] visited,int[] nums,int start,int count) {
//    if(start==nums.length||left<0) return false;
//    if(left==0) {
//    count++;
//    if(count==3) return true;
//    else {
//    return canfind(target,target,visited,nums,0,count);
//    }
//    }
//    for(int i=start;i<nums.length;i++) {
//    if(visited[i]) continue;
//    visited[i]=true;
//    if(canfind(target,left-nums[i],visited,nums,i+1,count))
//    return true;
//    visited[i]=false;
//    }
//    return false;
//    }
    
//    func makesquare(_ nums: [Int]) -> Bool {
//        let sortNums = nums.sorted()
//        let sum = nums.reduce(0) { (r, v) -> Int in
//            return r + v
//        }
//        if sum % 4 != 0 || sortNums.count < 4 {
//            return false
//        }
//
//        let max = sum / 4
//        print(max)
//        let matchs = Array<Int>(repeating: 0, count: 4)
//
//        return self.generate(index: 0, nums: sortNums, max: max, matchs: matchs)
//
//    }
//
//
//    private func generate(index: Int, nums: [Int], max: Int, matchs: [Int]) -> Bool {
//        if index >= nums.count {
//            print(matchs)
//            return matchs[0] == max && matchs[1] == max &&
//                matchs[2] == max && matchs[3] == max
//        }
//
//
//        for i in 0..<4 {
//            if (matchs[i] + nums[index] > max) {
//                continue
//            } else {
//                var newMatchs = matchs
//                newMatchs[i] += nums[index]
//
//                if self.generate(index: index + 1, nums: nums,
//                                 max: max, matchs: newMatchs) {
//                    return true
//                }
//
//                newMatchs[i] -= nums[index]
//            }
//        }
//
//        return false
//    }
    
    func runSolution() {
//        let nums = [1,1,2,2,2]
//        let nums = [3,3,3,3,4]
        let nums = [
            5969561,8742425,2513572,3352059,9084275,
            2194427,1017540,2324577,6810719,8936380,7868365,
            2755770,9954463,9912280,4713511
        ]
        
        print(makesquare(nums))
    }
}
