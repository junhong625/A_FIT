//
//  Analysis.swift
//  Afit
//
//  Created by 정사라 on 2021/12/18.
//

import Foundation

struct AnalysisResult: Codable {
  let feedback: String
  let sitAngle: String
  let bodyAngle: String
    
  
  enum CodingKeys: String, CodingKey {
    case feedback
    case sitAngle = "sit_angle"
    case bodyAngle = "body_angle"
  }
    

    
    
}

