#timetable is a dictionary that is linked one(days) to many(time)
#timetable = {'days':['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
#             'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
#             }

#halls is a dictionary that is linked one(hall) to one(capacity)
halls = {'hall':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 
         'capacity':[200, 250, 300, 100, 150, 250, 400, 500, 1000, 250, 750, 2000, 100, 50, 600, 450, 360, 500, 700, 5000, 2000, 1000, 200, 500, 150, 500]
         }

#schedule is a dictionary that saves the 
schedule = {'monday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                      'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                      },
            'tuesday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                       'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                       },
            'wednesday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                         'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                         'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                         },
            'thursday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                        'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                        },
            'friday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                      'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                      },
            'saturday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                        'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                        },
            'sunday':{'time':['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'], 
                      'course':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'hall':['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                      'size':['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                      }
            }

#while true(while the user wants to keep planning a schedule, get day, time, course, place from user
while True:
    schedule_day = input("Enter the day of the class:\n")
    schedule_time = input("Enter the time of the class:\n") + ":00"
    schedule_size = int(input("Enter the size of the class:\n"))
    schedule_course = input("Enter the course of the class:\n")
    schedule_hall = input("Enter the hall of the class:\n")
    
    #there are 14 timestamps
    for i in range(14):
        if schedule[schedule_day.lower()]['time'][i] == schedule_time:
            if schedule[schedule_day.lower()]['course'][i] != '':
                print("There is a class already scheduled for this time")
                break
            else:
                #There are 26 halls
                for j in range(26):
                    if halls['hall'][j] == schedule_hall:
                        if halls['capacity'][j] < schedule_size:
                            print("The hall is too small for the class. Kindly select a different hall.")
                            print(halls)
                            break
                        else:
                            schedule[schedule_day.lower()]['course'][i] = schedule_course
                            schedule[schedule_day.lower()]['hall'][i] = schedule_hall
                            schedule[schedule_day.lower()]['size'][i] = schedule_size
                            break
                break
    
    keep_setting = input("Enter 1 to continue setting the schedule, 2 to see the current schedule, or 3 to end\n")
    if keep_setting == '3':
        break
    if keep_setting == '2':
        print(schedule)
        keep_setting = input("Enter 1 to continue setting the schedule or 2 to end\n")
        if keep_setting == '2':
            break