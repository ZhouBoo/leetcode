//
//  113.swift
//  letcode
//
//  Created by zhoubo on 2018/5/11.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation


/**
 **Medium**
 
 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
 
 Note: A leaf is a node with no children.
 
 Example:
 
 Given the below binary tree and sum = 22,
 
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
 
 Return:
 
 [
 [5,4,11,2],
 [5,8,4,5]
 ]
 
 */
class Solution113: SolutionDelegate {
    
    var paths = Array<Array<Int>>()
    var sumv = 0
    var sums = Array<Int>()
    
    @discardableResult
    func pathSum(_ root: TreeNode?, _ sum: Int) -> [[Int]] {
        
        guard let root = root else { return paths }
        
        if sums.isEmpty {
            sums.append(root.val)
            sumv += root.val
        }
        
        if let left = root.left {
            sumv += left.val
            sums.append(left.val)
            pathSum(left, sum)
        }
        
        if let right = root.right {
            sumv += right.val
            sums.append(right.val)
            pathSum(right, sum)
        }
//        print(sums)
        if sumv == sum && root.left == nil && root.right == nil {
            paths.append(sums)
        }
        
        sums.removeLast()
        sumv -= root.val
//        print("-----")
//        print(paths)

        return paths
    }
    
    func runSolution() {
//        let s = TreeNode(5)
//        let lastLL = TreeNode(7), lastLR = TreeNode(2), lastRL = TreeNode(5), lastRR = TreeNode(1)
//        let midLL = TreeNode(11), midRL = TreeNode(13), midRR = TreeNode(4)
//        midLL.left = lastLL
//        midLL.right = lastLR
//        midRR.left = lastRL
//        midRR.right = lastRR
//
//        let topL = TreeNode(4), topR = TreeNode(8)
//        topL.left = midLL
//        topR.left = midRL
//        topR.right = midRR
//        s.left = topL
//        s.right = topR
//        let v = 22
        
        let s = TreeNode(1)
        let lastLL = TreeNode(2)
        s.left = lastLL

        let v = 1
        print(pathSum(s, v))
    }
}

/**
 * Definition for a binary tree node.
 */
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}
