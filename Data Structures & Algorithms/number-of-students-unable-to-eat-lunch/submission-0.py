class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        2 type sws: circular - 0 or square - 1
        students -> queue
        sanwiches -> stack
        each student -> 1 sw
        # sw = # students

        like -> remove from queue
        dislike -> move to queue's end

        return # unable to eat

        EX: 
        students = [1,1,0,0], sandwiches = [0,1,0,1]
        sq , sq, cir, cir.                cir, sq, cir, sq
        -> 1, 0, 0, 1
        -> 0, 0, 1, 1
        -> 0, 1, 1.                         1, 0, 1
        -> 1, 1, 0
        -> 1, 0,                            0, 1
        -> 0, 1

        O(n)/O(1)
        """

        res = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0: 
                res -= 1
                count[s] -= 1

            else:
                return res
        
        return res





