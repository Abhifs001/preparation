public class Recursion6 {
    public static void main(String[] args) {
        String s = "sefes";

         if (checkpal(s, 0, s.length()-1)) {
            System.out.println("pallindrome ");
         } else {
            System.out.println("not pallindrome");
         }
    }


    public static boolean checkpal(String s, int start, int end){

        if(s.charAt(start)==s.charAt(end)){
            return true; 
        }

        
        if(s.charAt(start)==s.charAt(end)){
             return checkpal(s, start+1, end-1);
        }

        return false;
    }
}
