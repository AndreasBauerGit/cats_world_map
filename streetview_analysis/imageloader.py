# Import google_streetview for the api and helper module
import google_streetview.api
import google_streetview.helpers

class ImageLoader:
    def __init__(self, size):
        self.size = size


    def read_image(self, apiargs):
        # Get a list of all possible queries from multiple parameters
        api_list = google_streetview.helpers.api_list(apiargs)

        # Create a results object for all possible queries
        results = google_streetview.api.results(api_list)

        # Preview results
        results.preview()

        # Download images to directory 'downloads'
        results.download_links('drive/colab/street_view/')
        return results

image_loader = ImageLoader((600, 600))

# Create a dictionary with multiple parameters separated by ;
apiargs = {
  'location': '23.87,90.3939;23.87,90.3944;23.87,90.3951;23.87,90.3959',
  'size': '640x300',
  'heading': '0;90;180',

  'pitch': '0',
  'key': 'google_dev_key'
}

image_loader.read_image(apiargs)