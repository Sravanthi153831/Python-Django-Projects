import json
import os
class VFXAssest:
  """Class to represent a single VFX Asset (OOP Concept)"""
  def _init_(self, asset_id, asset_id, asset_name, asset_type, status):
     self.asset_id = asset_id
     self.asset_name = asset_name
     self.asset_type = asset_type
     self.status = status
 def to_dict(self):
     """Converts object data into  dictionary""" 
     "Asset_ID": self.asset_id,
     "Asset_Name": self.asset_name,
     "Asset_Type": self.assef_taye,
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
        json data = [asset.to_dict() for asset in self.asset in self.assets]
        json.dump(json_data,file,
def load_data(self):
         """Reads and loads asset data from a JSON file"""
         if so.path.exists
              with open(self filename, "r") as file:
                   data = json.load(file)
                   for item in data:
                      asset = VFXAsset(
                          item["Asset_ID"],
                          item["Asset_Name"],
                          item["Asset_Type"],
                          item["Status "]
                      )
self.assets.append(asset)
manager = VFXPipelineManager()
asset1 = VXFAsset(
     "Dragon_Model"
     "3D Model]",
     "Completed"
)
manager_add_asset(asset1)


    
    
                      
                          
