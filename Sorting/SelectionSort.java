import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {8, 7, 6, 5, 4, 3, 1};
        selectionsort(arr);
        System.out.println(Arrays.toString(arr));

         
    }

      public static void selectionsort(int[] arr) {
            //store the current element 

            for(int i =0; i<arr.length;i++){
               

                //find the minimum element in the remaining unsorted part

                int minIndex = i;
                int j = i+1; 
                
                while(j<arr.length  ){
                  if( arr[j]<arr[minIndex]){  minIndex = j;    }
                    j++;
                   
                }

                // swap minimum element with current element 
                int temp= arr[i];
                arr[i]= arr[minIndex];
                arr[minIndex]= temp;
            }
    }
}
