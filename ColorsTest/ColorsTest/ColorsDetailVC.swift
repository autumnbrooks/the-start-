//
//  ColorsDetailVC.swift
//  ColorsTest
//
//  Created by Autumn Brooks on 6/1/24.
//

import UIKit

class ColorsDetailVC: UIViewController {
    
    var color: UIColor?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = color ?? .blue
    }
    
}
