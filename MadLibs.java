
import java.util.Scanner;

public class MadLibs
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    
    String mad = "I went to the <noun> to find the <plural noun>. When I was at the <noun>, I gave the <adjective> <noun> to my <proper noun>.";
    
    int num = mad.indexOf("<");
    int num2 = mad.indexOf(">");
    
    String noun = mad.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    String userInput = sc.nextLine();
    // after collecting input, add it in place of <noun>
    String madLib = mad.substring(0 , num) + userInput;
    
    // ask user for <plural noun>
    String nextPart = mad.substring(num2 + 1);
    num = nextPart.indexOf("<");
    num2 = nextPart.indexOf(">");
    noun = nextPart.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    userInput = sc.nextLine();
    madLib += nextPart.substring(0 , num) + userInput;
   
    
    nextPart = nextPart.substring(num2 + 1);
    num = nextPart.indexOf("<");
    num2 = nextPart.indexOf(">");
    noun = nextPart.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    userInput = sc.nextLine();
    madLib += nextPart.substring(0 , num) + userInput;
    ///
  
    nextPart = nextPart.substring(num2 + 1);
    num = nextPart.indexOf("<");
    num2 = nextPart.indexOf(">");
    noun = nextPart.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    userInput = sc.nextLine();
    madLib += nextPart.substring(0 , num) + userInput;
    ///
   
    
    nextPart = nextPart.substring(num2 + 1);
    num = nextPart.indexOf("<");
    num2 = nextPart.indexOf(">");
    noun = nextPart.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    userInput = sc.nextLine();
    madLib += nextPart.substring(0 , num) + userInput;
    ///
   
   nextPart = nextPart.substring(num2 + 1);
    num = nextPart.indexOf("<");
    num2 = nextPart.indexOf(">");
    noun = nextPart.substring((num + 1),num2);
    System.out.println("Please enter a " + noun + ":");
    userInput = sc.nextLine();
    madLib += nextPart.substring(0 , num) + userInput;
    ///
    System.out.println(madLib);
  }
}