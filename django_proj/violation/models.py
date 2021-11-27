from django.db import models

class Records(models.Model):
    course = [
        ('BET', 'Bachelor of Engineering Technology'),
        ('BSE', 'Bachelor of Science in Engineering'),
        ('BSIE', 'Bachelor of Science in Industrial Education'),
        ('BTTE', 'Bachelor of Technical Teacher Education'),
    ]

    major = [
        ('AET', 'Automotive'),
        ('CT', 'Civil'),
        ('COET', 'Computer'),
        ('ESET', 'Electronics'),
        ('EET', 'Electrical'),
        ('MPET', 'Mechanical'),
        ('PPET', 'Powerplant'),
        ('ICT', 'Information Communication Technology'),
        ('IA', 'Industrial Arts'),
        ('CPET', 'Computer Programming'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]

    section = [
        ('S-1A', 'S-1A'),
        ('NS-1B', 'NS-1B'),
        ('S-2A', 'S-2A'),
        ('NS-2B', 'NS-2B'),
        ('S-3A', 'S-3A'),
        ('NS-3B', 'NS-3B'),
        ('S-4A', 'S-4A'),
        ('NS-4A', 'NS-4A'),
    ]

    existingViolation = [
        ('Littering', 'Littering'),
        ('Loitering', 'Loitering'),
        ('Vandalism', 'Vandalism'),
        ('Gambling', 'Gambling'),
        ('Improper haircut', 'Improper haircut'),
        ('Improper public behavior', 'Improper public behavior'),
        ('Improper uniform', 'Improper uniform'),
        ('Wearing of hats in class', 'Wearing of hats in class'),
        ('Unauthorized use of water', 'Unauthorized use of water'),
        ('Use of gadgets during class', 'Use of gadgets during class'),
        ('Wearing of piercing', 'Wearing of piercing'),
        ('Cross-dressing', 'Cross-dressing'),
    ]

    existingComSer = [
        ('Summer break volunteer', 'Summer break volunteer'),
        ('Cafeteria volunteer', 'Cafeteria volunteer'),
        ('Organizing recyclables', 'Organizing recyclables'),
        ('Waste segregation', 'Waste segregation'),
        ('Planting plants', 'Planting plants'),
        ('Library personnel', 'Library personnel'),
        ('Garbage collection volunteer', 'Garbage collection volunteer'),
        ('Community sweeping', 'Community sweeping'),
    ]

    addViolation = [
        ('Littering', 'Littering'),
        ('Loitering', 'Loitering'),
        ('Vandalism', 'Vandalism'),
        ('Gambling', 'Gambling'),
        ('Improper haircut', 'Improper haircut'),
        ('Improper public behavior', 'Improper public behavior'),
        ('Improper uniform', 'Improper uniform'),
        ('Wearing of hats in class', 'Wearing of hats in class'),
        ('Unauthorized use of water', 'Unauthorized use of water'),
        ('Use of gadgets during class', 'Use of gadgets during class'),
        ('Wearing of piercing', 'Wearing of piercing'),
        ('Cross-dressing', 'Cross-dressing'),
    ]

    addComSer = [
        ('Summer break volunteer', 'Summer break volunteer'),
        ('Cafeteria volunteer', 'Cafeteria volunteer'),
        ('Organizing recyclables', 'Organizing recyclables'),
        ('Waste segregation', 'Waste segregation'),
        ('Planting plants', 'Planting plants'),
        ('Library personnel', 'Library personnel'),
        ('Garbage collection volunteer', 'Garbage collection volunteer'),
        ('Community sweeping', 'Community sweeping'),
    ]

    offenseType = [
        ('First offense', 'First offense'),
        ('Second offense', 'Second offense'),
        ('Third Offense', 'Third Offense'),
    ]


    #may mali sa student ID, student no, schoolyear = dapat charfield
    studentID = models.FloatField(verbose_name = 'studentID')
    lastName = models.CharField(max_length = 50, verbose_name = 'lastName')
    firstName = models.CharField(max_length = 50, verbose_name = 'firstName')
    middleName = models.CharField(max_length = 50, blank = True, verbose_name = 'middleName')
    course = models.CharField(max_length = 5, choices = course, verbose_name = 'course', default = '')
    major = models.CharField(max_length = 10, choices = major, verbose_name = 'major', default = '')
    section = models.CharField(max_length = 10, choices = section, verbose_name = 'section', default = '')
    studentNo = models.DecimalField(max_digits = 4, decimal_places = 0, verbose_name = 'studentNo')
    schoolYear = models.FloatField(verbose_name = 'schoolYear')
    existingViolation = models.CharField(max_length = 100, blank = True, choices = existingViolation, verbose_name = 'existingViolation', default = '')
    existingComSer = models.CharField(max_length = 100, choices = existingComSer, blank = True, verbose_name= 'existingComSer', default= '')
    remainComSerTime = models.DecimalField(max_digits= 2, decimal_places= 0, blank= True, verbose_name= 'remainComSerTime')
    addViolation = models.CharField(max_length= 100, choices= addViolation, verbose_name= 'addViolation', default= '')
    addComSer = models.CharField(max_length= 100, choices= addComSer, verbose_name= 'addComSer', default= '')
    offenseType = models.CharField(max_length= 25, choices= offenseType, verbose_name= 'offenseType', default= '')
    addComSerTime = models.DecimalField(max_digits=2, decimal_places= 0, verbose_name= 'addComSerTime')


    def __str__(self):
        return self.studentID

        
