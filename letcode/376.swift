//
//  376.swift
//  letcode
//
//  Created by zhoubo on 2018/5/8.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 
 **Medium**
 
 A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
 
 For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
 
 Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
 ````
 Examples:
 Input: [1,7,4,9,2,5]
 Output: 6
 The entire sequence is a wiggle sequence.
 
 Input: [1,17,5,10,13,15,10,5,16,8]
 Output: 7
 There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
 
 Input: [1,2,3,4,5,6,7,8,9]
 Output: 2
 ````
 Follow up:
 Can you do it in O(n) time?
 
*/
class Solution376: SolutionDelegate {
    
    func wiggleMaxLength(_ nums: [Int]) -> Int {
        guard nums.count > 1 else {
            return nums.count
        }
        // 方向 -1 还没决定， 0 是负 1 是正
        // 负就是说类似于 17 5 这种 后面小
        // 正就是 5 17 后面大
        var direct = -1
        
        var search = 0
        var currentLength = 1
        
        repeat {
            search += 1
            if direct == -1 {
                // 如果还没决定直接下一个
                if nums[search] == nums[search - 1] {
                    currentLength = 1
                } else {
                    direct = nums[search] > nums[search - 1] ? 1 : 0
                    currentLength += 1
                }
            } else if direct == 0 {
                // 那么本次就要 为 1
                if nums[search] > nums[search - 1] {
                    direct = 1
                    currentLength += 1
                }
                // 如果不是，此时方向不变
            } else {
                if nums[search] < nums[search - 1] {
                    direct = 0
                    currentLength += 1
                }
            }
        } while search < nums.count - 1
        
        
        return currentLength
    }
    
    func runSolution() {
        let s = [1,2,3,4,5,6,7,8,9]
//        let s = [1,7,4,9,2,5]
//        let s = [0, 0]
//        let s = [1,17,5,10,13,15,10,5,16,8]
        print(self.wiggleMaxLength(s))
    }
}
