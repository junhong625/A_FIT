//
//  LoginViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/08.
//

import Foundation
import UIKit
import Firebase
import FirebaseAuth
import GoogleSignIn



class LoginViewController:UIViewController {
    
    
    
    @IBOutlet weak var registerButton: UIButton!
    
    @IBOutlet weak var googleLoginButton: UIButton!
    
    @IBOutlet weak var appleLoginButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        [registerButton, googleLoginButton, appleLoginButton].forEach {
            
            $0?.layer.borderWidth = 1
            $0?.layer.borderColor = UIColor.white.cgColor
            $0?.layer.cornerRadius = 30
        }
    }
    
//    override func viewWillAppear(_ animated: Bool) {
//        super.viewWillAppear(animated)
//
//        navigationController?.navigationBar.isHidden = true
//    }
    
    
    
    @IBAction func registerButtonTapped(_ sender: UIButton) {
    }
    
    
    @IBAction func googleLoginButtenTapped(_ sender: UIButton) {
        
        // Your user is signed in!
     
     guard let clientID = FirebaseApp.app()?.options.clientID else { return }

     // Create Google Sign In configuration object.
     let config = GIDConfiguration(clientID: clientID)

     // Start the sign in flow!
     GIDSignIn.sharedInstance.signIn(with: config, presenting: self) { [unowned self] user, error in

       if let error = error {
         // ...
         return
       }

       guard
         let authentication = user?.authentication,
         let idToken = authentication.idToken
       else {
         return
       }

       let credential = GoogleAuthProvider.credential(withIDToken: idToken,
                                                      accessToken: authentication.accessToken)
         Auth.auth().signIn(with: credential) { _, _ in
             showMainViewController()
             
        //...
         
         }
     
     
     func showMainViewController() {
         let storyboard = UIStoryboard(name: "Main", bundle: Bundle.main)
         let MainViewController = storyboard.instantiateViewController(identifier: "MainViewController")
         MainViewController.modalPresentationStyle = .fullScreen
         UIApplication.shared.windows.first?.rootViewController?.show(MainViewController, sender: nil)
        }
    
     }
   }
}
