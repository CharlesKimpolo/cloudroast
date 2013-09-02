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


class GetImageMembersTest(ImagesV2Fixture):

    @tags(type='smoke')
    def test_get_members_of_image(self):
        """ Get the members of an image.

        1) Get members list for an image
        2) Verify the response code is 200
        3) Verify the response body is as expected
        """

    @tags(type='negative')
    def test_get_members_for_a_private_image_as_non_admin(self):
        """ Get the members of an image.

        1) Get members list for an image
        2) Verify the response code is 403
        """
