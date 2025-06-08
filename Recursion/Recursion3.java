public class Recursion3 {
    public static void main(String[] args) {
        int N = 4;
        int ans = sumofN(N, 0); // but main method is called without any object so it is contradicts the statement 1 
        System.out.println(ans);
    }
    //this belongs to objects of class 
            //if static is not there
    public static int sumofN(int n , int sum ){//1 non static method means call it using Object
        if(n==0){
            return sum;
        }
        
        return sumofN(n-1, sum+n);
    }
}
