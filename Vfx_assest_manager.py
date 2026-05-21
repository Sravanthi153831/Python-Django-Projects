3
import json
imprt os
class VFXAssest:
  """Class to represent a single VFX Asset (OOP Concept)"""
  def _init_(self, asset_id, asset_id, asset_name, asset_type, status="In Progress"):
     self.asset_id = asset_id
     self.asset_name = asset_name
     self.asset_type = asset_type
     self.status = status
 def to_dict(self):lize
     """Converts object data into a dictionary for JSON serialization"""
 eturn { 
     "Asset_ID": self.asset_id,
     "Asset_name": self.asset_name,
     "Asset_TYP$E": self.assef_taye,
     "Status": self.status
 ass. VFXPeliline Manager:
  """Class to handle JSON read/write 
  def _init_(self, filename="Vfx_pipeline_data.json"):
      self.filename = filename
      self.assets = []
      self.load_data()
 def add "asset(self , asset):
     """Adds a new asset to the 
       self.
  
  
  
