from ._anvil_designer import roimoduleTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class roimodule(roimoduleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home')

    self.repeating_panel_roi.items=app_tables.return_on_investment.search()
    # Any code you write here will run before the form opens.
  def edit_return_on_investment(self):
    initial_investment = self.tb_initial.text
    tenure = self.tb_tenure.text
    membership_type = self.tb_member.text
    interest_rate = self.tb_interest_rate.text
    anvil.server.call(
      'edit_return_on_investment',
      self.item,
      initial_investment = self.tb_initial.text,
      tenure = self.tb_tenure.text,
      membership_type = self.tb_member.text,
      interest_rate = self.tb_interest_rate.text,
    )
    # Any code you write here will run before the form opens.
    app_tables.return_on_investment.add_row(initial_investment=initial_investment,membership_type=membership_type,tenure=tenure,interest_rate=interest_rate)
    
    self.repeating_panel_roi.items=app_tables.return_on_investment.search()

    self.tb_initial.text = ""
    self.tb_tenure.text = ""
    self.tb_member.text = ""
    self.tb_interest_rate.text = ""

  
