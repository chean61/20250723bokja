import google.generativeai as genai 
import json

genai.configure(api_key="AIzaSyDszjDvADxJQ3UPBHMNlguWw8axL-IuCrM")

model = genai.GenerativeModel('gemini-pro')

keyword = "물리학"

prompt = f"""다음 조건에 맞춰 "{keyword}" 에 대해 퀴즈를 JSON 형식으로 3개 출제하시오.
- 주어진 주제에 대해 5개 보기가 있는 객관식 문제 3개 생성
- 문제와 보기는 한국어로 작성
- 정답은 한 개만 있고, 보기 앞에 숫자는 없어야 함
- JSON 형태로 문제, 보기 5개(리스트), 정답, 해설을 생성. key 이름은 각각 
question, options, answer, comment라고 하기
- 출력은 "["부터 시작"""

response = model.generate_content(prompt)

# 문제 생성(json 형식을 파이썬 개체로)

questions = json.loads(response.text)

# 퀴즈 풀기

score = 0

for idx, question in enumerate(questions, start=1): # 1번부터 문제 출력
    print(f"Questions {idx}: {question['question']}")
    print("Options: ")
    
    for i, option in enumerate(question['options'], start=1): # 선택지 출력 
        print(f"{i}. {option}")
    
    user_answer = input("Your answer (1-5): ")
    user_answer_index = int(user_answer) - 1

    if question['options'][user_answer_index] == question['answer']: # 사용자가 선택한 선택지가 정답지와 같으면
        print("Correct!") # Correct
        print('')
        score += 1
    else: # 다르면 
        print("Wrong answer") # Wrong
        print('')
        print(f"정답: {question['answer']}")
        print(f"풀이: {question['comment']}")
    
    print('')

print("당신의 점수는", score, "점 입니다.")
'''
<생성된 questions json 파일>
[{'question': '광합성을 하는 유기체로 다음 중 올바른 것은?', 
'options': ['식물', '동물', '미생물', '버섯', '박테리아'], 
'answer': '식물', 
'comment': '광합성은 식물의 녹색 엽록체에서 일어나는 과정입니다.'}, 
{'question': '광합성 반응식에서 소비되는 물질로 다음 중 올바른 것은?', 
'options': ['산소', '이산화탄소', '물', '글루코스', '질소'], 
'answer': '물', 
'comment': '광합성은 물 분자를 분해하여 산소를 방출하는 과정입니다.'}, 
{'question': '광합성에 필요한 원소로 다음 중 올바른 것은?', 
'options': ['탄소', '수소', '질소', '마그네슘', '아연'], 
'answer': '마그네슘', 
'comment': '마그네슘은 엽록체에서 엽록소의 중심 이온으로 역할을 합니다.'}]
'''
