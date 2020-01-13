class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] notFound = { -1, -1 };
        int left = this.findExtreme(nums, 0, nums.length - 1, target, true);
        if (left == -1)
            return notFound;
        int right = this.findExtreme(nums, left, nums.length - 1, target, false);
        return new int[] { left, right };
    }

    public int findExtreme(int[] nums, int low, int high, int target, boolean left) {
        while (low < high) {
            int mid = (low + high) / 2;
            if (target < nums[mid] || (target == nums[mid] && left)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        if (left) {
            return (low < nums.length && nums[low] == target) ? low : -1;
        } else {
            return (low == nums.length - 1 && nums[low] == target) ? low : low - 1;
        }
    }
}