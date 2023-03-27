from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import plans
from django.urls import reverse

class latestplan(Feed):
    title="Hyperspace"
    link="/drcomments/"
    description="Hyperspace is a broadband connection website"
    def items(self):
        return plans.objects.all()[:5]
    
    def item_title(self,data):
        return data.amount
    
    def item_description(self,data):
        return truncatewords(data.desc,10)
    
    def item_link(self,data):
        return reverse("homepage")
    

