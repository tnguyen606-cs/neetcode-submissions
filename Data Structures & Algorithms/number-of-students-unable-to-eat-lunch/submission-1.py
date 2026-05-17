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

        O(nk)/O(n)
        """

        n = len(students)
        queue = deque(students)

        for s in sandwiches:
            count = 0
            while count < n and queue[0] != s:
                cur = queue.popleft()
                queue.append(cur)
                count += 1

            if queue[0] == s:
                queue.popleft()
                n -= 1
            else:
                break

        return n








