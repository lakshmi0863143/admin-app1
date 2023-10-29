from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.a_teams')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.borrowers') 

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.lenders')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')
    
  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.revenue_share')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.risk_pool')

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_cms')

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_reports')


    
    
    
    
    
    
    
    
    

 

