//
//  ResultViewController.swift
//  Afit
//
//  Created by 정사라 on 2021/12/19.
//

import Foundation
import UIKit
import Photos
import YPImagePicker
import Alamofire
import MLKitPoseDetection
import MLKitPoseDetectionCommon

class ResultViewController: UIViewController {
    
    @IBOutlet var resultImageView: UIImageView!
    @IBOutlet weak var feedbackLabel: UILabel!
    @IBOutlet weak var sitAngleLabel: UILabel!
    @IBOutlet weak var bodyAngleLabel: UILabel!
    

    
    let spinnerView = UIActivityIndicatorView(style: .large)
    var analysis: AnalysisResult!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        [feedbackLabel, sitAngleLabel, bodyAngleLabel].forEach {

        $0?.layer.borderWidth = 1
        $0?.layer.borderColor = UIColor.white.cgColor
            
        }
    
        
        setup()
        
    }
    
    func setup() {
        setupSpinnerView()
    }
    
    func setupSpinnerView() {
        spinnerView.color = .white
        spinnerView.backgroundColor = .init(white: 0, alpha: 0.5)
        view.addSubview(spinnerView)
        spinnerView.translatesAutoresizingMaskIntoConstraints = false
        spinnerView.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
        spinnerView.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true
        spinnerView.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
        spinnerView.bottomAnchor.constraint(equalTo: view.bottomAnchor).isActive = true
        
    }
    
    
    @IBAction func imageSelectButtonTapped() {
        
        // 카메라 라이브러리 세팅
        var config = YPImagePickerConfiguration()
        config.screens = [.library, .photo]
        
        let picker = YPImagePicker(configuration: config)
        
        // 사진이 선택되었을 때
        picker.didFinishPicking { [unowned picker] items, _ in
            if let photo = items.singlePhoto {
                print(photo.fromCamera) // Image source (camera or library)
                print(photo.image) // Final image selected by the user
                print(photo.originalImage) // original image selected by the user, unfiltered
                print(photo.modifiedImage) // Transformed image, can be nil
                print(photo.exifMeta) // Print exif meta data of original image.
                // 프사이미지를 변경한다
                self.resultImageView.image = photo.image
            }
            // 사진 선택창 닫기
            picker.dismiss(animated: true, completion: nil)
        }
        // 사진 선택창 보여주기
        present(picker, animated: true, completion: nil)


    }
    
    @IBAction func analysisButtonTapped() {
        
        spinnerView.startAnimating()
        postImageToServer()

    }
    
    func postImageToServer() {
        let boundary = "Boundary-\(UUID().uuidString)"
        let url = URL(string: "http://3.37.56.9/httpTest/")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue(
          "multipart/form-data; boundary=\(boundary)",
          forHTTPHeaderField: "Content-Type")
        
        let httpBody = NSMutableData()
        let imageData = resultImageView.image?.pngData()
        let convertedData = convertFileData(
          fieldName: "image",
          fileName: "\(UUID().uuidString).png",
          mimeType: "image/png",
          fileData: imageData!,
          using: boundary)
        
        httpBody.append(convertedData)
        httpBody.appendString("--\(boundary)--")
        
        request.httpBody = httpBody as Data
        
        URLSession.shared.dataTask(with: request) { data, response, error in
          guard let data = data else { return }
          DispatchQueue.main.async {
            self.spinnerView.stopAnimating()
//              self.feedbackLabel.text = "\(String(data: data, encoding: .utf8)!)"

              print(String(data: data, encoding: .utf8)!)
              
              
          guard let decoded = try? JSONDecoder().decode(AnalysisResult.self, from: data) else { return }
            self.analysis = decoded
              self.feedbackLabel.text = "  Feedback: \(decoded.feedback)"
              self.sitAngleLabel.text = "  Sit angle: \(decoded.sitAngle)"
              self.bodyAngleLabel.text = "  Body angle: \(decoded.bodyAngle)"
              

          print(String(data: data, encoding: .utf8)!)
          ///{
          ///"feedback" : "올바르지 않은 자세입니다.",
          ///"waist_angle: "asdfasdf"
          ///"knee_angle: "asdfasdf"
          ///}
          ///
          ///
          }
        }.resume()
        
      }
      
      func convertFileData(
        fieldName: String,
        fileName: String,
        mimeType: String,
        fileData: Data,
        using boundary: String) -> Data {
          let data = NSMutableData()
          data.appendString("--\(boundary)\r\n")
          data.appendString("Content-Disposition: form-data; name=\"\(fieldName)\"; filename=\"\(fileName)\"\r\n")
          data.appendString("Content-Type: \(mimeType)\r\n\r\n")
          data.append(fileData)
          data.appendString("\r\n")
          return data as Data
      }
    }

    extension NSMutableData {
      func appendString(_ string: String) {
        if let data = string.data(using: .utf8) {
          self.append(data)
        }
      }
    }
    
        
extension ResultViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        
        // 인터넷 블로그 :https://yunjjang.tistory.com/6
        
        if let image = info[UIImagePickerController.InfoKey.originalImage] as? UIImage {
            resultImageView.image = image
        }
        
        dismiss(animated: true, completion: nil)
    }
    
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true, completion: nil)
    }
}



