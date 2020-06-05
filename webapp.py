from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
import model

app = Flask(__name__)

# set optional bootswatch theme
#app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'mosfet'
app.config['MODEL'] = model.environmentSensorData()

admin = Admin(app, name='SqliteDatabase', template_mode='bootstrap3', url='/')
admin.add_view(ModelView(model.environmentSensor))
admin.add_view(ModelView(model.smartMoistureProbe))
# Add administrative views here

app.run(host= '0.0.0.0')
