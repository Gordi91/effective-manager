from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required

from core.decorators import superuser_required_for_classes, superuser_required, stuff_required_for_classes
from core.decorators import IfNotStaffMixin, IfNotSuperuserMixin
from .models import Client, Certificate
from .forms import ClientForm, CertificateForm

# Clients


class ShowClients(IfNotStaffMixin, View):
    def get(self, request):
        template_name = 'certificates/show_clients.html'
        if request.user.is_superuser:
            clients = Client.objects.all()
        elif request.user.is_staff:
            clients = Client.objects.prefetch_related('certificate_set').\
                filter(Q(certificate__poller=request.user) | Q(certificate__certificator=request.user)).distinct().\
                order_by('certificate__added_to_database')
        return render(request, template_name, {'clients': clients})


@superuser_required_for_classes()
class NewClient(View):
    def get(self, request):
        template_name = 'certificates/new_client.html'
        form = ClientForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            client_id = form.instance.id
        return redirect('show_client', id=client_id)

@superuser_required_for_classes()
class ModifyClient(View):

    def get(self, request, id):
        template_name = 'certificates/new_client.html'
        client = get_object_or_404(Client, pk=id)
        form = ClientForm(instance=client)

        return render(request, template_name, {
            'form': form,
            'client': client,
        })

    def post(self, request, id):
        instance = get_object_or_404(Client, pk=id)
        form = ClientForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('show_client', id=id)



class ShowClient(View):
    def get(self, request, id):
        template_name = 'certificates/show_client.html'
        client = Client.objects.get(pk=id)

        return render(request, template_name, {
            'client': client,
        })


@superuser_required_for_classes()
class DeleteClient(View):
    def get(self, request, id):
        Client.objects.get(pk=id).delete()
        return redirect('show_clients')


# Certificates


class CertificatesListView(IfNotStaffMixin, View):
    def get(self, request):
        template_name = 'certificates/certificate_list.html'
        if request.user.is_superuser:
            certificate_list = Certificate.objects.all()
        elif request.user.is_staff:
            certificate_list = Certificate.objects.\
                filter(Q(poller=request.user) | Q(certificator=request.user)).distinct().\
                order_by('added_to_database')
        return render(request, template_name, {'certificate_list': certificate_list})


@superuser_required_for_classes()
class NewCertificate(View):
    def get(self, request):
        template_name = 'certificates/new_certificate.html'
        form = CertificateForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request):
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            if form.cleaned_data.get('poller'):
                certificate.assigne_to_poller()
            if form.cleaned_data.get('certificator'):
                certificate.assigne_to_certificator()
            certificate_id = form.instance.id
        return redirect('show_certificate', id=certificate_id)



class ShowCertificate(View):
    def get(self, request, id):
        template_name = 'certificates/certificate_detail.html'
        certificate = Certificate.objects.get(pk=id)
        try:
            is_poller = (certificate.poller.get_username()==request.user.username)
        except AttributeError:
            is_poller = False
        try:
            is_certificator = (certificate.certificator.get_username()==request.user.username)
        except AttributeError:
            is_certificator = False
        return render(request, template_name, {
            'certificate': certificate,
            'is_poller': is_poller,
            'is_certificator': is_certificator,
        })


@superuser_required_for_classes()
class DeleteCertificate(View):
    def get(self, request, id):
        Certificate.objects.get(pk=id).delete()
        return redirect('show_certificates')


@superuser_required_for_classes()
class ModifyCertificate(View):

    def get(self, request, id):
        template_name = 'certificates/new_certificate.html'
        certificate = get_object_or_404(Certificate, pk=id)
        form = CertificateForm(instance=certificate)

        return render(request, template_name, {
            'form': form,
            'certificate': certificate,
        })

    def post(self, request, id):
        certificate = get_object_or_404(Certificate, pk=id)
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('poller'):
                certificate.assigne_to_poller()
            if form.cleaned_data.get('certificator'):
                certificate.assigne_to_certificator()
        return redirect('show_certificate', id=id)

# class CertificateDetailView(DetailView):
#     model = Certificate


@staff_member_required
def poll_done(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    certificate.set_status_greater_then(3)
    return redirect('show_certificate', id=certificate.pk)


@staff_member_required
def certificate_done(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    certificate.set_status_greater_then(5)
    return redirect('show_certificate', id=certificate.pk)