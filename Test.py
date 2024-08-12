def no_musical(start_class, end_class, musical_performed_every, enrolment_duration):
    music_years = []
    all_years = []
    
    def time(years):
        year = []
        for x in range(years, years + enrolment_duration):
            year.append(x)
        return(year)
    
    for x in range(start_class, end_class + 1):
         all_years.append(x)
        
    while start_class <= end_class:
        music_years.append(start_class)
        start_class += musical_performed_every

    for x in music_years:
        if x not in time(all_years):
            print(x)
    
no_musical(2000, 2020, 5, 4)
