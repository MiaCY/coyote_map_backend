from flask import Blueprint, jsonify, request
from google.cloud import storage
from app.model.image import Image
from app import db


image_bp = Blueprint("images", __name__, url_prefix="/images")


# # working_dir = pathlib.Path.cwd()
# # files_folder = working_dir.joinpath('Files')
# # downloads_folder = working_dir.joinpath('Downloads')
bucket_name = 'coyote_map_bucket'

storage_client = storage.Client()
# gcs = GCS(storage_client)


@image_bp.route("", methods=["POST"])
def upload_image_to_gcs():
  # if not bucket_name in gcs.list_buckets():
  #   bucket_gcs = gcs.create_bucket('coyote_map_bucket', 'STANDARD')
  # else:
  #   bucket_gcs = gcs.get_bucket(bucket_name)
  # file_path = None
  # gcs.upload_file(bucket_gcs, file_path.name, str(file_path))
  file = request.files['image']
  region = request.headers.get('region')
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(file.filename)
  
  # metageneration_match_precondition = None

  # metageneration_match_precondition = blob.metageneration

  metadata = {'region': region}
  blob.metadata = metadata

  blob.upload_from_file(file)

  public_url = f'http://storage.googleapis.com/{bucket_name}/{file.filename}'

  # blob.patch(if_metageneration_not_match=metageneration_match_precondition )

  new_image = Image(
     imageName=file.filename,
     imageUrl=public_url,
     imageRegion=region
  )

  existing_image = Image.query.filter_by(
     imageName=file.filename
  ).first()

  if existing_image:
    existing_image.imageUrl=public_url
    existing_image.imageRegion=region
    db.session.merge(existing_image)
  else:
    db.session.add(new_image)

  db.session.commit()




  return public_url


@image_bp.route("", methods=["GET"])
def get_all_images():
    images = Image.query.all()
    # all_images = [image.to_dict() for image in images]
    all_url = []
    for image in images:
       all_url.append(image.imageUrl)
       

    return jsonify(all_url)

@image_bp.route("/<region_number>", methods=["GET"])
def get_images_by_region(region_number):
    images = Image.query.filter_by(imageRegion=region_number)
    images_of_region = [image.to_dict()['imageUrl'] for image in images]
          

    return jsonify(images_of_region)
   
   
   



