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


class PutImageTest(ImagesV2Fixture):

    @tags(type='smoke')
    def test_upload_image(self):
        """ Register and upload new image.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file
        4) Verify response code is 2xx
        """

    @tags(type='negative')
    def test_upload_image_with_invalid_content_type(self):
        """ Register and upload new image with invalid content-type.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file
        4) Verify response code is 4xx
        """

    @tags(type='negative')
    def test_upload_image_with_mismatched_file_format(self):
        """ Register and upload new image with a different file format than
        registered.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file
        4) Verify response code is 415
        """

    @tags(type='negative')
    def test_upload_image_using_incorrect_url(self):
        """ Register and upload new image using an incorrect URL.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file to incorrect url
        4) Verify response code is 404
        """

    @tags(type='negative')
    def test_upload_image_using_incorrect_http_method_post(self):
        """ Register and upload new image using an incorrect URL.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file using POST
        4) Verify response code is 404
        """

    @tags(type='negative')
    def test_upload_image_using_larger_size(self):
        """ Register and upload new image using larger file.

        1) Register new image
        2) Verify response code is 200
        3) Update image with image file
        4) Verify response code is 2xx
        """

    @tags(type='negative')
    def test_upload_image_without_image_id(self):
        """ Register and upload new image without image id.

        1) Register new image
        2) Verify response code is 200
        3) Update image without image id.
        4) Verify response code is 404
        """

    @tags(type='negative')
    def test_upload_image_with_invalid_image_id(self):
        """ Register and upload new image with invalid image id.

        1) Register new image
        2) Verify response code is 200
        3) Update image with invalid image id.
        4) Verify response code is 404
        """

    @tags(type='positive')
    def test_upload_image_that_already_has_data(self):
        """ Register and upload image data twice.

        1) Register new image
        2) Verify response code is 200
        3) Update image with data
        4) Verify response code is 2xx
        5) Update image with data
        6) Verify response code is 2xx
        """
