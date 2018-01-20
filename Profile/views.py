from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic.edit import FormView
from Profile.models import Profile
from Coordinator.forms import ProfileForm as ProfileForm_Coordinator
from Client.forms import ProfileForm as ProfileForm_Client


class ProfileView(FormView):
    template_name = 'edit_profile.html'

    def get(self, *args, **kwargs):
        self.id = kwargs.get('id', None)
        profile_group_user = Group.objects.get(user=self.id)
        if profile_group_user.name == 'Clients':
            ProfileView.form_class = ProfileForm_Client
        else:
            ProfileView.form_class = ProfileForm_Coordinator
        return super(ProfileView, self).get(*args, **kwargs)

    def post(self, request, id):
        self.id = id
        profile_group_user = Group.objects.get(user=self.id)
        if profile_group_user.name == 'Clients':
            form = ProfileForm_Client(request.POST)

            if form.is_valid():
                address = self.request.POST['address']
                contact_no = self.request.POST['contact_no']
                if not Profile.objects.filter(user_id=self.id).exists():

                    profile = Profile(address=address, contact_no=contact_no, user_id=self.id)
                    profile.save()
                    return redirect('/')
                else:
                    profile = Profile.objects.get(user_id=self.id)
                    profile.address = address
                    profile.contact_no = contact_no
                    profile.save()

                    return redirect('/')

            else:
                return render(request, 'edit_profile.html', {'form': form})

        else:
            form = ProfileForm_Coordinator(request.POST, request.FILES)

            if form.is_valid():
                business_name = self.request.POST['business_name']
                cover_photo = self.request.FILES['cover_photo']
                business_plate = self.request.FILES['business_plate']
                business_permit = self.request.FILES['business_permit']
                address = self.request.POST['address']
                contact_no = self.request.POST['contact_no']
                description = self.request.POST['description']
                if not Profile.objects.filter(user_id=self.id).exists():

                    profile = Profile(business_name=business_name, cover_photo=cover_photo, address=address,
                                      contact_no=contact_no, business_permit=business_permit,
                                      business_plate=business_plate, description=description, user_id=self.id)
                    profile.save()
                    # return redirect('/')
                    return render(request, 'Coordinator/validation.html')
                else:
                    profile = Profile.objects.get(user_id=self.id)
                    profile.business_name = business_name
                    profile.cover_photo = cover_photo
                    profile.address = address
                    profile.contact_no = contact_no
                    profile.business_plate = business_plate
                    profile.business_permit = business_permit
                    profile.description = description
                    profile.save()
            else:
                return redirect('/', context_instance=RequestContext(request))
                # return render(request, 'edit_profile.html', {'form':form})
                # return render(request, '/', context_instance=RequestContext(request))
