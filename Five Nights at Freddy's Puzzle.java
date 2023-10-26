/*
 * The answer is 1 9 8 3!
 */
import java.util.Scanner;

public class Main
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
   
    System.out.println("Your name is Charlotte Emily. It’s a late night in 1983 and you’re waiting for your father to complete his work at Freddy Fazbears Pizza. Someone in a purple suit told you they had a present for you in one of the rooms. In the room, there’s a box in the middle. It’s a music box two feet in dimension. You approach the box and decide to turn the dial. You have to turn the dial on to four single-digit numbers.");
    
    System.out.println("\nHow many times do you turn your first spin?");
    int userInt = sc.nextInt();
    
    System.out.println("\nHow many times do you turn your second spin?");
    int userInt2 = sc.nextInt();
    
    System.out.println("\nHow many times do you turn your third spin?");
    int userInt3 = sc.nextInt();
    
    System.out.println("\nHow many times do you turn your fourth spin?");
    int userInt4 = sc.nextInt();
    
    
    if ((userInt == 1) && (userInt2 == 9) && (userInt3 == 8) && (userInt4 == 3))
    {
     
     System.out.print("Nothing happens and you continue your shift peacefully. No one kills you by");
   
    }
    
    else
    {
      System.out.print("Puppet pops out and kills you viciously");
    }
    
    int count = 1;
    while (count > 0)
    {
      if (userInt != 1) {
        System.out.print(" by ripping out your throat");
      }
     count--;
    }
    
    count = 1;
    while (count > 0)
    {
      if (userInt != 9) {
        System.out.print(", gutting your stomach");
      }
     count--;
    }
  
    for(int i= 1; i > 0; i--)  {
      if (userInt != 8) {
        System.out.print(", and eats your heart.");
        
      }
    }
    
  }
}