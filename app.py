import streamlit as st
import time
import random

from questions import questions

st.write("st.session_state", st.session_state)

available_lifelines = ["5050", "Phone a Friend", "Audience Poll", "Power Paplu", "Change The Question", 'Double Dip']

# Initialize session state to store lifelines
if 'lifelines' not in st.session_state:
    st.session_state.lifelines = available_lifelines.copy()

if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0

if "score" not in st.session_state:
    st.session_state['score'] = 0

if "display_success" not in st.session_state:
    st.session_state['display_success'] = False

if "display_error" not in st.session_state:
    st.session_state['display_error'] = False

if "display_options" not in st.session_state:
    st.session_state['display_options'] = questions[st.session_state['current_question']]['options']

if 'is_double dip' not in st.session_state:
    st.session_state['is_double_dip'] = 0


# Define your quiz questions and answers

def _50505_lifeline():
    question = questions[st.session_state.current_question]
    correct_option = question['correct_option']
    incorrect_option = question['options'].copy()
    incorrect_option.remove(correct_option)
    st.session_state.display_options =  [random.choice(incorrect_option), correct_option]
    pass

def power_paplu():
    with st.sidebar:
        lifeline = [i for i in available_lifelines if i != 'Power Paplu' and i not in st.session_state.lifelines]
        revive  = st.selectbox("Choose the lifeline", options = lifeline)
        st.session_state.lifelines.append(revive)

def audience_poll():
    options = st.session_state.display_options
    votes = {}
    for option in options:
        votes[option] = random.randint(100, 1000)

    votes[questions[st.session_state.current_question]['correct_option']] *= 1.5 #higher vote percent for correct answer
    total_votes = sum(votes.values())
    percentages = {option: (count / total_votes) * 100 for option, count in votes.items()}
    
    st.bar_chart(percentages)

# Define the votes

    pass

def change_the_question():
    st.session_state.current_question += 1


def click_lifeline(*args):
    lifeline = ''.join(args)
    st.write(lifeline)
    if lifeline == '5050':
        _50505_lifeline()
    if lifeline == "Power Paplu":
        power_paplu()
    if lifeline == 'Change The Question':
        change_the_question()
    if lifeline == 'Audience Poll':
        audience_poll()
    if lifeline == 'Double Dip':
        st.session_state.is_double_dip = 1
        print("double dip")
        print(st.session_state)


    st.session_state.lifelines.remove(lifeline)
    st.session_state.use_lifelines = False



# Checkbox to enable/disable lifelines
with st.sidebar:
    use_lifelines = st.sidebar.checkbox("Use Lifelines", key='use_lifelines')
    if use_lifelines:
        for lifeline in st.session_state.lifelines:
            st.button(lifeline, on_click = click_lifeline, args = lifeline)


st.title("KBC")




def submit_btn_click(**kwargs):
    selected_option = kwargs['selected_option']
    qno = st.session_state.current_question
    correct_answer = questions[qno]['correct_option']
    correct_answer, selected_option
    if correct_answer == selected_option:
        # st.session_state.display_success = True
        # st.session_state.display_true = False
        # st.write("CORRECT ANSWER")
        container = st.empty()
        container.success("Correct answer")
        time.sleep(2)
        container.empty()
        st.session_state.score += 1
        st.session_state.current_question += 1
        st.session_state.display_options = questions[st.session_state.current_question]['options']
    elif st.session_state.is_double_dip >= 1:
        container = st.empty()
        container.info("Incorrect Try Again")
        time.sleep(2)
        container.empty()
        st.is_double_dip = False
        st.session_state.display_options = questions[st.session_state.current_question]['options']
        st.session_state.is_double_dip -= 1

    else:
        # st.write("WRONG ANSWER")
        # st.session_state.display_error = True 
        # st.session_state.display_success = False
        container = st.empty()
        container.error("Incorrect Answer")
        time.sleep(5)
        container.empty()
        st.session_state.current_question = 0
        st.session_state.display_options = questions[st.session_state.current_question]['options']

        # st.session_state.display_restart_btn = True

    # st.session_state.current_question+= 1


if st.session_state.current_question < 10:
    print(st.session_state)
    st.write("Question:", questions[st.session_state.current_question]["question"])
    selected_option = st.radio("Options:", st.session_state.display_options)
    st.button("Submit", on_click = submit_btn_click,  kwargs = {"selected_option": selected_option})
    # container = st.empty()
    # if st.session_state.display_success:
    #     container = st.empty()
    #     container.success("Correct answer")
    #     time.sleep(2)
    #     container.empty()
    #     st.session_state.score += 1
    #     st.session_state.current_question += 1
    #     st.session_state.display_success = False
    
    # if st.session_state.display_error:
    #     container = st.empty()
    #     container.error("Incorrect answer")
    #     time.sleep(2)
    #     container.empty()
    #     st.session_state.score  = 0
    #     st.session_state.current_question = 0
    #     st.session_state.display_error = False
    # st.session_state.display_success, st.session_state.display_error



else:
    st.write("Congratulations! You have completed the Krodpati")

# st.button("Next Question") if current_question < len(question÷/s) else st.button("Restart Quiz")

