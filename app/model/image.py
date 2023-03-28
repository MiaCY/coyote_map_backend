from app import db

class Image(db.Model):
    __tablename__ = 'coyote_map_images'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    imageName = db.Column(db.String, nullable = False)
    imageUrl = db.Column(db.String, nullable = False)
    imageRegion = db.Column(db.Integer, nullable = False) 

    # def to_dict(self):
    #     image_dict = {
    #         "id": self.id,
    #         "imageName": self.imageName,
    #         "imageUrl": self.imageUrl,
    #         "imageRegion": self.imageRegion
    #     }

    #     return image_dict

    # @classmethod
    # def create_image(cls, image_data):
    #     return cls(
    #         imageName=image_data['imageName'],
    #         iamgeUrl=image_data['imageUrl'],
    #         imageRegion=image_data['imageRegion']
    #         )  
