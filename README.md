## PIP Befehl zum installieren der Module:

```pip3 install django django-extensions django-crispy-forms djangorestframework django-bootstrap3```



## Script zum Nutzen der Klassen: 

```
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bw3webinterface.settings')
django.setup()
from bw3backend import models as webmodule
webmodule.client.objects.all()
```


## Zugangsdaten für die Develop-Datenbank:

Nutzername: boswatch_test <br>
Passwort:   bw3test123
