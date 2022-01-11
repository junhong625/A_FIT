//
//  QnABoardViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/28.
//

import Foundation
import UIKit
import Alamofire


class QnABoardViewController: UIViewController {
    
    @IBOutlet weak var TitleTextView: UITextField!
    @IBOutlet weak var EmailText: UITextField!
    @IBOutlet weak var ContentText: UITextView!
    @IBOutlet weak var SendBtn: UIButton!
    @IBOutlet weak var BackBtn: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        TitleTextView.delegate = self
        EmailText.delegate = self
        ContentText.delegate = self
        
        TitleTextView.becomeFirstResponder()
    
    }
    

    @IBAction func SendBtnTapped(_ sender: UIButton) {
        
        let Tittle = TitleTextView.text ?? ""
        let Email = EmailText.text ?? ""
        let Contents = ContentText.text ?? ""
        
        let url = "http://3.37.56.9/qnaboard/regist_qna"
        var request = URLRequest(url: URL(string: url)!)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.timeoutInterval = 10

        // POST 로 보낼 정보
        let params = ["title": Tittle, "email": Email, "content" : Contents ] as Dictionary

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
        }
    }

    
    @IBAction func BackBtnTapped(_ sender: UIButton) {
        
        self.presentingViewController?.dismiss(animated: true)

        }
    
}
    
extension QnABoardViewController: UITextFieldDelegate {
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        view.endEditing(true)
        return false
    }
}

extension QnABoardViewController: UITextViewDelegate {
    func textFieldShouldClear(_ textField: UITextField) -> Bool {
        view.endEditing(true)
        return false
    }
}
