class SortColorDutchAlgo {
    // public void sortColors(int[] nums) {
    //     if (nums.length == 1)
    //         return;

    //     int freq[] = new int[300];
    //     for (int i : nums) {
    //         freq[i]++;
    //     }
    //     int k = 0;
    //     for (int num = 0; num < freq.length; num++) {
    //         int count = freq[num];
    //         while (count-- > 0) {
    //             nums[k++] = num;
    //         }
    //     }
    //     return;
    // }

    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low++, mid++);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high--);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

}