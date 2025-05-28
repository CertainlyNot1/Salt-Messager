from app import create_app,tapatiio,db



app = create_app() 
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    tapatiio.run(app,debug=True)