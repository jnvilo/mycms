"""
Every CMSApp must implement a class called Controller inside the controller 
module. MyCMS will search the cmsapp directory for a controller.py and will 
attempt to import a Controller class. The controller class must be an inhereted 
class from CMSAppController.
"""

from mycms.cmsapps.base import CMSPageView
from mycms.cmsapps.base import CMSPageData
from mycms.cmsapps.decorators import cms_attribute



class PageData(CMSPageData):
       
   @cms_attribute
   def categories(self):
      """
      Returns all child CMSNodes that have the cmsapp name as category.
      """
      pass
   
   def articles(self):
      """
      Returns all child CMSNodes that have the cmsapp name as article.
      """
      pass
    

class PageView(CMSPageView):
   """
   The Controller implements the logic on producing the necessary attributes
   required to render the View(the django template).
   """
   class Meta:
   
      JAVASCRIPT = []
      CSS = []
      TEMPLATE = "category/category.html"  
      PAGEDATA = PageData 
   
      
   
        
        
    
    