from django.urls import resolve
from django.test import TestCase
from PresList.views import home_page

from PresList.models import Item, List

from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):
    
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, home_page)
      
   
   
   def test_only_saves_items_when_necessary(self): 
      self.client.get('/')        
      self.assertEqual(Item.objects.count(), 0)
      
class ListViewTest(TestCase):
 
   def test_uses_list_template(self):
      list_ = List.objects.create()        
      response = self.client.get(f'/PresList/{list_.id}/')
      self.assertTemplateUsed(response, 'registration.html')
     
#para sa first entry ng 2nd page
   def test_displays_all_list_items(self):        
       list_ = List.objects.create()        
       Item.objects.create(fullname='Park Jimin(default)', list=list_)        
       Item.objects.create(fullname='1234567', list=list_)
   
   def test_passes_correct_list_to_template(self):       
       other_list = List.objects.create()        
       correct_list = List.objects.create()        
       response = self.client.get(f'/PresList/{correct_list.id}/')
       self.assertEqual(response.context['list'], correct_list)  
 
class NewListTest(TestCase):   

 #1ts page
   def test_redirects_after_POST(self):        
       response = self.client.post('/PresList/new', data={'on': 'A new on','od':'A new od'})                     
       new_list = List.objects.first()        
       self.assertRedirects(response, f'/PresList/{new_list.id}/')
       
       

  #2ndd page to test
class NewItemTest(TestCase):
   def test_can_save_a_POST_request_to_an_existing_list(self):       
      other_list = List.objects.create()        
      correct_list = List.objects.create()        
      
      self.client.post(            
          f'/PresList/{correct_list.id}/add_item',            
          data={'fname': 'A new existing fname','ir': 'A new ir','bname': 'A new bname'}
          ) 
      
      self.assertEqual(Item.objects.count(), 1)        
      new_item = Item.objects.first()        
      self.assertEqual(new_item.fullname, 'A new existing fname')       
      self.assertEqual(new_item.list, correct_list)
   #eto din   
   def test_redirects_to_list_view(self):        
      other_list = List.objects.create()        
      correct_list = List.objects.create()        
      response = self.client.post(            
          f'/PresList/{correct_list.id}/add_item',            
         data={'fname': 'A new fname','ir': 'A new ir','bname': 'A new bname'})  
      self.assertRedirects(response, f'/PresList/{correct_list.id}/')
   
class ORM(TestCase):

   def test_saving_and_retrieving_items(self):
      list_ = List()        
      list_.save()
      
      first_item = Item()        
      first_item.fullname = 'The first (ever) list item' 
      first_item.list = list_ 
      first_item.save()        
               
      second_item = Item()      
      second_item.fullname = 'Item the second'
      second_item.list = list_         
      second_item.save()
       
       
      saved_list = List.objects.first()          
      self.assertEqual(saved_list, list_)
                 
      saved_items = Item.objects.all()
      self.assertEqual(saved_items.count(), 2)
       
      first_saved_item = saved_items[0]
      second_saved_item = saved_items[1]      	     
      self.assertEqual(first_saved_item.fullname, 'The first (ever) list item')
      self.assertEqual(first_saved_item.list, list_)
      self.assertEqual(second_saved_item.fullname, 'Item the second')
      self.assertEqual(second_saved_item.list, list_)



