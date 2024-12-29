from dict import StudentTwo
StudentTwoAttributes = {
    "height": 5.6,
    "weight": 50,
    "eye_color": "brown",
}
StudentTwo["physical"] = StudentTwoAttributes
print(StudentTwo.get("physical").get("eye_color")) 