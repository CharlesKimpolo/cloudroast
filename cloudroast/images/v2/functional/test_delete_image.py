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


class DeleteImageTest(ImagesV2Fixture):
    @tags(type='smoke')
    def test_delete_image(self):
        """ Try to delete an image.

        1) Create standard image.
        2) Delete images
        3) Verify response code is 204 and has no response body
        4) Get image
        5) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_with_invalid_image_id(self):
        """ Delete an image given an invalid id.

        1) Delete image
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_with_deleted_image_id(self):
        """ Delete an image given an already deleted image id.

        1) Create standard image.
        2) Delete image
        3) Verify response code is 204
        4) Delete image
        5) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_that_is_protected(self):
        """ Delete an image that is protected.

        1) Create standard image with protected=true.
        2) Delete image
        3) Verify response code is 403
        """

    @tags(type='negative', net='no')
    def test_delete_image_using_incorrect_url(self):
        """ Delete an image with an incorrect url.

        1) Delete image with incorrect URL endpoint.
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_using_invalid_http_method_post(self):
        """ Delete an image using HTTP method POST.

        1) Delete image with POST
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_with_blank_image_id(self):
        """ Delete an image with missing id.

        1) Delete image without image id
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_delete_image_with_request_body(self):
        """ Delete an image with a request body.

        1) Delete image with request body
        2) Verify response code is 500
        """

    @tags(type='negative', net='no')
    def test_delete_public_image_as_non_admin(self):
        """ Delete a public image as a normal tenant.

        1) Delete image
        2) Verify response code is 403
        """

    @tags(type='negative', net='no')
    def test_delete_shared_image(self):
        """ Delete an image that is shared with tenant.

        1) Delete image
        2) Verify response code is 203
        3) Get image as tenant
        4) Verify response code is 404
        """
