//
//  FullBodyViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/16.
//

import Foundation
import UIKit
import Lottie

class FullBodyViewController: UIViewController {
    
    
    @IBOutlet weak var examLabel: UILabel!
    
        
 //   @IBOutlet weak var animationView: AnimationView!
    
    @IBOutlet weak var imgView: UIImageView!
    
    @IBOutlet weak var examText: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지로 대체했기 때문에 애니메이션 주석 처리함
        
//        //Lottie AnimationView 생성
//        let squatKick = AnimationView(name: "55808-squat-kick")
//        squatKick.frame = CGRect(x: 45, y: 45, width: 200, height: 200)
//        // 메인 뷰에 삽입
//        self.view.addSubview(squatKick)
//
//        squatKick.frame = squatKick.superview!.bounds
//        squatKick.contentMode = .scaleAspectFit
//
//        // 애니메이션 재생 (애니메이션 재생모드 미 설정시 1회)
//        squatKick.play()
//
//        // 애니메이션 재생모드 ( .loop = 애니메이션 무한 재생 )
//        squatKick.loopMode = .loop

//        // 애니메이션 종료
//        // squatKick.pause()
//
//        // 1. Set animation content mode
//
//        animationView.contentMode = .scaleAspectFit
//
//        // 2. Set animation loop mode
//
//        animationView.loopMode = .loop
//
//        // 3. Adjust animation speed
//
//        animationView.animationSpeed = 0.5
//
//        // 4. Play animation
//        animationView.play()
        
    }

}

