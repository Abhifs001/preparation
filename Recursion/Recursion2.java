class Recursion2{
    public static void main(String[] args) {
        printsomething(1, 5);
        
    }

    public static void printsomething(int index, int N ){
            
        if(index==N){
            System.out.println(index);
            return;
        }

        System.out.println(index);
        printsomething(index+1, N);
    }
}