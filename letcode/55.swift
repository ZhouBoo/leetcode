//
//  55.swift
//  letcode
//
//  Created by zhoubo on 2018/5/8.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Medium**
 
 Given an array of non-negative integers, you are initially positioned at the first index of the array.
 
 Each element in the array represents your maximum jump length at that position.
 
 Determine if you are able to reach the last index.
 
 Example 1:
 ````
 Input: [2,3,1,1,4]
 Output: true
 Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 ````
 Example 2:
 ````
 Input: [3,2,1,0,4]
 Output: false
 Explanation: You will always arrive at index 3 no matter what. Its maximum
 jump length is 0, which makes it impossible to reach the last index.
 ````
 */
class Solution55: SolutionDelegate {
    
    func canJump(_ nums: [Int]) -> Bool {
        var index = 0
        var flag = false
        while index < nums.count {
            let number = nums[index]
            if number < 1 {
                break
            }
            
            var maxNumber = 0
            var maxIndex = -1
            
            for jumpIndex in (index + 1)...(index + number) {
                
                if jumpIndex >= nums.count {
                    index = nums.count
                    flag = true
                    break
                }
                
                let maxJump = jumpIndex + nums[jumpIndex]
                if maxNumber <= maxJump {
                    maxNumber = maxJump
                    maxIndex = jumpIndex
                }
                
            }
            
            if maxIndex != -1 {
                index = maxIndex
                print("index = \(index), value = \(nums[index])")
            } else {
                break
            }
        }
        
        return flag || index >= nums.count - 1
    }
    
    func runSolution() {
//        let s = [3,2,1,0,4]
//        let s = [2,3,1,1,4]
//        let s = [0]
//        let s = [2, 0, 0]
        let s = [5,9,3,2,1,0,2,3,3,1,0,0]
//        let s = [4,2,0,0,1,1,4,4,4,0,4,0]
        print(canJump(s))
    }
}
