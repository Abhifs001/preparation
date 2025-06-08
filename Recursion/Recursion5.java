import java.util.Arrays;

public class Recursion5 {
    public static void main(String[] args) {
        
        int[] arr = {1,2,3,4,5};

        int[] revAr = RevArray(arr, 0, arr.length-1);

      System.out.println( Arrays.toString(revAr)); // why this is not working 
      
    }

    public static int[] RevArray(int[] arr, int start, int end){

    if(start==end){
        return arr;
    }

    int temp = arr[start];
    arr[start]= arr[end];
    arr[end]=temp; 

    return RevArray(arr, start+1, end-1);

    }
}
