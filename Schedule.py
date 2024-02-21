class Student:
    def __init__(self):
        self.schedule = []
        self.courses_dict = {}

    def add_courses(self, course_codes):
        class_combinations = [] #this is a list to store all combinations of courses entered by the user
        #Calls recursive function to compare 'course_codes', (given by user in main), starting at the index 0 course
        
        self.recursive_course_compares(course_codes, 0, [], class_combinations)  
       
        for combination in class_combinations: #goes through all combos in class_combinations list of courses
            formatted_schedule = []                              
            
            for i in range(len(combination)): 
                course_info = combination[i]       #formats courses
                section, days, time_range = course_info
                start_time, end_time = time_range.split('-')
                formatted_schedule.append(f"{course_codes[i]}: {section}, {days}, {start_time}-{end_time}")

            #first conflict check call
            if not self.adding_check_conflicts(formatted_schedule):
                self.schedule = formatted_schedule  #adds courses to 'schedule'
                return None 

        return "Schedule can't be made."

    def recursive_course_compares(self, course_codes, index, combinations2, combinations1):

        if index == len(course_codes): #Base Case
            combinations1.append(list(combinations2))
            return
                

        course_code = course_codes[index] #this gets every class from the txt file thats course code is = 
        if course_code in self.courses_dict: #to the ones searched by the user   
            available_classes = self.courses_dict[course_code]

            for chosen in available_classes: 
                section, days, time_range = chosen
                start_time, end_time = time_range.split('-') 
                formatted_course_info = (section, days, f"{start_time}-{end_time}")

            #if no time conflict, add course to combinations2 list
                if not self.time_conflict_loop(formatted_course_info, combinations2):
                    combinations2.append(formatted_course_info)

                    #adds 1 to index and calls itself, does process again.
                    self.recursive_course_compares(course_codes, index + 1, combinations2, combinations1)

                #backtracking, It removes the last added course before trying the next section of same course
                    combinations2.pop() 


    def time_conflict_loop(self, course_info, combinations2): #checks for conflicts within a set of courses.
    
        for existing_course_info in combinations2:
            if self.time_conflict(course_info, existing_course_info):
                return True 
        return False 

    def time_conflict(self, course_info_1, course_info_2): #this checks for conflicts between 2 courses.
  
        days_1, time_range_1 = course_info_1[1], course_info_1[2].split("-") 
        if len(time_range_1) < 2:
            return False  

        start_time_1, end_time_1 = int(time_range_1[0]), int(time_range_1[1]) #formats times into int so they can be compared.
        
        days_2, time_range_2 = course_info_2[1], course_info_2[2].split("-")
        if len(time_range_2) < 2:
            return False  

        start_time_2, end_time_2 = int(time_range_2[0]), int(time_range_2[1]) 

        if days_1 != days_2:
            return False

        return start_time_1 < end_time_2 and start_time_2 < end_time_1
        
    def adding_check_conflicts(self, schedule): #compares pairs of courses in 'self.schedule'
        for i in range(len(schedule)):               
            for j in range(i + 1, len(schedule)):
                if self.time_conflict(schedule[i], schedule[j]):
                    return True
        return False  

    def read_courses_from_file(self, file_path):
        with open(file_path, 'r') as file:         
            for line in file:
                details = line.split()
                course_code = details[0]
                course_section = details[1]
                course_days = details[2]
                course_start = details[3]
                course_end = details[4]
                if course_code not in self.courses_dict:
                    self.courses_dict[course_code] = []
                self.courses_dict[course_code].append((course_section, course_days, f"{course_start}-{course_end}"))

    def view_available_courses(self): #prints list of unique courses at beginning of program
        available_courses_str = "Available Courses:\n"
        for course_code, course_details_list in self.courses_dict.items():
            for i in course_details_list:   
                if course_code not in available_courses_str:
                    available_courses_str += f"{course_code} \n"
        return available_courses_str

    def main(self):
        self.read_courses_from_file("classes.txt")
        print(self.view_available_courses())

        num_courses = int(input("Enter the number of courses you'd like to register for: "))
        course_codes = []
        
        for i in range(num_courses):
            course_code = input("Enter the course code: ")
            course_codes.append(course_code)

        if self.add_courses(course_codes):
            print("Schedule can't be made.")
        else:
            print("\nYour Schedule:")
            for course_info in self.schedule:
                print(course_info)
            

student_instance = Student()
student_instance.main()
