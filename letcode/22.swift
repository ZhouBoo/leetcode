//
//  22.swift
//  letcode
//
//  Created by zhoubo on 2018/5/22.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Medium**
 
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
 For example, given n = 3, a solution set is:
 
 [
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
 ]
 */
class Solution22: SolutionDelegate {
    
    func generateParenthesis(_ n: Int) -> [String] {
        let stackLeft = Array(repeating: "(", count: n - 1)
        let stackRight = Array(repeating: ")", count: n )
        let leftFlag = 1
        var result: [String] = []
        let temp: String = "("
        
        self.generate(leftFlag: leftFlag, result: &result,
                      left: stackLeft, right: stackRight, temp: temp)
        
        return result
    }
    
    private func generate(leftFlag: Int, result: inout [String], left: [String], right: [String], temp: String) {
        if left.count == 0 && right.count == 0 {
            result.append(temp)
            return
        }
        
        if left.count > 0 {
            let newleftFlag = leftFlag + 1
            let newTemp = "\(temp)("
            var newLeft = Array(left)
            let _ = newLeft.popLast()
            print(newTemp)
            generate(leftFlag: newleftFlag, result: &result,
                     left: newLeft, right: right, temp: newTemp)
        }
        
        if leftFlag > 0 && right.count > 0 {
            let newleftFlag = leftFlag - 1
            let newTemp = "\(temp))"
            var newRight = Array(right)
            let _ = newRight.popLast()
            print(newTemp)
            generate(leftFlag: newleftFlag, result: &result,
                     left: left, right: newRight, temp: newTemp)
        }
        
    }
    
    func runSolution() {
        let n = 3
        let r = generateParenthesis(n)
        print(r)
    }
}
