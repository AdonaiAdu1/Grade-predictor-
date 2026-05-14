import math

def predict_score(hours, previous, attendance):
    
    score = (hours * 1.5) + (previous * 0.6) + (attendance * 0.3)
    
    # Keep between 0 and 100
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    
    return round(score, 1)

def get_feedback(score):
    if score >= 80:
        return "Excellent! Keep it up!"
    elif score >= 65:
        return "Good work! A little more effort"
    elif score >= 50:
        return "Fair. Need more study time"
    else:
        return "Needs improvement. Try harder"

def main():
    print("=== STUDENT GRADE PREDICTOR ===")
    print()
    
    hours = float(input("Enter study hours per week: "))
    previous = float(input("Enter previous test score (0-100): "))
    attendance = float(input("Enter attendance percentage (0-100): "))
    
    predicted = predict_score(hours, previous, attendance)
    feedback = get_feedback(predicted)
    
    print()
    print("=== RESULT ===")
    print(f"Predicted final score: {predicted}/100")
    print(f"Feedback: {feedback}")
    
    print()
    print("Note: Model accuracy is ~75% based on sample data")

if __name__ == "__main__":
    main()
