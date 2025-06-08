import java.util.Arrays;

public class BubSort {
    public static void main(String[] args) {
        int[] arr ={6,5,4,3,2,1};

        BubbleSort(arr);
        System.out.println(Arrays.toString(arr));


    }

    public static void BubbleSort(int[] arr){
        int n = arr.length; 
        boolean swap  = false; 

        for(int i=0;i<n;i++){

            for(int j=0;j<n-1-i; j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j]; 
                    arr[j]= arr[j+1];
                    arr[j+1] = temp; 

                    swap = true; 
                }
            }

            if(!swap){
                break;//array already sort
            }
        }
    }
}
