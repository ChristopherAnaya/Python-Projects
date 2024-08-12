def no_musical(start_class, end_class, musical_performed_every, enrolment_duration):
    music_years = set(range(start_class, end_class+1, musical_performed_every))
    years = set(range(start_class, start_class + enrolment_duration))
    
print(no_musical(2000, 2060, 5, 2))







def no_musical(start_class, end_class, musical_performed_every, duration_of_enrolment_in_school):
    # Step 1: Determine all the years when a musical is performed
    musical_years = set(range(start_class, end_class + 1, musical_performed_every))
    
    no_musical_classes = 0
    
    # Step 2: For each class, check if they overlap with a musical year
    for class_start in range(start_class, end_class + 1):
        class_years = set(range(class_start, class_start + duration_of_enrolment_in_school))
        
        # Step 3: Check for overlap
        if not class_years & musical_years:  # No overlap
            no_musical_classes += 1
            
    return no_musical_classes

# Example usage:
print(no_musical(2000, 2010, 5, 3))  # Output should be 4
