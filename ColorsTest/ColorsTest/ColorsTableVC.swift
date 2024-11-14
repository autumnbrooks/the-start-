//
//  ColorsTableVC.swift
//  ColorsTest
//
//  Created by Autumn Brooks on 6/1/24.
//

import UIKit

class ColorsTableVC: UIViewController  {
    
    var colors: [UIColor] = []
    
    enum Cells {
        static let colorCell = "colorCell"
    }
    
    enum Segues{
        static let toDetail = "toColorsDetailVC"
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        addRandomColors()
        // Do any additional setup after loading the view.
    }
    
    func addRandomColors(){
        for _ in 0..<50{
            colors.append(.random())
        }
    }

    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let destVC = segue.destination as! ColorsDetailVC
        destVC.color = sender as? UIColor
    }

}
extension ColorsTableVC: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return colors.count
    
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: Cells.colorCell ) else {
            return UITableViewCell()
        }
        cell.backgroundColor = colors[indexPath.row]
        
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let color = colors[indexPath.row]
        performSegue(withIdentifier: Segues.toDetail, sender: color)
    }
}

