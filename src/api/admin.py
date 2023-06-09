import os
from flask_admin import Admin
from .models import db, User
from .favoritos import Favoritos
from .people import People
from .planets import Planets
from .vehicles import Vehicles
from .favoritepeople import FavoritePeople
from .favoriteplanets import FavoritePlanets
from .favoritevehicles import FavoriteVehicles

from flask_admin.contrib.sqla import ModelView


from flask_admin.menu import MenuCategory, MenuView, MenuLink

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Vehicles, db.session))
    admin.add_view(ModelView(FavoritePlanets, db.session))
    admin.add_view(ModelView(FavoritePeople, db.session))
    admin.add_view(ModelView(FavoriteVehicles, db.session))
    admin.add_view(ModelView(Favoritos, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
    admin.add_link(MenuLink(name='Home Page Backend', url='/'))