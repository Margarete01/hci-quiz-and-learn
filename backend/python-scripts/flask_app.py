from flask import Flask
import question

app = Flask(__name__)

@app.route('/api/question_answers', methods=['GET'])
def get_question_answers():
    return question.get_question_answers()

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return question.get_questions()

@app.route('/api/answers', methods=['GET'])
def get_answers():
    return question.get_answers()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7990)