//
//  UIColor+ext.swift
//  ColorsTest
//
//  Created by Autumn Brooks on 6/1/24.
//

import UIKit

extension UIColor {
    
    static func random()  ->  UIColor {
        
        let randomColor = UIColor(red: .random(in: 0...1), green: .random(in: 0...1), blue: .random(in: 0...1), alpha: 1)
        
        return randomColor
    }
    
}
