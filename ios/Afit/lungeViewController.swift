//
//  lungeViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/17.
//

import Foundation
import UIKit
import Lottie

class lungeViewController: UIViewController {
    
    
    @IBOutlet weak var examLabel: UILabel!
    
        
    @IBOutlet weak var animationView: AnimationView!
    
    
    @IBOutlet weak var examText: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        

        // 1. Set animation content mode

        animationView.contentMode = .scaleAspectFit

        // 2. Set animation loop mode

        animationView.loopMode = .loop

        // 3. Adjust animation speed

        animationView.animationSpeed = 0.5
        
        // 4. Play animation
        animationView.play()
        
        
        // 애니메이션 종료
        // animationView.pause()
        
    }

}



