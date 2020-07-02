//
//  QuickSort.swift
//  letcode
//
//  Created by zhoubo on 2018/8/21.
//  Copyright © 2018年 zhoubo. All rights reserved.
//

import Foundation

func partition( data:inout [Int],low:Int,high:Int) -> Int {
    
    let root = data[high]
    var index = low
    for i in low...high {
        if data[i] < root {
            if i != index {
                data.swapAt(i, index)
            }
            index = index+1
        }
    }
    
//    if high != index {
        data.swapAt(high, index)
//    }
    return index
}

func quickSort(data: inout [Int], low: Int, high: Int) -> Void {
    if low >= high {
        return
    }
    print(data)
    let sortIndex = partition(data: &data, low: low, high: high)
    quickSort(data: &data, low: low, high: sortIndex-1)
    quickSort(data: &data, low: sortIndex+1, high: high)
}

func runQuickSort() {
    var arr:[Int] = [10,3,17,8,5,2,1,9,5,4]
    quickSort(data: &arr, low: 0, high: arr.count-1)
    print("\(arr)")
}

