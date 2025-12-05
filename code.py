class Library:
  def __init__(self,zip_code):
    self.zip_code = zip_code
    
  def display_zip(self):
    print(self.zip_code)

ala_lib = Library(439875)

ala_lib.display_zip()

