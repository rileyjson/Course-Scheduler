import unittest
from Schedule import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student() 
        self.student.read_courses_from_file("classes.txt")

    def test_search_courses(self):
        # Test adding multiple courses without conflicts
        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")],
            "CS102": [("Section2", "Tue", "13-15")],
            "CS103": [("Section3", "Wed", "09-11")]
        }
        courses_to_search = ["CS101", "CS102", "CS103"]
        result = self.student.add_courses(courses_to_search)
        self.assertIsNone(result)
        self.assertEqual(len(self.student.schedule), 3)  # Assuming three courses were 


    def test_read_courses_from_file(self):
        # Test if read_courses_from_file method properly reads the file and populates the courses_dict
        self.student.read_courses_from_file("classes.txt")
        self.assertEqual(len(self.student.courses_dict), 5)  # Adjust the expected count as per the test file


    def test_course_not_exist(self):
        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")]}
        courseNumber = ["CS201"]

        result = self.student.add_courses(courseNumber)
        
        expected = "Invalid course, try again"
        self.assertNotEqual(result, expected)
    

    def test_no_time_conflict_with_registered_courses(self):
    # Input data
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section2", "Tue", "13-15")
        self.assertFalse(self.student.time_conflict(self.student.schedule[0], course_info))

        
    
    def test_over_wanted_classes(self):
        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")],
            "CS102": [("Section2", "Tue", "13-15")],
            "CS103": [("Section3", "Wed", "09-11")]
        }

        courses_to_add = ["CS101", "CS102", "CS103","MATH165"]
       
        result = self.student.add_courses(courses_to_add)
        self.assertIsNotNone(result)
        self.assertNotEqual(len(self.student.schedule), 3)

        
            
    #Student who need special assistance
    #The student need a gap time between each of the class
    #This is testing about student can view clearly the detail of the course times
    def test_view_available_courses(self):
        expected_output = "Available Courses:\nCS120 \nCOMM210 \nCS121 \nCS222 \nMATH165 \n"
        result = self.student.view_available_courses()
        self.assertEqual(result, expected_output)


    #cyari12 done
    def test_add_courses(self):
        # Test adding multiple courses without conflicts
        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")],
            "CS102": [("Section2", "Tue", "13-15")],
            "CS103": [("Section3", "Wed", "09-11")]
        }
        courses_to_add = ["CS101", "CS102", "CS103"]
        result = self.student.add_courses(courses_to_add)
        self.assertIsNone(result)
        self.assertEqual(len(self.student.schedule), 3)  # Assuming three courses were added

     # Test for time conflict when there's a conflict
    def test_time_conflict(self):
        # Test for time conflict when there's no conflict
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section2", "Tue", "13-15")
        self.assertFalse(self.student.time_conflict(self.student.schedule[0], course_info))

        # Test for time conflict when there's a conflict
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section1", "Mon", "11-13")
        self.assertTrue(self.student.time_conflict(self.student.schedule[0], course_info))


     #testing for full time student wih live in campus and willing to take 15 credits   
    def test_fulltimestudent_in_campus(self):
        self.student.courses_dict = {
        'CS120': [('001', 'MWF', '0900-0950')],
        'COMM210': [('002', 'MWF', '0800-0850')],
        'CS121': [('001', 'TR', '1230-1345')],
        'CS222': [('005', 'TR', '1400-1515')],
        'MATH165': [('001', 'TR', '1100-1215')]
    }

        courses_to_add = ["CS120", "COMM210", "CS121", "CS222", "MATH165"]
        result = self.student.add_courses(courses_to_add)
        self.assertIsNone(result)
        # Assuming you expect all five courses to be added
        self.assertEqual(len(self.student.schedule), 5)


    #Not to get overlapping course time people who commute to campus and taking classes
    #The student only can go Tuesday and Thursday
    #Testing for the student who only can go TR, not to get overlapping course time
    def test_overlapping_course_time(self):
        self.student.schedule = [("Section1", "TR", "10-12")]
        course_info = ("Section1", "TR", "11-13")
        self.assertTrue(self.student.time_conflict(self.student.schedule[0], course_info))
       

        # Test for time conflict when there's a conflict
        self.student.schedule = [("Section1", "Mon", "10-12")]
        course_info = ("Section1", "Mon", "11-13")
        self.assertTrue(self.student.time_conflict(self.student.schedule[0], course_info))



        
    def test_register_reduced_course_load(self):

        self.student.courses_dict = {
            "CS101": [("Section1", "Mon", "10-12")],
            "CS102": [("Section2", "Tue", "13-15")]}
        
        courses_to_add = ["CS101", "CS102"]
        result = self.student.add_courses(courses_to_add)
        self.assertIsNone(result)
        self.assertEqual(len(self.student.schedule), 2)  


if __name__ == "__main__":
    unittest.main()
