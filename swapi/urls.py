from __future__ import unicode_literals
import os,sys
import re
BASE_API_PATH=""
API_VERSION=""

if "BASE_API_PATH" in os.environ:
    BASE_API_PATH = re.sub('[^ a-zA-Z0-9]', '', str(os.environ["BASE_API_PATH"]))
    BASE_API_PATH=BASE_API_PATH+"/"

if "API_VERSION" in os.environ:
    API_VERSION = re.sub('[^ a-zA-Z0-9]', '', str(os.environ["API_VERSION"]))
    API_VERSION=API_VERSION+"/"


from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from resources import views

router = routers.DefaultRouter()

router.register(r"people", views.PeopleViewSet)
router.register(r"planets", views.PlanetViewSet)
router.register(r"films", views.FilmViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"vehicles", views.VehicleViewSet)
router.register(r"starships", views.StarshipViewSet)


urlpatterns = patterns("",
    url(r"^"+BASE_API_PATH+"admin/", include(admin.site.urls)),
    url(r"^"+BASE_API_PATH+"$", "swapi.views.index"),
    url(r"^"+BASE_API_PATH+"documentation$", "swapi.views.documentation"),
    url(r"^"+BASE_API_PATH+"about$", "swapi.views.about"),
    url(r"^"+BASE_API_PATH+"stats$", "swapi.views.stats"),
    url(r"^"+BASE_API_PATH+"stripe/donation", "swapi.views.stripe_donation"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"people/schema$", "resources.schemas.people"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"planets/schema$", "resources.schemas.planets"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"films/schema$", "resources.schemas.films"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"species/schema$", "resources.schemas.species"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"vehicles/schema$", "resources.schemas.vehicles"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION+"starships/schema$", "resources.schemas.starships"),
    url(r"^"+BASE_API_PATH+"api/"+API_VERSION, include(router.urls)),
)
