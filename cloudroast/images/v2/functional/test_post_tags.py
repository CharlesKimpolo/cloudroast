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


class PostImageTagsTest(ImagesV2Fixture):

    @tags(type='smoke')
    def test_add_tag_to_image(self):
        """ Add tag to an image.

        1) Add a tag to existing image
        2) Verify the response code is 200
        3) Verify that the added tag is in the list of image tags.
        """

    @tags(type='positive')
    def test_add_multiple_tags_to_image(self):
        """ Add multiple tags to an image.

        1) Add a list of tags to existing image
        2) Verify the response code is 200
        3) Verify that the added tags are in the list of image tags.ge.
        """

    @tags(type='positive')
    def test_add_duplicate_tag_to_image(self):
        """ Add multiple tags to an image.

        1) Try to add an existing tag to an image
        2) Verify the response code is 200
        3) Verify that duplication is ignored
        """

    @tags(type='negative')
    def test_add_empty_tag_to_image(self):
        """ Add multiple tags to an image.

        1) Try to add an empty tag to an image
        2) Verify the response code is 404
        """
