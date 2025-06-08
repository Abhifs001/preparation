

public class Recursion1 {
    public static void main(String[] args) {
        printsomething(6);
    }

    public static void printsomething(int index){
        //base 
        if(index ==0){
            return ; 
        }

        System.out.println(index);

        printsomething(index-1);

    }


}
