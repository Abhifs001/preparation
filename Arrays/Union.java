import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Collections;

public class Union {
    public static void main(String[] args) {
        int[] nums1 = { 5, 7, 6 };
        int[] nums2 = { 4, 1, 2 };
        int[] ans = unionArray(nums1, nums2);
        for (int num : ans)
            System.out.println(num);
    }

    public static int[] unionArray2(int[] nums1, int[] nums2) {
        List<Integer>ans = new ArrayList<>(); 
        
        int i = 0 , j = 0 ; 
        while(i<nums1.length && i<nums2.length){
            if(nums1[i]!=nums2[j]){
                ans.add(nums1[i++]); 
                ans.add(nums2[j++]);
            }else{
                ans.add(nums1[i]);
                i++;
            }
        }

            return ans.stream().mapToInt(Integer::intValue).toArray(); 
    }

    // returns
    public static int[] unionArray(int[] nums1, int[] nums2) {
        LinkedHashSet<Integer> st = new LinkedHashSet<>();

        for (int i : nums1) {
            st.add(i);
        }
        for (int i : nums2) {
            st.add(i);
        }
        int[] ans = new int[st.size()];
        int k = 0;
        for (int i : st) {
            ans[k] = i;
            k++;
        }
        return ans;
    }

}
