from  registrations.build_app import create_app
  
app=create_app()

@app.route('/')
def index():
  return "working"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9000,debug=True)