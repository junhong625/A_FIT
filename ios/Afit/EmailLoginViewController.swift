//
//  EmailLoginViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/17.
//

import Foundation
import UIKit
import Alamofire

class EmailLoginViewController: UIViewController {
    
    @IBOutlet weak var useremailText: UITextField!
    
    @IBOutlet weak var passwordText: UITextField!
    
    
    @IBOutlet weak var backButton: UIView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Navigation bar 보이기
        navigationController?.navigationBar.isHidden = false
        
        useremailText.delegate = self
        passwordText.delegate = self
        
        // useremail 란에 커서가 자동적으로 찍히도록
        useremailText.becomeFirstResponder()

    }
    
    
    @IBAction func backBtnTapped(_ sender: Any) {
        
        self.navigationController?.popToRootViewController(animated: true)
    }
    
    @IBAction func loginButtonTapped(_ sender: UIButton) {
        
        let useremail = useremailText.text ?? ""
        let password = passwordText.text ?? ""
        
        let url = "http://3.37.56.9/login/app_login"
        var request = URLRequest(url: URL(string: url)!)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.timeoutInterval = 10

        // POST 로 보낼 정보
        let params = ["user_id": useremail, "password": password] as Dictionary

        // httpBody 에 parameters 추가
        do {
            try request.httpBody = JSONSerialization.data(withJSONObject: params, options: [])
        } catch {
            print("http Body Error")
        }

        AF.request(request).responseString { (response) in

            switch response.result {
            case .success:
                print("POST 성공")

            case .failure(let error):

                print("🚫 Alamofire Request Error\nCode:\(error._code), Message: \(error.errorDescription!)")
            }
            
            
            self.showMainViewController()
        }
    }
    
    
    func showMainViewController() {
        let storyboard = UIStoryboard(name: "Main", bundle: Bundle.main)
        let MainViewController = storyboard.instantiateViewController(identifier: "MainViewController")
        MainViewController.modalPresentationStyle = .fullScreen
        UIApplication.shared.windows.first?.rootViewController?.show(MainViewController, sender: nil)
    }
    
    
}

extension EmailLoginViewController: UITextFieldDelegate {
    
    // 이메일, 비번 입력 후 리턴 버튼을 눌렀을 때 키보드 내려가게 하기
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        view.endEditing(true)
        return false
    }
}
