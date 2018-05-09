//
//  45.swift
//  letcode
//
//  Created by zhoubo on 2018/5/9.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Hard**
 
 Given an array of non-negative integers, you are initially positioned at the first index of the array.
 
 Each element in the array represents your maximum jump length at that position.
 
 Your goal is to reach the last index in the minimum number of jumps.
 
 Example:
 
 Input: [2,3,1,1,4]
 Output: 2
 Explanation: The minimum number of jumps to reach the last index is 2.
 Jump 1 step from index 0 to 1, then 3 steps to the last index.
 Note:
 
 You can assume that you can always reach the last index.
 */
class Solution45: SolutionDelegate {
    
    func jump(_ nums: [Int]) -> Int {
        guard nums.count > 1 else { return 0}
        var index = 0
        var flag = 0
        while index < nums.count {
            let number = nums[index]
            if number < 1 || index >= nums.count {
                break
            }
            
            if index + number + 1 >= nums.count {
                print("index = \(index), foward = \(number)")
                flag += 1
                break
            }
            
            var maxNumber = 0
            var maxIndex = -1
            
            for jumpIndex in (index + 1)...(index + number) {
                
                if jumpIndex > nums.count - 1 {
                    index = nums.count
                    break
                }
                
                let maxJump = jumpIndex + nums[jumpIndex]
                if maxNumber <= maxJump {
                    maxNumber = maxJump
                    maxIndex = jumpIndex
                }
                
            }
            
            if maxIndex != -1 {
                print("index = \(maxIndex), foward = \(maxIndex - index)")
                if maxIndex > index || index >= nums.count {
                    flag += 1
                }
                index = maxIndex
            } else {
                break
            }
        }
        
        return flag
    }
    
    func runSolution() {
//        let s = [2,3,1,1,4]
//        let s = [2,3,1]
//        let s = [2,3,1,1,4]
//        let s = [1,2,0,1]
//        let s = [1, 2]
//        let s = [2, 1]
        let s = [1]
        print(s)
        print(jump(s))
    }
}
