public class Pat4 {
    public static void main(String[] args) {
        
        int n = 5 ; 

        for(int i = 0 ; i < n; i++){

            //first print space 
            int j;
            for( j = 0 ; j< n-i-1; j++){
                System.out.print(" ");
            }

            for(int k = 0 ; k<n-j;k++){
            System.out.println("*"); 

            }
            System.out.println();
            

            //now print star 
            


        }
    }
}
