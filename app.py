import streamlit as st
import time
import random
import matplotlib.pyplot as plt  # Import Matplotlib

from all_questions import questions

# questions = random.shuffle(all_questions.copy())
# st.write("st.session_state", st.session_state)

available_lifelines = ["5050", "Phone a Friend", "Audience Poll", "Power Paplu", "Change The Question", 'Double Dip']

# Initialize session state to store lifelines
if 'lifelines' not in st.session_state:
    st.session_state.lifelines = available_lifelines.copy()

if 'current_lifeline' not in st.session_state:
    st.session_state.current_lifeline = None

if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0
    random.shuffle(questions)
    # global quz
    # questions = random.shuffle(all_questions.copy())
    # random.shuffle(questions)

if "score" not in st.session_state:
    st.session_state['score'] = 0

if "display_success" not in st.session_state:
    st.session_state['display_success'] = False

if "display_error" not in st.session_state:
    st.session_state['display_error'] = False

if "display_options" not in st.session_state:
    st.session_state['display_options'] = questions[st.session_state['current_question']]['options']


st.title("Kaun Banega Crorepati :moneybag:")
st.divider()
status = st.empty()


def _50505_lifeline():
    question = questions[st.session_state.current_question]
    correct_option = question['correct_option']
    incorrect_option = question['options'].copy()
    incorrect_option.remove(correct_option)
    st.session_state.display_options =  [random.choice(incorrect_option), correct_option]
    pass

def pp_change():
    if st.session_state.revive != "":
        st.session_state.lifelines.append(st.session_state.revive)
    

def power_paplu():
    with st.sidebar:
        lifeline = [i for i in available_lifelines if i != 'Power Paplu' and i not in st.session_state.lifelines]
        lifeline = [""] + lifeline
        revive  = st.selectbox("Choose the lifeline", options = lifeline, key = 'revive', on_change = pp_change)

def audience_poll():
    options = st.session_state.display_options
    votes = {}
    for option in options:
        votes[option] = random.randint(100, 1000)

    votes[questions[st.session_state.current_question]['correct_option']] *= 1.5 #higher vote percent for correct answer
    total_votes = sum(votes.values())
    percentages = {option: (count / total_votes) * 100 for option, count in votes.items()}
    fig, ax = plt.subplots()
    bars = ax.bar(percentages.keys(), percentages.values())
    ax.set_ylabel('Percentage of Votes')
    ax.set_title('Audience Poll Results')

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%', (bar.get_x() + bar.get_width() / 2, height),
                    ha='center', va='bottom')

    # Display the bar chart inside the container
    status.pyplot(fig)
    time.sleep(5)
    status.empty()
    # status.bar_chart(percentages)


def change_the_question():
    st.session_state.current_question += 1
    st.session_state.display_options = questions[st.session_state.current_question]['options']

def phone_a_friend():
    qno = st.session_state.current_question
    correct_answer = questions[qno]['correct_option']
    # staus = st.empty()
    status.info("Correct answer is " + correct_answer )
    time.sleep(5)
    status.empty()


def click_lifeline(*args):
    lifeline = ''.join(args)
    # st.write(lifeline)
    if lifeline == '5050':
        _50505_lifeline()
    if lifeline == "Power Paplu":
        power_paplu()
    if lifeline == 'Change The Question':
        change_the_question()
    if lifeline == 'Audience Poll':
        audience_poll()
    if lifeline == 'Double Dip':
        # st.multisele
        st.session_state.current_lifeline = 'Double Dip'
        # print("double dip")
        # print(st.session_state)
    if lifeline == 'Phone a Friend':
        phone_a_friend()


    st.session_state.lifelines.remove(lifeline)
    st.session_state.use_lifelines = False




# Checkbox to enable/disable lifelines
with st.sidebar:
    # st.title("Kaun Banega Crorepati :moneybag:")

    use_lifelines = st.sidebar.checkbox("Use Lifelines", key='use_lifelines')
    if use_lifelines:
        for lifeline in st.session_state.lifelines:
            st.button(lifeline, on_click = click_lifeline, args = lifeline)
    st.header("Score")
    st.write(st.session_state.score)







def restart():
    # status.write("Next")
    qno = st.session_state.current_question
    correct_answer = questions[qno]['correct_option']
    # container = st.empty()
    status.warning("Incorrect, correct answer is " + correct_answer)
    time.sleep(2)
    status.empty()
    
    random.shuffle(questions)
    ss = st.session_state
    st.session_state.score = 0
    st.session_state.current_question = 0
    ss.current_lifeline = available_lifelines
    ss.current_lifeline = None
    ss.display_success = False
    ss.display_error = False
    ss.display_options = questions[ss.current_question]['options']

    with st.status("Restarting.. "):
        time.sleep(2)

def next():
    # status.write("Next")
    # container = st.empty()
    status.success("Correct answer")
    time.sleep(2)
    status.empty()

    ss = st.session_state
    ss.current_question +=1
    ss.score += 1
    ss.display_options = questions[ss.current_question]['options']
    ss.current_lifeline = None

def submit_btn_click(**kwargs):
    # print("session state in submit")
    # print(st.session_state)
    # print()
    selected_option = kwargs['selected_option']
    qno = st.session_state.current_question
    correct_answer = questions[qno]['correct_option']
    # correct_answer, selected_option
    if correct_answer == selected_option:
        next()

    elif st.session_state.current_lifeline == "Double Dip" :
        # container = st.empty()
        status.info("Incorrect Try Again")
        time.sleep(2)
        status.empty()
        st.session_state.is_double_dip = False
        st.session_state.current_lifeline = None
        st.session_state.display_options = questions[st.session_state.current_question]['options']

    else:
        restart()

    pass



if st.session_state.current_question < 10:
    print("Session State: ")
    print(st.session_state)
    print()
    lab = f"Question {st.session_state.current_question + 1}: "
    # st.subheader(lab)
    st.subheader(lab + questions[st.session_state.current_question]["question"])
    # st.divider()
    selected_option = st.radio("Options are :", st.session_state.display_options)
    st.button("Lock the Answer", on_click = submit_btn_click,  kwargs = {"selected_option": selected_option})




else:
    st.success("Congratulations! You have won the game")

# st.button("Next Question") if current_question < len(question÷/s) else st.button("Restart Quiz")

