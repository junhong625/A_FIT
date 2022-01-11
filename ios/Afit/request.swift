//
//  request.swift
//  Afit
//
//  Created by 정사라 on 2021/12/19.
//

import Foundation
import UIKit

struct Response: Codable {
    let success: Bool
    let result: String
    let message: String
}

//Body 가 없는 요청
func requestGet(url: String, completionHandler: @escaping (Bool, Any) -> Void ) {
 
 }

// Body 가 있는 요청
func requestPost(url: String, method: String, param: [String: Any], completionHandler: @escaping (Bool, Any) -> Void) {
    if method == "GET" {
        requestGet(url: url) { (success, data) in
            completionHandler(success, data)
        }
        
    }
    else {
        requestPost(url: url, method: method, param: param) { (success, data) in
            completionHandler(success, data)
        }
    }
}
