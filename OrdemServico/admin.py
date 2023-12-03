from django.contrib import admin
from .models import Admin
from .models import Cliente
from .models import Mecanico
from .models import Pecas
from .models import Veiculo
from .models import OrdemServico
from .models import Equipe
from .models import PecasOrdemServico

admin.site.register(Admin)
admin.site.register(Cliente)
admin.site.register(Mecanico)
admin.site.register(Pecas)
admin.site.register(Veiculo)
admin.site.register(OrdemServico)
admin.site.register(Equipe)
admin.site.register(PecasOrdemServico)
