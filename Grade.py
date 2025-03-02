score = float(input("กรุณากรอกคะแนนของคุณ: "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"คะแนนคือ {score} ได้เกรด {grade}")
