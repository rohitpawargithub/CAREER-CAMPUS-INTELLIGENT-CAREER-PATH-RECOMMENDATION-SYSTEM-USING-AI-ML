from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/home')
def career():
    return render_template("hometest.html")


@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      print(result)
      res = result.to_dict(flat=True)
      print("res:", res)

      # Expected form fields in the order the model expects (match the form order in hometest.html)
      expected_fields = [
          'rate_Database Fundamentals',
          'rate_Computer Architecture',
          'rate_Distributed Computing Systems',
          'rate_Cyber Security',
          'rate_Networking',
          'rate_Development',
          'rate_Programming Skills',
          'rate_Project Management',
          'rate_Computer Forensics Fundamentals',
          'rate_Technical Communication',
          'rate_AI ML',
          'rate_se',
          'rate_Business Analysis',
          'rate_Communication skills',
          'rate_Data Science',
          'rate_Troubleshooting skills',
          'rate'  # Graphics Designing select uses name="rate"
      ]

      arr = []
      for key in expected_fields:
          # Try several variants to tolerate spaces/underscores/case
          candidates = [key,
                        key.replace(' ', '_'),
                        key.replace(' ', ''),
                        key.lower(),
                        key.lower().replace(' ', '_'),
                        key.lower().replace(' ', '')]
          value = None
          for c in candidates:
              if c in res:
                  value = res.get(c)
                  break
          if value is None:
              # Try requesting from request.form directly (flask keeps original keys)
              value = result.get(key)
          try:
              # Convert to float, default to 0.0 on failure or missing
              v = float(value) if (value is not None and value != '') else 0.0
          except (ValueError, TypeError):
              v = 0.0
          print(f"Field: {key}, Value: {value}, Converted: {v}")
          arr.append(v)

      data = np.array(arr)
      data = data.reshape(1, -1)
      print("\n=== INPUT ARRAY ===")
      print("Values:", arr)
      print("Unique values:", set(arr))
      print(data)
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))
      label_encoder = pickle.load(open("label_encoder.pkl", 'rb'))
      predictions = loaded_model.predict(data)
     # return render_template('testafter.html',a=predictions)
      
      print(predictions)
      pred = loaded_model.predict_proba(data)
      print("Prediction probabilities:", pred)
      print("Max probability:", pred.max())
      
      # For XGBoost: use a higher threshold based on max probability
      # Only include jobs that have probability >= 80% of max probability
      max_prob = pred.max()
      threshold = max_prob * 0.8  # Jobs with at least 80% of max probability
      pred_binary = pred[0] >= threshold
      
      print("Threshold:", threshold)
      print("Binary predictions:", pred_binary)
      
      i = 0
      j = 0
      index = 0
      res = {}
      final_res = {}
      while j < 17:
          if pred_binary[j]:
              res[index] = j
              index += 1
          j += 1
      # print(j)
      #print(res)
      index = 0
      for key, values in res.items():
          if values != predictions[0]:
              final_res[index] = values
              print('final_res[index]:',final_res[index])
              index += 1
      #print(final_res)
      # Convert numeric predictions back to job names using label encoder
      jobs_list = label_encoder.classes_
      jobs_dict = {i: job_name for i, job_name in enumerate(jobs_list)}
                
      # Convert the primary prediction to job name
      primary_job_index = predictions[0]
      primary_job_name = jobs_dict[primary_job_index]
      print('Primary prediction:', primary_job_name)
      
      data1 = primary_job_name
      print(data1)
      return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
      
@app.route('/job/<job_name>')
def job_detail(job_name):
    # Replace underscores with spaces for display
    job_name_display = job_name.replace('_', ' ')
    # You can add more info for each job here
    return render_template('job_detail.html', job_name=job_name_display)

@app.route('/jobs_info')
def jobs_info():
    # Render a page with info about all jobs
    return render_template('jobs_info.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    # Bind explicitly to IPv4 localhost to avoid other system services
    # (macOS can have services listening on 127.0.0.1:5000 which cause 403s).
    app.run(debug=True, host='127.0.0.1', port=5000)
