# Input: list with numbers, number.
# Output: Approved students, failed students and average grade.
# Restrictions: list must be type list and not empty

def calculateGrades (gradesList, passigGrade):
      
      if not isinstance (gradesList, list) and gradesList != []:
            return "error"
      
      approved = 0
      failed = 0
      total = 0
      length = len(gradesList)
      
      for studentGrade in gradesList:
            total += studentGrade
            
            if studentGrade >= passigGrade:
                  approved += 1
            else:
                  failed += 1
                  
      average = total / length
      
      print("Approved students: ", approved)
      print("Failed students: ", failed)
      print("Average grade: ", average)
      
      return [approved, failed, average]

calculateGrades ([66, 78, 90, 50, 44, 98, 96], 70)
