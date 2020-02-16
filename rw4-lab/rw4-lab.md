# testing examples
## Teacher

Trying to add a TA to a course
    method similar to addTA(TA, course)
        method should fail if:
            TA is invalid student id
            TA is already a TA of the course
            course is not valid or not taught by the professor

        method should succeed if:
            Student ID is valid and course is valid and belongs to teacher
    
Trying to remove a student from a course
    method similar to removeStudent(studentID, course)
        method should fail if:
            studentID is invalid
            studentID is not in the course already
            course is not taught by the professor

        method should succeed if:
            studentID is valid and belongs to a student in the course which is taught by the professor
