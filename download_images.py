from simple_image_download import simple_image_download as simp

resopnse = simp.simple_image_download

keywords = ["building workers"]

for kw in keywords:
    resopnse().download(kw, 100)