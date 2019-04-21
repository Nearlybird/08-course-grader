def course_grader(test_scores):
    ave_score = sum(test_scores)/int(len(test_scores))
    output = 0
    
    if ave_score < 70:
        output = output + 1
        
    elif ave_score >= 70:
        for score in (test_scores):
            if score < 50:
                output = output + 1
            else:
                output = output
    
    if output > 0:
        return "fail"
    else:
        return "pass"
