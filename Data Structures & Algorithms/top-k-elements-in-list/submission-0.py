class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = [(count, num) for num, count in freq.items()]

        heap = arr[:k]
        heapq.heapify(heap)  # O(k)

        for count, num in arr[k:]:
            if count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

        return [num for count, num in heap]