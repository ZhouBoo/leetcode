//
//  51.swift
//  letcode
//
//  Created by zhoubo on 2018/5/22.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

/**
 **Hard**
 
 The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
 
 Given an integer n, return all distinct solutions to the n-queens puzzle.
 
 Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
 
 Example:
 
 Input: 4
 Output: [
 [".Q..",  // Solution 1
 "...Q",
 "Q...",
 "..Q."],
 
 ["..Q.",  // Solution 2
 "Q...",
 "...Q",
 ".Q.."]
 ]
 Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
 */
class Solution51: SolutionDelegate {
    
    func solveNQueens(_ n: Int) -> [[String]] {
        var pr = [[String]]()
        
        var result = [[String]]()
        for _ in 0..<n {
            result.append(Array<String>(repeating: " ", count: n))
        }
        
        self.searchQueue(y: 0, map: result, rest: result.count, pr: &pr)
        
        return pr
    }
    
    private func searchQueue(y: Int, map: [[String]], rest: Int, pr: inout [[String]]) {
        if rest <= 0 || y >= map.count {
            pr.append(map.map { (strs) -> String in
                return strs.reduce("", { (r, new) -> String in
                    return "\(r)\(new == "Q" ? "Q" : ".")"
                })
            })
            return
        }
        var x = 0
        while x < map.count {
            if map[x][y] == " " {
                var newMap = map
                putQueue(x: x, y: y, map: &newMap)
                searchQueue(y: y + 1, map: newMap, rest: rest - 1, pr: &pr)
            }
            
            x += 1
        }
    }
    
    private func putQueue(x: Int, y: Int, map: inout [[String]]) {
        var l = x - 1, r = y - 1
        map[x][y] = "Q"
        let lenth = map.count
        while l > -1 && r > 0 {
            map[l][r] = "."
            l -= 1
            r -= 1
        }
        
        l = x + 1
        r = y + 1
        while l < lenth && r < lenth {
            map[l][r] = "."
            l += 1
            r += 1
        }
        
        l = x - 1
        r = y + 1
        while l > -1 && r < lenth {
            map[l][r] = "."
            l -= 1
            r += 1
        }
        
        l = x + 1
        r = y - 1
        while l < lenth && r > 0 {
            map[l][r] = "."
            l += 1
            r -= 1
        }
        
        l = lenth - 1
        r = y
        while l > -1 {
            if l == x && y == r {
                l -= 1
                continue
            }
            map[l][r] = "."
            l -= 1
        }
        
        l = x
        r = lenth - 1
        while r > -1 {
            if l == x && y == r {
                r -= 1
                continue
            }
            map[l][r] = "."
            r -= 1
        }
    }
    
    private func printMap(map: [[String]]) {
        for index in 0..<map.count {
            print(map[index])
        }
    }
    
    func runSolution() {
        let n = 4
        let r = solveNQueens(n)
        printMap(map: r)
        
        print("count = \(r.count)")
    }
}
