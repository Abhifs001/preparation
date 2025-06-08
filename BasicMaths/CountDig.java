class CountDig{
    public static void main(String[] args) {
        int num = 123; 

        int temp = num ; 
        int count = 0 ; 
        while(temp>0){
            

            count++; 
            temp/=10; 
        }

        System.out.println(count);
    }
}