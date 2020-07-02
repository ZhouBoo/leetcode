//
//  main.swift
//  letcode
//
//  Created by zhoubo on 2018/3/29.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

let start = Date()
print("start -----> \(start)")
//let s = Solution30().findSubstring(s1, s2)
//Solution409().runSolution()
//Solution290().runSolution()
//Solution187().runSolution()
//Solution76().runSolution()
//Solution455().runSolution()
//Solution376().runSolution()
//Solution402().runSolution()
//Solution55().runSolution()
//Solution45().runSolution()
//Solution49().runSolution()// interesting
//Solution452().runSolution()
//Solution113().runSolution()
//Solution78().runSolution() // interesting
//Solution90().runSolution()
//Solution40().runSolution()
//Solution22().runSolution()
Solution51().runSolution()
//Solution473().runSolution()
//Solution848().runSolution()
//runQuickSort()
//let end = Date()
//let duration = end.timeIntervalSince(start)
//print("end ------> duration: \(duration) s")


//func getOneBits(n: Int) -> [Int] {
//    // Write your code here
//    var count:Int = 0
//    var bit: Int = 1
//    var indexs: [Int] = []
//    var index: Int = 0
//    var lastOne: Int = 0
//    while(index < 32) {
//        if ((n & bit) == bit) {
//            count += 1
//            indexs.insert(index, at: 0)
//            lastOne = index
//        }
//        index += 1
//        bit = bit << 1
//    }
//    indexs = indexs.map { (n) -> Int in
//        return lastOne - n + 1
//    }
//    indexs.insert(count, at: 0)
//    return indexs
//}

//print(getOneBits(n: 161))


//func kDifference(arr: [Int], k: Int) -> Int {
//    // Write your code here
//    let sets = Set(arr)
//    var arr = Array(sets)
//    arr.sort()
//    var count = 0
//    for (index, i) in arr.enumerated() {
//        if index == 0 {
//            continue
//        } else {
//            var p = index - 1
//            while (p >= 0) {
//                let diff = abs(arr[p] - i)
//                if diff == k {
//                    count += 1
//                    break
//                } else if diff > k {
//                    break
//                }
//                p -= 1
//            }
//        }
//    }
//    return count
//}
//
//print(kDifference(arr: [1, 5, 3, 4, 2], k: 2))

//
//func balancedSum(sales: [Int]) -> Int {
//    var left = 0
//    var right = sales.reduce(0, +)
//    for (index, i) in sales.enumerated() {
//        left += i
//        right -= i
//        if (left == right) {
//            return index + 1
//        } else {
//            var cRight = right
//            var cIndex = sales.count - 1
//            while (cRight > left && cIndex > index) {
//                cRight -= sales[cIndex]
//                if (left == cRight) {
//                    return index + 1
//                }
//                cIndex -= 1
//            }
//
//        }
//    }
//    return 0
//}
//
//
//print(balancedSum(sales: [1, 2, 3, 3]))
//print(balancedSum(sales: [3, 1, 2, 1]))
