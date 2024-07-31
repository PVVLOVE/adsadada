from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    forwarded_for = request.headers.get('X-Forwarded-For')
    user_ip = forwarded_for.split(',')[0] if forwarded_for else request.remote_addr
    return render_template('index.html', user_ip=user_ip)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        forwarded_for = request.headers.get('X-Forwarded-For')
        user_ip = forwarded_for.split(',')[0] if forwarded_for else request.remote_addr
        content = request.form['message']
        messages.append({'ip': user_ip, 'message': content})
        return redirect(url_for('chat'))
    return render_template('chat.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
