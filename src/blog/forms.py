from django import forms
from blog.models import UserProfile,Post


class createPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file','manager']
    
    def __init__(self, *args, **kwargs):
        userss = kwargs.pop('userss')
        super(createPost,self).__init__( *args, **kwargs)
        
        user_idsss = UserProfile.objects.filter(user__username=userss).values_list('contact' , flat=True)
        self.fields['manager'].queryset = UserProfile.objects.filter(id__in = user_idsss)