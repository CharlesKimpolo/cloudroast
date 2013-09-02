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


class PostImageMembersTest(ImagesV2Fixture):

    @tags(type='smoke')
    def test_add_member_to_image(self):
        """Add member(tenant_id) to an image.

        1) Add a member (tenant_id) to an image
        2) Verify the response code is 204
        3) Verify that the image member list is not empty and contains the added member.
        """

    @tags(type='negative')
    def test_add_member_to_private_image_as_non_admin(self):
        """Add member(tenant_id) to a private image as non admin user.

        1) Add a member (tenant_id) to an image
        2) Verify the response code is 403
        3) Verify that the image member list is not empty and contains the added member.
        """
