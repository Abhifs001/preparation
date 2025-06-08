public class ReverseNum {
    

    public static void main(String[] args) {
                int num = 123; 

        int temp = num ; 
        int count = 0 ; 
        while(temp>0){
            
            int unit = temp%10; 
            count = count*10+unit; 
           
            temp/=10; 
        }

        System.out.println(count);
    }
}
