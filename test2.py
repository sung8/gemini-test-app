# import requests
# from vertexai.preview.generative_models import GenerativeModel, Image
#
# def load_image_from_url(image_url):
#     response = requests.get(image_url)
#     return Image.from_bytes(response.context)
#
# # ensure that all file images are the same
# landmark1 = load_image_from_url("https://www.msccruisesusa.com/-/media/global-contents/destinations/ports/usa/san-francisco/cruise-to-san-francisco-usa.jpg")
# landmark2 = load_image_from_url("https://nationalparkexpress.com/wp-content/uploads/2022/05/grand-canyon-west-1.jpg")
#
# model = GenerativeModel("gemini-pro-vision")
#
# response = model.generate_content(
#     [landmark1, "city: San Francisco, country: United States",
#      landmark2, ]
# )
#
# print(response)