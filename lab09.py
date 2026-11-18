def two_sum(nums, target):
    # Outline (write your plan here first):
    # Restate: Find two indices i < j such that nums[i] + nums[j] == target.
    # Example: nums = [2, 7, 11, 15], target = 9 -> 2 + 7 = 9 -> [0, 1]
    # Approach: Keep a dictionary mapping seen numbers to their indices.
    # For each (i, num), check if (target - num) is already in the dictionary.
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def max_profit(prices):
    # Outline:
    # Restate: Buy on one day and sell on a later day to maximize profit (or 0).
    # Example: [7, 1, 5, 3, 6, 4] -> buy at 1, sell at 6 -> profit = 5.
    # Approach: Track the lowest price seen so far as we scan left to right,
    # and update best profit with (current_price - min_price).
    min_price = float("inf")
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best:
            best = price - min_price
    return best


def max_subarray(nums):
    # Outline:
    # Restate: Find the largest sum of any contiguous slice of nums.
    # Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> [4, -1, 2, 1] -> sum = 6.
    # Approach (Kadane's algorithm): At each number, decide whether to extend
    # the current subarray or start fresh at the current number. Track the max.
    current_sum = nums[0]
    best_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Restate: Check if every opening bracket has a matching closing bracket in order.
    # Example: "([{}])" -> True, "([)]" -> False, "(((" -> False.
    # Approach: Push opening brackets onto a stack. On a closing bracket, check
    # that the stack isn't empty and the top matches. At the end, stack must be empty.
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))               # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))           # 5
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(is_balanced("([{}])"))                    # True


if __name__ == "__main__":
    main()
