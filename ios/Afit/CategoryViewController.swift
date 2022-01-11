//
//  CategoryViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/24.
//

import Foundation
import UIKit
import SafariServices



class CategoryViewController: UIViewController {
    
    @IBOutlet weak var BtnGotoSite: UIButton!
    

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
        
    
    @IBAction func BtnGotoSite(_ sender: UIButton) {
        
        let youtubeurl = NSURL(string: "https://www.youtube.com/")
        let youtubeSafariView: SFSafariViewController = SFSafariViewController(url: youtubeurl as! URL)
        self.present(youtubeSafariView, animated: true, completion: nil)
        
    }
    
}
