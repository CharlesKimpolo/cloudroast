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


class PatchImageTest(ImagesV2Fixture):
    @tags(type='smoke')
    def test_update_image_name(self):
        """Try update an image's name property.

        1) Update name of an image
        2) Verify response code is 204
        3) Verify response is an image with correct properties.
        """

    @tags(type='positive', net='no')
    def test_add_image_property(self):
        """Try to add an image property.

        1) Update image with new property.
        2) Verify response code is 204
        3) Verify response is an image with correct properties and new property
        """

    @tags(type='positive', net='no')
    def test_remove_image_property(self):
        """Try to remove an image property.

        1) Update image to remove property.
        2) Verify response code is 204
        3) Verify response is an image with correct properties and removed
        property missing
        """

    @tags(type='positive', net='no')
    def test_update_image_with_optional_properties(self):
        """Try to update an image's optional properties.

        1) Update image's id, visibility, tags.
        2) Verify response code is 204
        3) Verify response is an image with correct properties and optional
        parameters exist
        """

    @tags(type='negative', net='no')
    def test_update_image_with_invalid_name(self):
        """Try to update an image's name with invalid characters.

        1) Update image's name with invalid characters
        2) Verify response code is 4xx
        """

    @tags(type='negative', net='no')
    def test_update_image_with_invalid_image_property(self):
        """Try to update an image with invalid property.

        1) Update image with bogus property
        2) Verify response code is 4xx
        """

    @tags(type='negative', net='no')
    def test_update_image_using_incorrect_url(self):
        """Try to update an image using wrong URL.

        1) Update image with incorrect URL
        2) Verify response code is 4xx
        """

    @tags(type='negative', net='no')
    def test_update_image_using_incorrect_http_method_put(self):
        """Try to update an image using wrong HTTP method, PUT.

        1) Update image using PUT
        2) Verify response code is 404
        """

    @tags(type='positive', net='no')
    def test_update_image_using_larger_size(self):
        """Try to update an image's size property.

        1) Update image's size
        2) Verify response code is 204
        3) Verify response is an image with correct properties and new size
        """

    @tags(type='negative', net='no')
    def test_update_image_using_blank_image_id(self):
        """Try to update an image using no image id.

        1) Update image without image id
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_update_image_using_invalid_image_id(self):
        """Try to update an image using invalid image id.

        1) Update image with invalid image id
        2) Verify response code is 404
        """

    @tags(type='negative', net='no')
    def test_update_image_using_incorrect_request_body(self):
        """Try to update an image using incorrect request body.

        1) Update image with incorrect request body.
        2) Verify response code is 415
        """

    @tags(type='negative', net='no')
    def test_update_image_with_new_owner(self):
        """Try to update owner of image.

        1) Update image with new owner.
        2) Verify response code is 4xx
        """

    @tags(type='negative', net='no')
    def test_update_image_with_new_location_and_active(self):
        """Try to update location of an active image.

        1) Update active image with new location.
        2) Verify response code is 4xx
        """
