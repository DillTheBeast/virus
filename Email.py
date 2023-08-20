

def questions():
    person = input('What subject do u want to email to')
    reason = input('What is the reason for this email\nPlease choose meeting, or question')

    if reason == 'meeting':
        time = input('What time would you like to meet the teacher at?')

    elif reason == 'question':
        question = input('What question would you like to ask?')

