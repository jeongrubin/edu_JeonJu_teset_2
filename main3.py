import streamlit as st

# 연산 함수 정의
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

# Streamlit 애플리케이션 제목
st.title(":slot_machine: 정수빈 계산기")

# 사용자 입력
num1 = st.number_input("첫 번째 숫자 입력:", value=0.0)
num2 = st.number_input("두 번째 숫자 입력:", value=0.0)

# 연산 선택
operation = st.selectbox("원하는 연산 선택", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

# 버튼 클릭 시 연산 수행
if st.button("계산하기"):
    if operation == "덧셈":
        result = add(num1, num2)
        st.write(f"결과: {num1} + {num2} = {result}")
    elif operation == "뺄셈":
        result = subtract(num1, num2)
        st.write(f"결과: {num1} - {num2} = {result}")
    elif operation == "곱셈":
        result = multiply(num1, num2)
        st.write(f"결과: {num1} * {num2} = {result}")
    elif operation == "나눗셈":
        result = divide(num1, num2)
        st.write(f"결과: {num1} / {num2} = {result}")
