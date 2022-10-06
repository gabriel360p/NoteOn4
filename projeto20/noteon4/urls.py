from django.urls import path
from . import views


app_name="noteon4"

urlpatterns=[
	#tTelas:
	path('',views.viewtindex,name="viewtindex"),
	

	
	path('tlogin/',views.viewtlogin,name="tlogin"),

	path('tregistro/',views.viewtregistro,name="tregistro"),
	
	path('tvernota/<int:id> <int:id2>',views.viewtvernota,name="tvernota"),

	path('tpainel/<int:id>',views.viewtpainel,name="tpainel"),
	
	path('tperfil/<int:id>',views.viewtperfil,name="tperfil"),
	

	#defbtn:
	path('defbtnregistro/',views.defbtnregistro,name='defbtnregistro'),

	path('defbtnlogin/',views.defbtnlogin,name="defbtnlogin"),
	
	path('defbtnnvnota/<int:id>',views.defbtnnvnota,name="defbtnnvnota"),

	path('defsavenvnota/<int:id>',views.defsavenvnota,name="defsavenvnota"),

	path('defeditar/<int:id> <int:id2>',views.defeditar,name="defeditar"),

	path('defeditarperfil/<int:id>',views.defeditarperfil,name="defeditarperfil"),
	
	path('defdeletar/<int:id> <int:id2>',views.defdeletar,name="defdeletar"),
]