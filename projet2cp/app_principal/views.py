from email import message
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .forms import switchform, vlanform, switchConfigForm, modeleform, CreateSuperUserForm
from .models import switch, vlan, Port, ModeleSwitch
from django.contrib import messages
from django.contrib.auth import decorators
from django.contrib.auth.models import User, Group, Permission
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

''' def user_of_stores(user):
    if user.is_authenticated() and user.has_perm("stores.change_store"):
        return True
    else:
        return False 
        
        @user_passes_test(user_of_stores)
'''
#@permission_required('app_principal.add_switch')

def ajoutswitch(request):

        form = switchform(request.POST or None)
        if request.method == 'POST':
                if form.is_valid():
                        s=form.save()
                        form.save()
                        id=s.id
                        messages.success(request, ('le switch a été creé avec succés!'))  
                        return redirect('app_principal:config_switch', id)
                else:
                        messages.error(request, ('Echec lors de la création, veuillez réessayer une autre fois.')) 
        context = {'form':form, 'choix':'switch','operation':'Ajout',}
        return render (request ,'app_principal/form_validation.html',context)

#@permission_required('app_principal.add_vlan')

def ajoutvlan(request):

        form=vlanform(request.POST or None)

        if request.method == 'POST':
                if form.is_valid():
                        form.save()
        context = {'form':form, 'choix':'vlan','operation':'Ajout',}
        return render (request ,'app_principal/form_validation.html',context)

#@permission_required('app_principal.change_switch')

def switchConfig(request, switch_id):
    s = get_object_or_404(switch, id=switch_id)
    if request.method == 'POST': #si le switch d'id = switch_id n'existe pas on renvoie 404
        form= switchConfigForm(request.POST,instance=s)

        if form.is_valid():
            form.save()
            if s.etat==switch.passif:
                s.etat=switch.actif
                s.save()
            return redirect('app_principal:switch')
        
            # configuration du `switch` existant dans la base de données
            # redirect vers le form de ports---à faire
        
    else:
        form = switchConfigForm(instance=s)
    return render(request,
                'app_principal/form_validation.html',
                {'form':form, 'choix':s.nom,'operation':'Configuration',})	
        
#@permission_required('app_principal.view_switch')
       
def switchtab(request):
        cols_principales=['nom','bloc','local','armoire','Cascade depuis']
        cols_detail=['Adresse MAC','Numero de Serie',"Numero d'inventaire","Date d'achat",'Marque','Modèle']
        switchs = switch.objects.all()
        context={'objet':'switchs','objets':switchs,'colsp':cols_principales,'colsd':cols_detail,}
        return render(request, 'app_principal/offictable.html',context)

#@permission_required('app_principal.view_vlan')

def vlan_tab(request):
        cols_principales=['num_Vlan ','nom','ip','masque','passerelle']
        cols_detail=[]
        vlans = vlan.objects.all()
        context={'objet':'vlans','objets':vlans,'colsp':cols_principales,'colsd':cols_detail,}
        return render(request, 'app_principal/offictable.html',context)

#@permission_required('app_principal.view_port')
def port_tab(request):
        cols_principales=['num_port','type_port','etat','vlan_associe','elm_suiv']
        cols_detail=[]
        ports = Port.objects.all()
        context={'objet':'ports','objets':ports,'colsp':cols_principales,'colsd':cols_detail,}
        return render(request, 'app_principal/offictable.html',context)

#@permission_required('app_principal.view_modele')
def modele_tab(request):
        cols_principales=['nbr_port','nbr_port_SFP','nbr_port_GE','nbr_port_FE']
        cols_detail=[]
        modeles = ModeleSwitch.objects.all()
        context={'objet':'modèles','objets':modeles,'colsp':cols_principales,'colsd':cols_detail,}
        return render(request, 'app_principal/offictable.html',context)

#@user_passes_test(user.is_superuser)

def register_super_user(request):
        form=CreateSuperUserForm(request.POST or None)
        if request.method == 'POST': #ladmin a introduit lemail
                
                if form.is_valid():
                        form.password1 = User.objects.make_random_password()
                        form.password2=form.password1
                        try:
                                username=form.email_clean()
                        except ValidationError:
                                messages.warning(request,("cet email existe déja"))
                        else:
                                form.username =username
                                form.save()
                                messages.success(request,("Un nouveau superutilisateur a été creé avec succés!"))   
                                user=User.objects.get(email=form.cleaned_data["email"])
                                user.is_superuser=True #on le rend un superutilisateur
                                user.is_active=False #il doit confirmer son email
                                user.save() #on sauvegarde l'user dans la bdd
                                #envoie d'un email
                                msg_html = render_to_string('app_principal/email.html', {'user': user})
                                EmailMultiAlternatives(
                                        "activation de compte",
                                        msg_html,
                                        settings.EMAIL_HOST_USER,
                                        [str(user.email)],
                                )
                                if i==0 :
                                        messages.warning(request,('message not sent'))
                                if i==1:
                                        messages.success(request,('message sent'))

                         
                else:
                        messages.error(request,("Echec! l'utilisateur n'a pas été creé."))            
               
        return render(request,'app_principal/gestionuser.html',{'form':form})	

        
