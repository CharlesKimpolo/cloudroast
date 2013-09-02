"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from cafe.drivers.unittest.decorators import tags
from cloudroast.images.v2.fixtures import ImagesV2Fixture


class GetImageFileTest(ImagesV2Fixture):
    @tags(type='smoke')
    def test_download_image_data(self):
        """Downloads binary data for an image.

        1) Register new image
        2) Verify response code is 200
        3) Upload image with an image file
        4) Download binary image data
        5) Verify response code is 200
        6) Verify that the downloaded image data is same as uploaded binary
        image data
        """

    @tags(type='negative')
    def test_download_image_without_data:
        """Download binary data for an image that has none.

        1) Register new image
        2) Verify response code is 200
        4) Download binary image data
        5) Verify response code is 404
        """
