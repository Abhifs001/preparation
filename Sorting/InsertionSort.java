import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        
        int[] arr = {8,7,6,5,4,3,1};
        insertionsort(arr);
        System.out.println(Arrays.toString(arr));

    }

    public static void insertionsort(int[] arr){

        //treat current element as sorted 

        for(int curr = 1; curr < arr.length; curr++){
            //store the current element 
            int ele= arr[curr]; //index till sorted part

             //treat remaining as unsorted 


            int j = curr-1; 

            while (j>=0 && arr[j]>ele){
                arr[j+1]=arr[j]; 
                j--;
            }

            arr[j+1]= ele;

              
        }
    }
    
}
