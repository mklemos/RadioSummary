from mesop import Mesop, route, request, render_template, jsonify
from main import start_capture_process  # Import your main function

app = Mesop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/capture-and-summarize', methods=['POST'])
def capture_and_summarize():
    data = request.json
    station = data['station']
    
    # Assuming start_capture_process is modified to return transcription and summary
    transcription, summary = start_capture_process(station)
    
    return jsonify({'transcription': transcription, 'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)

