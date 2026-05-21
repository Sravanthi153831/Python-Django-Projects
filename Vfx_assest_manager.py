import json
import as
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
 def add_asset(self , asset):
     """Adds a new asset to the tracking system"""
       self.assets.append(asset)
       self.save_data()
       print(f"✔️ Asset '{assets.asset_name}' successfully added to pipeline.") 
def save_data(self):
    """Writes current asset data to a JSON file"""
    with open(self.filename, 'w') as file"""
        Json data = [asset.to_dict() for asset in self.asset in self.assets]
        
  
  
