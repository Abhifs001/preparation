import java.util.Collections;
import java.util.PriorityQueue;

class PriorityQ{
    public static void main(String[ ]args){
        PriorityQueue<Integer> p = new PriorityQueue<>( ); 
        
        int[] arr= {3,2,1,5,6,4} ; 
        int ans = findKthLargest(arr, 2 );
                System.out.println( ans);
    }

     public static int findKthLargest(int[] nums, int k) {
        
        PriorityQueue<Integer> p = new PriorityQueue<>();

        //nums = [3,2,1,5,6,4], k = 2
        //3 2 --2 3 
        // 2 1 -----1 
        // 5 1 ---
       
        for(int i = 0 ; i < nums.length;i++){
            System.out.println("-----------adding---------"+ nums[i]);
            p.add(nums[i]);
            System.out.println("--------after adding-----"+ p);
            if( p.size()>k){
                System.out.println("----------removing top element");
                p.poll();//remove larger 
                System.out.println("after removing-----"+p);
            } 
        }

      return p.peek(); 
         
    }
}