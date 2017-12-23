from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404, render_to_response, redirect, render, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView

from Profile.models import Profile
from Coordinator.forms import ProfileForm as ProfileForm_Coordinator
from Client.forms import ProfileForm as ProfileForm_Client


class ProfileView(FormView):
    template_name = 'edit_profile.html'

    def get(self, *args, **kwargs):
        # self.id = self.kwargs['id']
        self.id = kwargs.get('id', None)
        profile = get_object_or_404(User, id=self.id)
        profile_group_user = Group.objects.get(user=self.id)
        if profile_group_user.name == 'Clients':
            ProfileView.form_class = ProfileForm_Client
        else:
            ProfileView.form_class = ProfileForm_Coordinator
        return super(ProfileView, self).get(*args, **kwargs)

    def post(self, request, id):
        self.id = id
        # profile = get_object_or_404(User, id=self.id)
        profile_group_user = Group.objects.get(user=self.id)
        # if AddressForm_applicant:
        if profile_group_user.name == 'Clients':
            form = ProfileForm_Client(request.POST)

            if form.is_valid():
                address = self.request.POST['address']
                # gender = self.request.POST['gender']
                contact_no = self.request.POST['contact_no']
                if not Profile.objects.filter(user_id=self.id).exists():

                    profile = Profile(address=address, contact_no=contact_no, user_id=self.id)
                    # profile = Profile(address=address, gender=gender, contact_no=contact_no, user_id=self.id)
                    profile.save()
                    return redirect('/')
                else:
                    profile = Profile.objects.get(user_id=self.id)
                    profile.address = address
                    # profile.gender = gender
                    profile.contact_no = contact_no
                    profile.save()

                    return redirect('/')

            else:
                # print('Hello')
                # return render_to_response('edit_profile.html', {'form': form})
                return render(request, 'edit_profile.html', {'form': form})

        else:
            form = ProfileForm_Coordinator(request.POST, request.FILES)

            if form.is_valid():

                business_name = self.request.POST['business_name']
                cover_photo = self.request.FILES['cover_photo']
                address = self.request.POST['address']
                contact_no = self.request.POST['contact_no']
                fax_no = self.request.POST['fax_no']
                tel_no = self.request.POST['tel_no']
                if not Profile.objects.filter(user_id=self.id).exists():

                    profile = Profile(business_name=business_name, cover_photo=cover_photo, address=address,
                                      contact_no=contact_no, fax_no=fax_no,
                                      tel_no=tel_no, user_id=self.id)
                    profile.save()
                    # return HttpResponseRedirect('/')
                    # return redirect(request, '/', context_instance=RequestContext(request))
                    # return redirect('home.html')
                    return redirect('/')
                else:
                    profile = Profile.objects.get(user_id=self.id)
                    profile.business_name = business_name
                    profile.cover_photo = cover_photo
                    profile.address = address
                    profile.contact_no = contact_no
                    profile.tel_no = tel_no
                    profile.fax_no = fax_no
                    profile.save()
                    # return redirect('home.html')
            else:
                return render(request, '/', context_instance=RequestContext(request))
                # return render_to_response('edit_profile.html', {'form': form})
                # return render(request, 'edit_profile.html', {'form': form})
