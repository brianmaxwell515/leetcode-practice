class Solution(object):
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


arr = [1024, 128, 512, 256, 64, 32, 16, 8, 4, 2, 1]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(Solution.sortByBits(1, arr))

# (錯誤答案)
# return sorted(arr, key=lambda x: bin(x).count('1'))

# 這個沒有考慮1的個數相同的情況下怎麼排序，題目要求是數值小的優先，
# 那就在後面加一個原值x就可以了，即(bin(x).count('1' ), x)，意思是先比較x中1的個數，再比較x的值
