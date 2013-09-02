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


class PostImagesTest(ImagesV2Fixture):
    """Test creation/registration of images."""

    @tags(type='positive')
    def test_register_image_with_compulsory_properties(self):
        """Register a VM image with minimum compulsory properties.

        1) Register new image.
        2) Verify the response code is 200
        3) Verify the model returned has correct properties.
        """

    @tags(type='positive')
    def test_register_image_with_optional_properties(self):
        """Register a VM image with additional optional properties.

        1) Register new image.
        2) Verify the response code is 200
        3) Verify the model returned has correct properties.
        """

    @tags(type='negative')
    def test_register_image_that_is_already_registered(self):
        """Register a VM image that is already registered.

        1) Register new image.
        2) Verify the response code is 4xx
        """

    @tags(type='negative')
    def test_register_image_without_compulsory_properties(self):
        """Register a VM image without compulsory properties.

        1) Register new image.
        2) Verify the response code is 4xx
        """

    @tags(type='negative')
    def test_register_image_with_special_characters_in_name(self):
        """Register a VM image with special characters in its name.

        1) Register new image.
        2) Verify the response code is 4xx
        """

    @tags(type='negative')
    def test_register_image_with_unacceptable_disk_format(self):
        """Register a VM image with a bogus disk format.

        1) Register new image.
        2) Verify the response code is 4xx
        """

    @tags(type='negative')
    def test_register_image_with_unacceptable_container_format(self):
        """Register a VM image with a bogus container format.

        1) Register new image.
        2) Verify the response code is 4xx
        """
