@app.route('/')
def index():
    return render_template('index.html') # Để nó hiện ra cái bảng nút bấm Nhi vừa tạo
