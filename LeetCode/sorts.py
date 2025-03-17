class Solution():
    #Goes through every number (n) and keeps bringing the (n+1) highest number all the way to the end
    #i.e 0 => 1,2,3,4,5,6,7,8,9, 1 => 2,3,4,5,6,7,8,9, 2 => 3,4,5,6,7,8,9...
    def bubble_sort(list):
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if list[j] < list[i]:
                    (list[i], list[j]) = (list[j], list[i])
        return list
    #Iterating over every number (n), find the index (n > 1) of the smallest number and puts it at the front
    #I.e 0 <= 1,2,3,4,5,6,7,8,(9), 1 <= 2,3,4,5,(6),7,8,9...
    def selection_sort(list):
        for i in range(len(list)):
            lowest_index = i
            changed = False
            for j in range(i + 1, len(list)):
                if (list[j] < list[lowest_index]):
                    lowest_index = j
                    changed = True
            if changed:
                list[i], list[lowest_index] = list[lowest_index], list[i]
        return list
    #Starting from the 3rd number (n), work backwards (n-1) switching numbers (n-2) until at the beginning of the list
    # 2 <= 1, 3 <= 2,1, 4 <= 3,2,1, 5 <= 4,3,2,1...
    def insertion_sort(list):
        for i in range(2, len(list) + 1):
            for j in range(i - 1, 0, -1):
                if list[j - 1] > list[j]:
                    list[j - 1], list[j] = list[j], list[j-1]
        return list

print(Solution.bubble_sort([1, -5, 4, 2, 9, 10003, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
print(Solution.selection_sort([1, -5, 4, 2, 9, 10003, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
print(Solution.insertion_sort([1, -5, 4, 2, 9, 10003, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))