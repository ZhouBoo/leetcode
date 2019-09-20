//
//  DispatchSource.swift
//  letcode
//
//  Created by zhoubo on 2019/9/10.
//  Copyright © 2019 zhoubo. All rights reserved.
//

import Foundation

//NSTimer 与 GCD Timer比较
//NSTimer
//
//依赖NSRunloop
//容易导致内存泄漏
//NSTimer的创建与撤销必须在同一个线程操作、 performSelector的创建与撤销必须在同一个线程操作
//GCD Timer
//
//可以被当做对象放入数组或字典中
//GCD Timer必须强引用，否则出了栈就会失效，这种失效不会触发取消处理器
//GCD Timer精度可控
//如果使用dispatch_walltime来设置定时器的起始时间，定时器默认使用walltime来触发定时器；
//如果使用dispatch_time来设置定时器的起始时间，定时器默认使用系统时钟来触发定时器，然而当计算机休眠时，系统时钟也是休眠的。
//对于时间间隔比较大的定时器，使用dispatch_walltime来设置定时器的起始时间

func signalDispatchSource() {
    signal(SIGCHLD, SIG_IGN)
//    let queue = DispatchQueue.global(qos: DispatchQoS.QoSClass.default)
}
