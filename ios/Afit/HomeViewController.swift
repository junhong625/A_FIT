//
//  HomeViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/17.
//

import Foundation
import UIKit
import Alamofire

class HomeViewController: UIViewController {
    
    @IBOutlet weak var welcomeLabel: UILabel!
    
    @IBOutlet weak var GoalText: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        

    }
    
    @IBAction func qnaBtnTapped(_ sender: UIButton) {
        
        
        
    }
    
    @IBAction func logoutButtonTapped(_ sender: UIButton) {
        
        AF.request("http://3.37.56.9/login/logout").responseJSON() { response in
          switch response.result {
          case .success:
            if let data = try! response.result.get() as? [String: Any] {
              print(data)
            }
          case .failure(let error):
            print("Error: \(error)")
            return
          }
        }
        
        self.navigationController?
            .popToRootViewController(animated: true)
    }
    
}

extension HomeViewController: UITextFieldDelegate {
    
    // 리턴 버튼을 눌렀을 때 키보드 내려가게 하기
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        view.endEditing(true)
        return false
    }
}
